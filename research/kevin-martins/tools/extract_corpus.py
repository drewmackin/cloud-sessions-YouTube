#!/usr/bin/env python3
"""Rebuild verbatim transcript windows from the raw Perplexity search results in agent logs.

  python3 research/kevin-martins/tools/extract_corpus.py LOG.jsonl [LOG.jsonl ...]

Every perplexity_search result is stored in the logs exactly as the API returned it. This script parses
those results (no retyping), splits each YouTube hit into its contiguous transcript windows, drops
windows that are exact duplicates or fully contained in a longer one, and writes
research/kevin-martins/corpus/<videoId>.md with the windows ordered by their first timestamp.
Windows are separated by a line containing only "[…]" so a quote can never silently span a gap.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "corpus"
RESULT_HEAD = re.compile(r"^\d+\. \*\*(.+?)\*\*\s*$")
URL = re.compile(r"^\s*URL: (\S+)")
VIDEO_ID = re.compile(r"(?:v=|youtu\.be/|/shorts/|/live/)([\w-]{11})")
TS = re.compile(r"\{ts:(\d+(?:\.\d+)?)\}")
DATE_TAIL = re.compile(r"^\s+Date: \d{4}-\d{2}-\d{2}\s*$")


def perplexity_payloads(path: Path):
    """Yield the 'results' text of every perplexity_search tool result in a JSONL log."""
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if 'results' not in line or 'search results' not in line:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            for text in walk_strings(event):
                if text.startswith('{"results":"Found') or text.startswith('{"results": "Found'):
                    try:
                        yield json.loads(text)["results"]
                    except (json.JSONDecodeError, KeyError):
                        continue


def walk_strings(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for value in node.values():
            yield from walk_strings(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk_strings(value)


def split_results(payload: str):
    """Yield (title, url, transcript_text) for each search result."""
    current = None
    for line in payload.splitlines():
        head = RESULT_HEAD.match(line)
        if head:
            if current:
                yield current
            current = {"title": head.group(1), "url": "", "lines": [], "in_transcript": False, "meta": []}
            continue
        if current is None:
            continue
        url = URL.match(line)
        if url and not current["url"]:
            current["url"] = url.group(1)
            continue
        if line.strip() == "### Transcript":
            current["in_transcript"] = True
            continue
        if DATE_TAIL.match(line):
            current["meta"].append(line.strip())
            continue
        if current["in_transcript"]:
            current["lines"].append(line)
        else:
            current["meta"].append(line.strip())
    if current:
        yield current


def windows(lines: list[str]) -> list[str]:
    """Split transcript lines into contiguous windows at '...' / '…' separator lines."""
    out, buf = [], []
    for line in lines:
        if line.strip() in {"...", "…"}:
            if buf:
                out.append("\n".join(buf).strip())
            buf = []
        else:
            buf.append(line.rstrip())
    if buf:
        out.append("\n".join(buf).strip())
    return [w for w in out if w]


def flat(text: str) -> str:
    return " ".join(TS.sub(" ", text).split())


def first_ts(window: str) -> float:
    m = TS.search(window)
    return float(m.group(1)) if m else -1.0


def main(paths: list[str]) -> int:
    per_video: dict[str, dict] = defaultdict(lambda: {"titles": set(), "meta": set(), "windows": set()})
    payloads = 0
    for p in paths:
        for payload in perplexity_payloads(Path(p)):
            payloads += 1
            for result in split_results(payload):
                m = VIDEO_ID.search(result["url"])
                if not m or "youtube.com" not in result["url"] and "youtu.be" not in result["url"]:
                    continue
                vid = m.group(1)
                entry = per_video[vid]
                entry["titles"].add(result["title"])
                entry["meta"].update(x for x in result["meta"] if x and len(x) < 300)
                for w in windows(result["lines"]):
                    entry["windows"].add(w)
    OUT.mkdir(parents=True, exist_ok=True)
    total_windows = 0
    for vid, entry in sorted(per_video.items()):
        ws = sorted(entry["windows"], key=lambda w: (first_ts(w), -len(w)))
        flats = [flat(w) for w in ws]
        keep = []
        for i, w in enumerate(ws):
            fi = flats[i]
            if any(i != j and fi in flats[j] and (len(flats[j]) > len(fi) or j < i) for j in range(len(ws))):
                continue
            keep.append(w)
        total_windows += len(keep)
        stamps = [first_ts(w) for w in keep if first_ts(w) >= 0]
        header = [f"# {sorted(entry['titles'])[0]}", "",
                  f"- URL: https://www.youtube.com/watch?v={vid}",
                  f"- Windows: {len(keep)} (first timestamps {min(stamps, default=0):.0f}s … {max(stamps, default=0):.0f}s)",
                  "- Source: verbatim Perplexity search results (YouTube auto-captions), machine-extracted from agent logs",
                  "", "Metadata lines seen:", *[f"  {m}" for m in sorted(entry["meta"])[:12]], "", "---", ""]
        (OUT / f"{vid}.md").write_text("\n".join(header) + "\n\n[…]\n\n".join(keep) + "\n", encoding="utf-8")
    print(f"{payloads} search payloads → {len(per_video)} videos, {total_windows} windows → {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

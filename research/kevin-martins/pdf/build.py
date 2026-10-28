#!/usr/bin/env python3
"""Build the Kevin Martins / FSC report PDF.

  python3 research/kevin-martins/pdf/build.py

Sections come from sections/NN-*.md (Markdown with a small front-matter block).

Prompt cards come from prompts.json and are never retyped:
  - "spoken" cards cut the prompt out of the machine-extracted caption corpus (corpus/<videoId>.md),
    from an exact start phrase through an exact end phrase, inside ONE contiguous caption window
    (windows are separated by "[…]"), so a quote can't silently span a gap. The timestamp printed is
    the caption marker at or before the quote.
  - "doc" cards print a Google Doc's plain-text export (raw/doc-<fileId>.txt) in full.
The build stops if any phrase can't be found exactly.

Inline quotes in sections can be verified the same way with {{q:VIDEO|start|end}}, which renders the
exact caption text plus a timestamp link.
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CORPUS = ROOT / "corpus"
RAW = ROOT / "raw"
OUT_HTML = HERE / "report.html"
OUT_PDF = ROOT / "Kevin-Martins-FSC-AI-Video-Workflow.pdf"
TS = re.compile(r"\{ts:(\d+(?:\.\d+)?)\}")
GAP = "\n[…]\n"
DOC_RE = re.compile(r"\{\{d:([\w-]+)\|(.+?)\}\}")
QUOTE_RE = re.compile(r"\{\{q:([\w-]{11})\|(.+?)\|(.+?)\}\}")
_windows: dict[str, list[str]] = {}


def clock(seconds: int) -> str:
    h, rest = divmod(int(seconds), 3600)
    return f"{h}:{rest // 60:02d}:{rest % 60:02d}" if h else f"{rest // 60}:{rest % 60:02d}"


def windows(video: str) -> list[str]:
    if video not in _windows:
        path = CORPUS / f"{video}.md"
        if not path.is_file():
            sys.exit(f"missing corpus file {path}")
        body = path.read_text(encoding="utf-8").split("\n---\n", 1)[1]
        _windows[video] = body.split(GAP)
    return _windows[video]


def tokens(window: str) -> list[tuple[str, int | None]]:
    """Words of a window, each with the caption timestamp in force at that word (None before the first)."""
    out, current = [], None
    for piece in re.split(r"(\{ts:\d+(?:\.\d+)?\})", window):
        m = TS.fullmatch(piece)
        if m:
            current = int(float(m.group(1)))
            continue
        out += [(word, current) for word in piece.split()]
    return out


QUOTES = "\"“”'‘’"


def norm(word: str) -> str:
    """Match words ignoring the caption's quotation marks around speech (the words themselves must match)."""
    return word.strip(QUOTES)


def cut(video: str, start: str, end: str) -> tuple[str, int, bool]:
    """Exact caption text from `start` through `end` inside one window, its timestamp, and whether that
    timestamp is exact (False = the quote begins before the window's first marker; the next marker is used).
    Quotation marks the captions put around the spoken prompt are dropped at its two ends only."""
    s_words, e_words = [norm(w) for w in start.split()], [norm(w) for w in end.split()]
    for window in windows(video):
        toks = tokens(window)
        words = [w for w, _ in toks]
        normed = [norm(w) for w in words]
        for i in range(len(words) - len(s_words) + 1):
            if normed[i:i + len(s_words)] != s_words:
                continue
            for j in range(i, len(words) - len(e_words) + 1):
                if normed[j:j + len(e_words)] == e_words:
                    quote = " ".join(words[i:j + len(e_words)]).lstrip(QUOTES).rstrip(QUOTES)
                    stamp = toks[i][1]
                    if stamp is not None:
                        return quote, stamp, True
                    later = next((t for _, t in toks[i:] if t is not None), 0)
                    return quote, later, False
    sys.exit(f"[{video}] not found inside one caption window: {start!r} … {end!r}")


def link(video: str, stamp: int, exact: bool) -> str:
    if not exact and stamp == 0:
        return f'<a href="https://www.youtube.com/watch?v={video}">time not in caption excerpt</a>'
    label = clock(stamp) if exact else f"just before {clock(stamp)}"
    return f'<a href="https://www.youtube.com/watch?v={video}&t={stamp}s">{label}</a>'


def doc_text(file_id: str) -> str:
    path = RAW / f"doc-{file_id}.txt"
    if not path.is_file():
        sys.exit(f"missing doc export {path}")
    lines = [line.rstrip() for line in path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").split("\n")]
    out: list[str] = []
    for line in lines:
        if not line.strip():
            if out and out[-1] == "":
                continue
            line = ""
        out.append(line.lstrip("\t") if line.startswith("\t") else line)
    return "\n".join(out).strip("\n")


def render_cards() -> dict[str, str]:
    cards = json.loads((HERE / "prompts.json").read_text(encoding="utf-8"))
    out = {}
    for c in cards:
        if c["kind"] == "doc":
            text = doc_text(c["file_id"])
            where = (f'Google Doc “{html.escape(c["doc_title"])}” · '
                     f'<a href="https://docs.google.com/document/d/{c["file_id"]}">open</a>')
            kind = "full document text, exported unchanged (empty lines collapsed)"
        else:
            text, stamp, exact = cut(c["video"], c["start"], c["end"])
            where = f'{html.escape(c["source_title"])} · {link(c["video"], stamp, exact)}'
            kind = "spoken; exact YouTube caption text"
        for key in ("when", "where", "what", "note", "speaker"):
            if c.get(key):
                c[key] = QUOTE_RE.sub(inline_quote, c[key])
        rows = "".join(
            f'<div class="pc-row"><span class="pc-k">{label}</span><span class="pc-v">{c[key]}</span></div>'
            for label, key in [("When", "when"), ("Where", "where"), ("What it does", "what")] if c.get(key))
        long = " long" if len(text) > 1600 else ""
        out[c["id"]] = f"""
<div class="prompt-card{long}" id="{c['id']}">
  <div class="pc-head"><span class="pc-id">{c['id']}</span><span class="pc-title">{html.escape(c['title'])}</span></div>
  {rows}
  <pre class="pc-text">{html.escape(text)}</pre>
  <div class="pc-proof"><b>Proof:</b> {c['speaker']} · {where} · <span class="pc-kind">{kind}</span></div>
  {f'<div class="pc-note">{c["note"]}</div>' if c.get("note") else ''}
</div>"""
    return out


def inline_quote(m: re.Match) -> str:
    video, start, end = m.group(1), m.group(2), m.group(3)
    text, stamp, exact = cut(video, start, end)
    return f'“{html.escape(text)}” <span class="src">({link(video, stamp, exact)})</span>'


def doc_quote(m: re.Match) -> str:
    file_id, phrase = m.group(1), m.group(2)
    if phrase not in " ".join(doc_text(file_id).split()):
        sys.exit(f"[doc {file_id}] phrase not found verbatim: {phrase!r}")
    return f"<code>{html.escape(phrase)}</code>"


def video_meta(video: str) -> tuple[str, str]:
    known = json.loads((HERE / "video_meta.json").read_text(encoding="utf-8"))
    if video in known:
        return known[video]["title"], known[video]["date"]
    head = (CORPUS / f"{video}.md").read_text(encoding="utf-8").split("\n---\n", 1)[0]
    title = head.splitlines()[0].lstrip("# ").strip()
    dates = re.findall(r"Date: (\d{4}-\d{2}-\d{2})", head)
    return title, (dates[0] if dates else "")


def sources_table(text: str) -> str:
    ids = sorted({m.group(1) for m in QUOTE_RE.finditer(text)}
                 | {c["video"] for c in json.loads((HERE / "prompts.json").read_text()) if c.get("video")})
    rows = sorted((video_meta(v)[1], video_meta(v)[0], v) for v in ids)
    lines = ["| Published | Video (Kevin Martins channels) | Link |", "|---|---|---|"]
    lines += [f"| {d or 'n/a'} | {t.replace('|', '/')} | [youtu.be/{v}](https://www.youtube.com/watch?v={v}) |" for d, t, v in rows]
    return f"<p class='src'>{len(rows)} videos are quoted in this report.</p>\n\n" + "\n".join(lines)


def build() -> None:
    cards = render_cards()
    all_text = "\n".join(p.read_text(encoding="utf-8") for p in (HERE / "sections").glob("*.md"))
    all_text += (HERE / "prompts.json").read_text(encoding="utf-8")
    used: set[str] = set()
    parts = []
    for path in sorted((HERE / "sections").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta, body = {}, text
        if text.startswith("---\n"):
            head, body = text[4:].split("\n---\n", 1)
            meta = dict(line.split(": ", 1) for line in head.splitlines() if ": " in line)

        def card(m: re.Match) -> str:
            if m.group(1) not in cards:
                sys.exit(f"unknown card {m.group(1)} in {path.name}")
            used.add(m.group(1))
            return cards[m.group(1)]

        body = re.sub(r"\{\{card:([\w-]+)\}\}", card, body)
        body = body.replace("{{sources}}", sources_table(all_text))
        body = body.replace("{{nquoted}}", str(len({m.group(1) for m in QUOTE_RE.finditer(all_text)}
                                                    | {c["video"] for c in json.loads((HERE / "prompts.json").read_text()) if c.get("video")})))
        body = QUOTE_RE.sub(inline_quote, body)
        body = DOC_RE.sub(doc_quote, body)
        rendered = markdown.markdown(body, extensions=["tables", "fenced_code", "attr_list", "md_in_html", "sane_lists"])
        header = ""
        if meta.get("number") or meta.get("title"):
            header = (f'<div class="sec-head"><div class="sec-num">{html.escape(meta.get("number", ""))}</div>'
                      f'<div><div class="sec-title">{html.escape(meta.get("title", ""))}</div>'
                      f'<div class="sec-sub">{html.escape(meta.get("subtitle", ""))}</div></div></div>')
        parts.append(f'<section class="{meta.get("class", "section")}">{header}{rendered}</section>')
    missing = set(cards) - used
    if missing:
        print(f"note: cards defined but not placed: {sorted(missing)}", file=sys.stderr)
    css = (HERE / "style.css").read_text(encoding="utf-8")
    OUT_HTML.write_text("<!doctype html><html><head><meta charset='utf-8'>"
                        "<title>Kevin Martins &amp; FSC: AI Video Workflow</title>"
                        f"<style>{css}</style></head><body>{''.join(parts)}</body></html>", encoding="utf-8")
    subprocess.run(["node", str(HERE / "render.js"), str(OUT_HTML), str(OUT_PDF)], check=True)
    info = subprocess.run(["pdfinfo", str(OUT_PDF)], capture_output=True, text=True).stdout
    pages = re.search(r"Pages:\s+(\d+)", info).group(1)
    print(f"wrote {OUT_PDF} ({pages} pages)")


if __name__ == "__main__":
    build()

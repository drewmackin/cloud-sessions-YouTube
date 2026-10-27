#!/usr/bin/env python3
"""Build the Kevin Martins / FSC report PDF.

  python3 research/kevin-martins/pdf/build.py

Sections come from sections/NN-*.md (Markdown with a small front-matter block). Prompt cards come from
prompts.json; each card's text is cut straight out of a raw transcript file (raw/<videoId>.md), between an
exact start phrase and end phrase, so the printed prompt is the source text and never retyped.
The build fails if a quoted phrase can't be found verbatim.
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
ROOT = HERE.parent  # research/kevin-martins
RAW = ROOT / "raw"
OUT_HTML = HERE / "report.html"
OUT_PDF = ROOT / "Kevin-Martins-FSC-AI-Video-Workflow.pdf"
TS = re.compile(r"\{ts:(\d+(?:\.\d+)?)\}")


def clock(seconds: float) -> str:
    s = int(seconds)
    h, rest = divmod(s, 3600)
    return f"{h}:{rest // 60:02d}:{rest % 60:02d}" if h else f"{rest // 60}:{rest % 60:02d}"


def raw_text(video: str) -> str:
    path = RAW / f"{video}.md"
    if not path.is_file():
        sys.exit(f"missing raw transcript {path}")
    return path.read_text(encoding="utf-8")


def flatten(text: str) -> str:
    """Caption text as one line: timestamp markers out, whitespace collapsed (words untouched)."""
    return " ".join(TS.sub(" ", text).split())


def cut(video: str, start: str, end: str) -> tuple[str, int]:
    """Return the verbatim caption text from `start` through `end`, and the timestamp nearest before it."""
    text = raw_text(video)
    flat = flatten(text)
    i = flat.find(start)
    if i < 0:
        sys.exit(f"[{video}] start phrase not found verbatim: {start!r}")
    j = flat.find(end, i)
    if j < 0:
        sys.exit(f"[{video}] end phrase not found verbatim after start: {end!r}")
    quote = flat[i:j + len(end)]
    pos = locate(text, start)
    stamp = 0
    for m in TS.finditer(text):
        if m.start() > pos:
            break
        stamp = int(float(m.group(1)))
    return quote, stamp


def locate(text: str, phrase: str) -> int:
    """Character offset in the original text where `phrase` (whitespace-insensitive) begins."""
    words = phrase.split()
    pattern = r"\s*(?:\{ts:\d+(?:\.\d+)?\}\s*)?".join(re.escape(w) for w in words)
    m = re.search(pattern, text)
    return m.start() if m else 0


def prompt_cards(only_section: str | None = None) -> dict[str, str]:
    cards = json.loads((HERE / "prompts.json").read_text(encoding="utf-8"))
    rendered: dict[str, str] = {}
    for card in cards:
        quote, stamp = cut(card["video"], card["start"], card["end"])
        url = f"https://www.youtube.com/watch?v={card['video']}&t={stamp}s"
        meta = "".join(
            f'<div class="pc-row"><span class="pc-k">{k}</span><span class="pc-v">{html.escape(card[key])}</span></div>'
            for k, key in [("When", "when"), ("Where", "where"), ("What it does", "what")] if card.get(key))
        rendered[card["id"]] = f"""
<div class="prompt-card" id="{card['id']}">
  <div class="pc-head"><span class="pc-id">{html.escape(card['id'])}</span><span class="pc-title">{html.escape(card['title'])}</span></div>
  {meta}
  <pre class="pc-text">{html.escape(quote)}</pre>
  <div class="pc-proof"><b>Proof:</b> {html.escape(card['speaker'])} · {html.escape(card['source_title'])} ·
    <a href="{url}">{clock(stamp)}</a> · <span class="pc-kind">{html.escape(card.get('kind', 'spoken, verbatim from auto-captions'))}</span></div>
  {f'<div class="pc-note">{html.escape(card["note"])}</div>' if card.get("note") else ''}
</div>"""
    return rendered


def build() -> None:
    cards = prompt_cards()
    parts = []
    for path in sorted((HERE / "sections").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta, body = {}, text
        if text.startswith("---\n"):
            head, body = text[4:].split("\n---\n", 1)
            meta = dict(line.split(": ", 1) for line in head.splitlines() if ": " in line)
        body = re.sub(r"\{\{card:([\w-]+)\}\}", lambda m: cards[m.group(1)] if m.group(1) in cards
                      else sys.exit(f"unknown card {m.group(1)} in {path.name}"), body)
        body = re.sub(r"\{\{cards:all\}\}", lambda m: "\n".join(cards.values()), body)
        rendered = markdown.markdown(body, extensions=["tables", "fenced_code", "attr_list", "md_in_html", "sane_lists"])
        cls = meta.get("class", "section")
        number = meta.get("number", "")
        title = meta.get("title", "")
        header = ""
        if number or title:
            header = (f'<div class="sec-head"><div class="sec-num">{html.escape(number)}</div>'
                      f'<div><div class="sec-title">{html.escape(title)}</div>'
                      f'<div class="sec-sub">{html.escape(meta.get("subtitle", ""))}</div></div></div>')
        parts.append(f'<section class="{cls}">{header}{rendered}</section>')
    css = (HERE / "style.css").read_text(encoding="utf-8")
    OUT_HTML.write_text(f"<!doctype html><html><head><meta charset='utf-8'><title>Kevin Martins & FSC: AI Video Workflow</title>"
                        f"<style>{css}</style></head><body>{''.join(parts)}</body></html>", encoding="utf-8")
    script = HERE / "render.js"
    subprocess.run(["node", str(script), str(OUT_HTML), str(OUT_PDF)], check=True)
    pages = subprocess.run(["pdfinfo", str(OUT_PDF)], capture_output=True, text=True).stdout
    print(f"wrote {OUT_PDF} ({re.search(r'Pages:\s+(\d+)', pages).group(1)} pages)")


if __name__ == "__main__":
    build()

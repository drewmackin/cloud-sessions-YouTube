#!/usr/bin/env python3
"""List every {{q:…}} quote in the sections and prompt cards that can't be cut exactly, with nearby caption text."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

HERE = Path(__file__).resolve().parent
texts = [(p.name, p.read_text(encoding="utf-8")) for p in sorted((HERE / "sections").glob("*.md"))]
texts.append(("prompts.json", json.dumps(json.loads((HERE / "prompts.json").read_text()), ensure_ascii=False)))
bad = ok = 0
for name, text in texts:
    for m in build.QUOTE_RE.finditer(text):
        video, start, end = m.groups()
        try:
            build.cut(video, start, end)
            ok += 1
        except SystemExit:
            bad += 1
            print(f"\n✗ {name}: {video} | {start} | {end}")
            key = [build.norm(w) for w in start.split()[:3]]
            for w in build.windows(video):
                words = [build.norm(x) for x, _ in build.tokens(w)]
                for i in range(len(words)):
                    if words[i:i + len(key)] == key:
                        print("   …", " ".join(x for x, _ in build.tokens(w)[i:i + 45]))
                        break
    for m in build.WEB_RE.finditer(text):
        try:
            build.cut_web(*m.groups())
            ok += 1
        except SystemExit:
            bad += 1
            print(f"\n✗ {name}: web {m.group(1)} | {m.group(2)} | {m.group(3)}")
    for m in build.META_RE.finditer(text):
        try:
            build.meta_check(*m.groups())
            ok += 1
        except SystemExit:
            bad += 1
            print(f"\n✗ {name}: meta {m.group(1)} | {m.group(2)}")
print(f"\n{ok} ok, {bad} failing")

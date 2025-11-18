#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

base = os.path.dirname(os.path.abspath(__file__))
js_path = os.path.join(base, "wabi.ai", "_next", "static", "chunks", "app", "page-e7f18f5caa462839.js")

with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

needle = "加入候补"
positions = []
start = 0
while True:
    idx = content.find(needle, start)
    if idx == -1:
        break
    positions.append(idx)
    start = idx + len(needle)

out_path = os.path.join(base, "join_button_snippet.txt")
with open(out_path, "w", encoding="utf-8") as out:
    out.write("positions: " + ",".join(map(str, positions)) + "\n\n")
    for pos in positions:
        s = max(0, pos - 260)
        e = min(len(content), pos + 260)
        out.write(f"POS {pos}\n")
        out.write(content[s:e])
        out.write("\n\n")

print(f"Wrote snippets to {out_path}")


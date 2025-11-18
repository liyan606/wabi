#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

base = os.path.dirname(os.path.abspath(__file__))
js_path = os.path.join(base, "wabi.ai", "_next", "static", "chunks", "app", "page-e7f18f5caa462839.js")

with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

needle = 'href:"#waitlist"'
pos = content.find(needle)

out_path = os.path.join(base, "waitlist_snippet.txt")
with open(out_path, "w", encoding="utf-8") as out:
    out.write(f"pos {pos}\n")
    if pos != -1:
        start = max(0, pos - 260)
        end = min(len(content), pos + 260)
        out.write(content[start:end])

print(f"Wrote snippet to {out_path}")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

base = os.path.dirname(os.path.abspath(__file__))
js_path = os.path.join(base, "wabi.ai", "_next", "static", "chunks", "app", "page-e7f18f5caa462839.js")

with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

out_path = os.path.join(base, "footer_js_snippet.txt")
with open(out_path, "w", encoding="utf-8") as out:
    for needle in ["服务条款", "隐私", "manifesto/footer/logo.svg", "Wabi on X", "https://x.com/wabi"]:
        pos = content.find(needle)
        out.write(f"=== {needle} pos {pos}\\n")
        if pos == -1:
            continue
        start = max(0, pos - 260)
        end = min(len(content), pos + 260)
        out.write(content[start:end])
        out.write("\\n\\n")

print(f"Wrote JS snippets to {out_path}")


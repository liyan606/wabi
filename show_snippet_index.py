#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

base = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base, "wabi.ai", "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

target = "这就是我们"
pos = content.find(target)
if pos == -1:
    print("target not found")
else:
    start = max(0, pos - 120)
    end = min(len(content), pos + 120)
    snippet = content[start:end]
    print(snippet)


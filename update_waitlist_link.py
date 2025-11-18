#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

base = os.path.dirname(os.path.abspath(__file__))
js_path = os.path.join(base, "wabi.ai", "_next", "static", "chunks", "app", "page-e7f18f5caa462839.js")

OLD = 'href:"#waitlist"'
NEW = 'href:"https://uwnf572od4k.feishu.cn/wiki/BJ0Uwmp8fiyNnPkLwwzcNG1Fnrh?from=from_copylink"'

with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

if OLD not in content:
    raise SystemExit("OLD pattern not found in JS bundle")

content = content.replace(OLD, NEW)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated waitlist link in", js_path)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

work_dir = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(work_dir, "wabi.ai", "index.html")

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

quoted_chinese = re.findall(r'["\']([^"\']*[\u4e00-\u9fa5]+[^"\']*)["\']', content)
direct_chinese = re.findall(r'[\u4e00-\u9fa5]+[^\u4e00-\u9fa5\s]*[\u4e00-\u9fa5]*', content)

all_texts = set()
for text in quoted_chinese + direct_chinese:
    if text and re.search(r'[\u4e00-\u9fa5]', text):
        all_texts.add(text)

unique_texts = sorted(all_texts, key=lambda x: (-len(x), x))

out_file = os.path.join(work_dir, "chinese_texts_index.txt")
with open(out_file, "w", encoding="utf-8") as f:
    f.write(f"index.html 中共找到 {len(unique_texts)} 条中文文本：\n\n")
    for i, text in enumerate(unique_texts, 1):
        f.write(f"{i}. {text}\n")

print(f"Wrote {len(unique_texts)} entries to {out_file}")

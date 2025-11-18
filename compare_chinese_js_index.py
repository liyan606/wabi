#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

base = os.path.dirname(os.path.abspath(__file__))

js_file = os.path.join(base, "chinese_texts.txt")
idx_file = os.path.join(base, "chinese_texts_index.txt")

def load_texts(path):
    texts = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0].isdigit() and ". " in line:
                # strip leading index like "123. "
                _, text = line.split(". ", 1)
                texts.append(text)
    return texts

js_texts = load_texts(js_file)
idx_texts = load_texts(idx_file)

js_set = set(js_texts)
idx_set = set(idx_texts)

only_in_idx = sorted(idx_set - js_set, key=lambda x: (-len(x), x))
only_in_js = sorted(js_set - idx_set, key=lambda x: (-len(x), x)) if js_set else []

base_out = os.path.join(base, "diff_chinese")
os.makedirs(base_out, exist_ok=True)

idx_out = os.path.join(base_out, "only_in_index.txt")
js_out = os.path.join(base_out, "only_in_js.txt")

with open(idx_out, "w", encoding="utf-8") as f:
    f.write("index.html 中有，但 JS 中没有的文本：\n\n")
    for t in only_in_idx:
        f.write(f"- {t}\n")

with open(js_out, "w", encoding="utf-8") as f:
    f.write("JS 中有，但 index.html 中没有的文本：\n\n")
    for t in only_in_js:
        f.write(f"- {t}\n")

print(f"Wrote {len(only_in_idx)} items to {idx_out}")
print(f"Wrote {len(only_in_js)} items to {js_out}")

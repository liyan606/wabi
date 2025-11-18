#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

# 获取当前工作目录
work_dir = os.path.dirname(os.path.abspath(__file__))
js_file = os.path.join(work_dir, 'wabi.ai', '_next', 'static', 'chunks', 'app', 'page-e7f18f5caa462839.js')

# 读取 JS 文件
with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取所有中文文本
# 方法1: 提取引号内的中文文本
quoted_chinese = re.findall(r'["\']([^"\']*[\u4e00-\u9fa5]+[^"\']*)["\']', content)

# 方法2: 提取直接出现的中文字符串
direct_chinese = re.findall(r'[\u4e00-\u9fa5]+[^\u4e00-\u9fa5\s]*[\u4e00-\u9fa5]*', content)

# 合并并去重
all_texts = set()
for text in quoted_chinese + direct_chinese:
    if text and re.search(r'[\u4e00-\u9fa5]', text):
        all_texts.add(text)

# 转换为列表并按长度排序
unique_texts = sorted(all_texts, key=lambda x: (-len(x), x))

print("=" * 80)
print(f"共找到 {len(unique_texts)} 条中文文本：")
print("=" * 80)
print()

for i, text in enumerate(unique_texts, 1):
    print(f"{i:3d}. {text}")

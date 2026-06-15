#!/usr/bin/env python3
# rewrite_belief.py - 将 belief.html 改为引用 dialogeu.css 的浅色版本

import re, sys

path = r"D:\temp_website\deepsuodao.github.io\belief.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 替换 head 中的 style 块为 link 引用
old_head = content[:content.find('</head>')]
# 删除整个 <style>...</style> 块
new_head = re.sub(r'<style>.*?</style>', '', old_head, flags=re.DOTALL)
# 在 <meta description> 后添加 link
new_head = new_head.replace(
    '<meta name="description" content="信心是复利不中断的核动力。本文系统阐述家庭财富管理的三大机制：保障金机制、复利机制、底线机制。">',
    '<meta name="description" content="信心是复利不中断的核动力。本文系统阐述家庭财富管理的三大机制：保障金机制、复利机制、底线机制。">\n<link rel="stylesheet" href="dialogeu.css">'
)
content = new_head + content[content.find('</head>'):]

# 2. 替换 class 名称（深色版 → 浅色版，对应 dialogeu.css 中已有的或新增的 belief-* 样式）
replacements = [
    # 布局容器
    ('class="hero"', 'class="belief-hero"'),
    ('class="article"', 'class="belief-article"'),
    # 场景块
    ('class="scene"', 'class="belief-scene"'),   # 会用 .belief-article .belief-scene 样式
    ('class="scene-title"', 'class="belief-scene-title"'),
    # 对话块
    ('class="dialogeu"', 'class="belief-dlg"'),
    ('class="speaker shendao"', 'class="belief-sp belief-sp-a"'),
    ('class="speaker gelinge"', 'class="belief-sp belief-sp-c"'),
    ('class="speaker andelu"', 'class="belief-sp belief-sp-b"'),
    ('class="line"', 'class="belief-ln"'),
    # 高亮盒子
    ('class="hl-box"', 'class="belief-hl"'),
    # 引用块
    ('<blockquote>', '<blockquote class="belief-golden">'),
    # 金字塔
    ('class="pyramid"', 'class="belief-pyramid"'),
    ('class="pyr-row"', 'class="belief-pyr-row"'),
    # 表格
    ('class="table-wrap"', 'class="belief-table-wrap"'),
    ('<table>', '<table class="summary-table">'),
    # 附录
    ('class="appendix"', 'class="belief-appendix"'),
    ('class="checklist"', 'class="belief-checklist"'),
]

for old, new in replacements:
    content = content.replace(old, new)

# 3. 删除所有内联 style= 属性（它们会覆盖 CSS，且是深色值）
# 先处理 style="color:#f0c868" 等（这些是金色高亮，改用 CSS class）
# 把这些内联样式替换为对应的 class
content = re.sub(r'style="color:#f0c868;font-weight:500;margin-bottom:8px">', 'class="belief-hl-label">', content)
content = re.sub(r'style="color:#f0c868">([^<]*)</strong>', r'<strong class="highlight-accent">\1</strong>', content)
content = re.sub(r'style="color:#e8e6e3">([^<]*)</strong>', r'<strong class="highlight-primary">\1</strong>', content)
# 删除残留的 style 属性
content = re.sub(r'\s+style="[^"]*"', '', content)

# 4. 在 </head> 前添加 viewport 的闭合（已处理）

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done. belief.html rewritten to use dialogeu.css.")

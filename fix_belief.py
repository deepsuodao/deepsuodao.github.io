#!/usr/bin/env python3
path = r"D:\temp_website\deepsuodao.github.io\belief.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 批量替换
replacements = [
    ('class="dialogue"', 'class="dlg"'),
    ('class="belief-scene"', 'class="scene"'),           # 统一用 dialogue.css 已有的 .scene
    ('class="belief-scene-title"', 'class="section-title"'),  # 统一用 dialogue.css 已有的 .section-title
    ('class="belief-ln"', 'class="line"'),
    ('class="belief-sp belief-sp-a"', 'class="speaker speaker-a"'),
    ('class="belief-sp belief-sp-b"', 'class="speaker speaker-b"'),
    ('class="belief-sp belief-sp-c"', 'class="speaker speaker-c"'),
    ('class="belief-hl"', 'class="hl-box"'),
    ('class="belief-pyramid"', 'class="pyramid"'),
    ('class="belief-pyr-row"', 'class="pyr-row"'),
    ('class="belief-appendix"', 'class="appendix"'),
    ('class="belief-checklist"', 'class="checklist"'),
    ('class="belief-golden"', 'class="golden"'),
    ('class="belief-table-wrap"', 'class="table-wrap"'),
]

for old, new in replacements:
    count = content.count(old)
    if count:
        print(f"  {count}× {old} -> {new}")
        content = content.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done.")

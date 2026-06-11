#!/usr/bin/env python3
"""Batch edit dialogue-*.html and principles.html:
1. max-width:900px -> max-width:1100px (only .container and .section-img.wide)
2. Insert back-to-top CSS before </style>
3. Insert back-to-top HTML before </footer>
"""

import os
import re
import glob

PROJECT = r"D:\temp_website\deepsuodao.github.io"

# Collect target files (exclude _bak)
files = (
    glob.glob(os.path.join(PROJECT, "dialogue-*.html"))
    + glob.glob(os.path.join(PROJECT, "principles.html"))
)
files = sorted(f for f in files if "_bak" not in os.path.basename(f))

print(f"Found {len(files)} target files to process (excluding _bak).")
for f in files:
    print(f"  {os.path.basename(f)}")

BACK_TO_TOP_CSS = """/* === Back to Top === */
.back-to-top{position:fixed;bottom:32px;right:32px;width:44px;height:44px;border-radius:50%;background:rgba(212,168,83,.1);border:1px solid rgba(212,168,83,.2);color:#d4a853;font-size:1.2rem;cursor:pointer;transition:all .3s;z-index:999;display:flex;align-items:center;justify-content:center;text-decoration:none;backdrop-filter:blur(4px)}
.back-to-top:hover{background:rgba(212,168,83,.2);border-color:rgba(212,168,83,.4)}
"""

BACK_TO_TOP_HTML = """<a href="#" class="back-to-top" aria-label="\u56de\u5230\u9876\u90e8">\u2191</a>"""

modified_count = 0

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Replace max-width:900px -> max-width:1100px
    #    Only replace .container{max-width:900px and .section-img.wide{max-width:900px
    content = content.replace(
        ".container{max-width:900px", ".container{max-width:1100px"
    )
    content = content.replace(
        ".section-img.wide{max-width:900px", ".section-img.wide{max-width:1100px"
    )

    # 2. Insert back-to-top CSS before </style>
    if "back-to-top" not in content:
        content = content.replace("</style>", BACK_TO_TOP_CSS + "\n</style>")

    # 3. Insert back-to-top HTML before </footer>
    if "back-to-top" not in content.split("</style>")[-1]:  # check in body only roughly
        pass
    # Simple: insert before </footer>
    content = content.replace("</footer>", BACK_TO_TOP_HTML + "\n</footer>")

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1
        print(f"  [MODIFIED] {os.path.basename(filepath)}")
    else:
        print(f"  [SKIPPED]  {os.path.basename(filepath)} (no changes)")

print(f"\nDone. Total files modified: {modified_count}")

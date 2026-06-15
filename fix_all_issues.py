#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix P2, P4, P7:
   - P4: Remove <style> block from index.html (styles now in index.css)
   - P2: Unify headers to use semantic <header> with CSS classes
   - P7: Fix form error handling in principles.html
"""

def fix_index_html():
    filepath = 'D:/temp_website/deepsuodao.github.io/index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # P4: Remove the entire <style> block (lines 19-230 approximately)
    # Find <style> and </style> tags
    style_start = content.find('<style>')
    style_end = content.find('</style>', style_start)
    
    if style_start != -1 and style_end != -1:
        # Remove from <style> to </style> (inclusive)
        content = content[:style_start] + content[style_end + len('</style>'):]
        print(f'  Removed <style> block (chars {style_start} to {style_end + len("</style>")})')
    else:
        print('  WARNING: <style> block not found in index.html')
    
    # Fix the JS script: it was inside the <style> block, need to re-add it
    # Find </head> and add the JS before it
    head_end = content.find('</head>')
    if head_end != -1:
        js_script = """
  <script>
    // IntersectionObserver for scroll-fade animations
    document.addEventListener('DOMContentLoaded', () => {
      const fadeEls = document.querySelectorAll('.scroll-fade, .reveal-text');
      if (!fadeEls.length) return;
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.15 });
      fadeEls.forEach(el => observer.observe(el));
    });
  </script>
""" + '  </head>'
        content = content[:head_end] + js_script + content[head_end + len('</head>'):]
        print('  Added scroll animation JS before </head>')
    
    # P2: Update header to use header-dark class (since hero is now dark)
    # Find the header tag and update it
    old_header_start = content.find('<header>')
    if old_header_start != -1:
        # Find the end of the opening <header> tag
        header_tag_end = content.find('>', old_header_start)
        if header_tag_end != -1:
            content = content[:old_header_start] + '<header class="header-dark">' + content[header_tag_end + 1:]
            print('  Updated index.html header to use header-dark class')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('  index.html updated successfully')

def fix_principles_html():
    filepath = 'D:/temp_website/deepsuodao.github.io/principles.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # P2: Replace inline-style header with semantic <header class="header-dark">
    old_header = '<header style="position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(11,13,16,0.92);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid rgba(212,175,55,0.08);">'
    new_header = '<header class="header-dark">'
    
    if old_header in content:
        content = content.replace(old_header, new_header, 1)
        print('  Replaced principles.html header with semantic <header class="header-dark">')
    else:
        print('  WARNING: Old header style not found in principles.html')
    
    # Also fix the inner div (remove inline styles)
    old_inner = '  <div style="max-width:1100px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:60px;">'
    new_inner = '  <div class="container">'
    
    # Find the line after <header class="header-dark"> and replace the inner div
    header_pos = content.find('<header class="header-dark">')
    if header_pos != -1:
        next_div = content.find('<div', header_pos)
        if next_div != -1:
            div_end = content.find('>', next_div)
            if div_end != -1:
                old_inner_actual = content[next_div:div_end + 1]
                content = content[:next_div] + new_inner[:-1] + content[div_end + 1:]
                # Now fix the closing </div> - it should be </div></header> structure
                # Actually, let me just replace the whole header block more carefully
    
    # Let me redo this more carefully - replace the entire header block
    # Find the header block (from <header ...> to </header>)
    header_start = content.find('<header')
    if header_start != -1:
        header_end = content.find('</header>', header_start)
        if header_end != -1:
            # Build new header
            new_header_block = """<header class="header-dark">
  <div class="container">
    <div class="logo">私家<span>智囊</span></div>
    <nav>
      <a href="./index.html">首页</a>
      <a href="./principles.html" style="color:#D4AF37;">原则</a>
      <a href="./index.html#tools">工具箱</a>
    </nav>
  </div>
</header>"""
            content = content[:header_start] + new_header_block + content[header_end + len('</header>'):]
            print('  Replaced entire header block in principles.html')
    
    # P7: Fix form error handling
    # Find the handleSubmit function and fix it
    old_onsubmit = 'onsubmit="return handleSubmit(event)"'
    new_onsubmit = 'onsubmit="handleSubmit(event); return false;"'
    content = content.replace(old_onsubmit, new_onsubmit)
    
    # Add proper error handling JS for the form
    # Find the form-feedback paragraph and add JS after it
    form_js = """
  <script>
    function handleSubmit(event) {
      event.preventDefault();
      const form = event.target;
      const formData = new FormData(form);
      const action = form.action;
      
      // Show loading state
      const btn = form.querySelector('button[type="submit"]');
      const originalText = btn.textContent;
      btn.textContent = '提交中...';
      btn.disabled = true;
      
      fetch(action, {
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json'
        }
      })
      .then(response => {
        if (response.ok) {
          document.getElementById('form-feedback').style.display = 'block';
          form.reset();
        } else {
          throw new Error('提交失败，请稍后重试');
        }
      })
      .catch(error => {
        document.getElementById('form-feedback').style.display = 'block';
        document.getElementById('form-feedback').style.color = '#c97a7a';
        document.getElementById('form-feedback').textContent = '提交失败：' + error.message + '。请直接联系我们。';
      })
      .finally(() => {
        btn.textContent = originalText;
        btn.disabled = false;
      });
    }
  </script>
"""
    
    # Add the JS before </body>
    body_end = content.find('</body>')
    if body_end != -1:
        content = content[:body_end] + form_js + content[body_end:]
        print('  Added proper form error handling JS to principles.html')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('  principles.html updated successfully')

if __name__ == '__main__':
    print('=== Fixing index.html ===')
    fix_index_html()
    print()
    print('=== Fixing principles.html ===')
    fix_principles_html()
    print()
    print('All fixes applied successfully!')

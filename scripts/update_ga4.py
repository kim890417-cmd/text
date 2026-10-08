import os
import glob
import re

GA4_SNIPPET = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CQQNZC7MSQ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-CQQNZC7MSQ');
</script>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Remove old sitekit gtag block if present
    # Pattern to match old Site Kit comments and the two script tags
    old_sitekit_pattern = re.compile(
        r'(<!--\s*Site Kit[^\n]*-->\s*)*'
        r'<script\s+id=[\'"]google_gtagjs-js[\'"][^>]*>.*?</script>\s*'
        r'<script\s+id=[\'"]google_gtagjs-js-after[\'"][^>]*>.*?</script>',
        re.DOTALL | re.IGNORECASE
    )

    if old_sitekit_pattern.search(content):
        content = old_sitekit_pattern.sub(GA4_SNIPPET, content, count=1)
    elif 'G-CQQNZC7MSQ' not in content:
        # If no old gtag block, insert right after <head> or <head ...>
        head_pattern = re.compile(r'(<head[^>]*>)', re.IGNORECASE)
        if head_pattern.search(content):
            content = head_pattern.sub(r'\1\n' + GA4_SNIPPET, content, count=1)
        else:
            print(f"Warning: No <head> found in {filepath}")

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    html_files = glob.glob('**/*.html', recursive=True)
    updated = 0
    total = len(html_files)

    for f in html_files:
        if process_file(f):
            updated += 1

    print(f"Total HTML files: {total}")
    print(f"Updated files: {updated}")

    # Verification: check all files for G-CQQNZC7MSQ and for old GT-P8VJJSFD
    has_ga4 = 0
    has_old = 0
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
            if 'G-CQQNZC7MSQ' in c:
                has_ga4 += 1
            if 'GT-P8VJJSFD' in c:
                has_old += 1

    print(f"Files with new GA4 (G-CQQNZC7MSQ): {has_ga4}/{total}")
    print(f"Files with old tag (GT-P8VJJSFD): {has_old}/{total}")

if __name__ == '__main__':
    main()

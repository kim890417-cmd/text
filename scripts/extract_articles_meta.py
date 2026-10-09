import glob
import os
import re
import json

articles = glob.glob('health/*/index.html')
data = []
for a in sorted(articles):
    slug = os.path.basename(os.path.dirname(a))
    with open(a, 'r', encoding='utf-8') as f:
        html = f.read()
    tm = re.search(r'<title>(.*?)</title>', html, re.I)
    title = tm.group(1).split('|')[0].strip() if tm else slug
    dm = re.search(r'<meta\s+name=[\'"]description[\'"]\s+content=[\'"](.*?)[\'"]', html, re.I)
    desc = dm.group(1).strip() if dm else ''
    
    # find unsplash image if exists
    m = re.findall(r'https://images\.unsplash\.com/[^\s\'\"<>]+', html)
    img = m[0] if m else ''
    data.append({'slug': slug, 'title': title, 'desc': desc, 'img': img})

with open('scripts/articles_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Saved {len(data)} articles metadata to scripts/articles_metadata.json")

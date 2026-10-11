import os, re
from pathlib import Path

repo = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")
posts = [p for p in (repo / "health").iterdir() if p.is_dir()]
print(f"Total health post directories: {len(posts)}")

canonical_mismatches = []
noindex_found = []
jsonld_mismatches = []
title_empty = []
redirect_dirs = []

for p in posts:
    idx = p / "index.html"
    if not idx.exists():
        continue
    content = idx.read_text(encoding="utf-8")
    
    # Check if this is a redirect stub
    if "meta http-equiv=\"refresh\"" in content.lower():
        redirect_dirs.append(p.name)
        continue
        
    # Check title
    title_match = re.search(r"<title>(.*?)</title>", content)
    title = title_match.group(1).strip() if title_match else ""
    if not title:
        title_empty.append(p.name)
        
    # Check canonical
    can_match = re.search(r'<link rel=[\'"]canonical[\'"] href=[\'"](.*?)[\'"]', content)
    can = can_match.group(1).strip() if can_match else ""
    if p.name not in can:
        canonical_mismatches.append((p.name, can))
        
    # Check robots
    rob_match = re.search(r'<meta name=[\'"]robots[\'"] content=[\'"](.*?)[\'"]', content)
    rob = rob_match.group(1).lower() if rob_match else ""
    if "noindex" in rob:
        noindex_found.append((p.name, rob))
        
    # Check jsonld BlogPosting headline vs title
    # e.g., if headline doesn't match roughly
    jp_match = re.search(r'"@type":"BlogPosting",.*?"headline":"(.*?)"', content)
    if jp_match:
        headline = jp_match.group(1)
        # unescape unicode
        try:
            headline_decoded = headline.encode().decode('unicode-escape')
        except Exception:
            headline_decoded = headline
        # compare with title
        clean_title = title.split("|")[0].strip()
        if headline_decoded not in clean_title and clean_title not in headline_decoded:
            jsonld_mismatches.append((p.name, headline_decoded, clean_title))

print(f"Redirect stubs count: {len(redirect_dirs)}")
print(f"Canonical mismatches: {len(canonical_mismatches)}")
for item in canonical_mismatches[:5]:
    print("  Canonical mismatch:", item)
print(f"Noindex found: {len(noindex_found)}")
print(f"JSON-LD mismatches: {len(jsonld_mismatches)}")
for item in jsonld_mismatches[:5]:
    print("  JSON-LD mismatch:", item[0], "headline:", item[1][:30], "vs title:", item[2][:30])

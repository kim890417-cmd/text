import os
import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

results = []

# 1. Scan all html files in health/
health_dir = REPO_DIR / "health"
posts = []
for p in health_dir.rglob("index.html"):
    content = p.read_text(encoding="utf-8-sig", errors="ignore")
    # extract body text
    # remove scripts and styles
    clean_text = re.sub(r'<script[\s\S]*?</script>', '', content, flags=re.IGNORECASE)
    clean_text = re.sub(r'<style[\s\S]*?</style>', '', clean_text, flags=re.IGNORECASE)
    clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    char_count = len(clean_text)
    has_adsense = "ca-pub-3406696816625207" in content
    has_canonical = "canonical" in content
    has_img = "<img " in content
    
    rel_path = p.relative_to(REPO_DIR).as_posix()
    posts.append({
        "path": rel_path,
        "chars": char_count,
        "adsense": has_adsense,
        "canonical": has_canonical,
        "img": has_img
    })

posts.sort(key=lambda x: x["chars"])

print(f"Total health posts scanned: {len(posts)}")
print("--- Shortest 10 posts ---")
for post in posts[:10]:
    print(f"{post['chars']} chars | img:{post['img']} | ads:{post['adsense']} | {post['path']}")

print("\n--- Longest 5 posts ---")
for post in posts[-5:]:
    print(f"{post['chars']} chars | img:{post['img']} | ads:{post['adsense']} | {post['path']}")

# 2. Scan static pages: index.html, blog.html, bmi, calorie, etc.
static_pages = list(REPO_DIR.glob("*.html"))
print("\n--- Root static pages ---")
for sp in static_pages:
    content = sp.read_text(encoding="utf-8-sig", errors="ignore")
    clean_text = re.sub(r'<script[\s\S]*?</script>', '', content, flags=re.IGNORECASE)
    clean_text = re.sub(r'<style[\s\S]*?</style>', '', clean_text, flags=re.IGNORECASE)
    clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    has_adsense = "ca-pub-3406696816625207" in content
    print(f"{sp.name}: {len(clean_text)} chars | adsense:{has_adsense}")

# 3. Check subdirectory pages like bmi/index.html, etc.
other_html = [p for p in REPO_DIR.rglob("*.html") if not p.as_posix().startswith((REPO_DIR / "health").as_posix()) and p.parent != REPO_DIR]
print("\n--- Other subdirectory HTML files ---")
for op in other_html:
    rel = op.relative_to(REPO_DIR).as_posix()
    content = op.read_text(encoding="utf-8-sig", errors="ignore")
    clean_text = re.sub(r'<script[\s\S]*?</script>', '', content, flags=re.IGNORECASE)
    clean_text = re.sub(r'<style[\s\S]*?</style>', '', clean_text, flags=re.IGNORECASE)
    clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    has_adsense = "ca-pub-3406696816625207" in content
    print(f"{rel}: {len(clean_text)} chars | adsense:{has_adsense}")

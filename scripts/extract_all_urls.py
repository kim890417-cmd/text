import os
import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Read all 40 health posts in order of publication from blog.html or rss.xml
rss_file = REPO_DIR / "rss.xml"
rss_content = rss_file.read_text(encoding="utf-8")

items = re.findall(r'<item>\s*<title>(.*?)</title>\s*<link>(.*?)</link>', rss_content, re.DOTALL)
print(f"Total articles found in RSS: {len(items)}")

with open("all_40_english_urls.txt", "w", encoding="utf-8") as f:
    for i, (title, link) in enumerate(items, 1):
        f.write(f"{i}. [{title.strip()}]\n{link.strip()}\n\n")

print("Generated all_40_english_urls.txt successfully!")

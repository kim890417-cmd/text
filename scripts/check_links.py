import re
from pathlib import Path

p = Path(".")
html_files = list(p.glob("*.html")) + list((p / "health").glob("**/*.html"))

all_pages = set()
for hf in html_files:
    rel = hf.relative_to(p).as_posix()
    if rel == "index.html":
        all_pages.add("/")
    elif rel.endswith("/index.html"):
        all_pages.add("/" + rel[:-10])
        all_pages.add("/" + rel[:-11])
    elif rel.endswith(".html"):
        all_pages.add("/" + rel[:-5])
        all_pages.add("/" + rel)

print(f"Total known routes: {len(all_pages)}")

broken = []
for hf in html_files:
    txt = hf.read_text(encoding="utf-8", errors="ignore")
    # find all href="/..."
    import urllib.parse
    links = re.findall(r'href=[\'"](/[^"\'#?]+)[\'"]', txt)
    for link_raw in links:
        link = urllib.parse.unquote(link_raw)
        if link.startswith("//"):
            continue
        link_clean = link.rstrip("/")
        if link == "/" or link == "/rss.xml" or link == "/sitemap.xml" or link == "/favicon.svg" or link.startswith("/style") or link.startswith("/images") or link.startswith("/css") or link.startswith("/wp-content") or link.startswith("/feed") or link.startswith("/wp-includes"):
            continue
        if link not in all_pages and link_clean not in all_pages and (link + "/") not in all_pages:
            broken.append((str(hf.relative_to(p)), link))

if broken:
    unique_broken = set(broken)
    print(f"Broken internal links found: {len(unique_broken)}")
    for f, l in sorted(list(unique_broken))[:20]:
        print(f"  {f} -> {l}")
else:
    print("ALL INTERNAL LINKS ARE 100% VALID!")

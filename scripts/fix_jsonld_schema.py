import os, re, json
from pathlib import Path

repo = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")
posts = [p for p in (repo / "health").iterdir() if p.is_dir()]

updated_count = 0

for p in posts:
    idx = p / "index.html"
    if not idx.exists():
        continue
    content = idx.read_text(encoding="utf-8")
    
    # Skip redirect stubs
    if "meta http-equiv=\"refresh\"" in content.lower():
        continue
        
    slug = p.name
    canonical_url = f"https://healthfit100.com/health/{slug}/"
    
    # Extract Title
    title_match = re.search(r"<title>(.*?)</title>", content)
    raw_title = title_match.group(1).split("|")[0].strip() if title_match else slug
    
    # Extract Description
    desc_match = re.search(r'<meta name="description" content="(.*?)"', content)
    description = desc_match.group(1).strip() if desc_match else raw_title
    
    # Extract Published date
    pub_match = re.search(r'<meta property="article:published_time" content="(.*?)"', content)
    published_date = pub_match.group(1).strip() if pub_match else "2026-10-01T09:00:00+09:00"
    
    # Extract Modified date
    mod_match = re.search(r'<meta property="article:modified_time" content="(.*?)"', content)
    modified_date = mod_match.group(1).strip() if mod_match else published_date
    
    # Extract Image
    img_match = re.search(r'<meta property="og:image" content="(.*?)"', content)
    og_image = img_match.group(1).strip() if img_match else f"{canonical_url}thumbnail.png"
    
    # Find existing JSON-LD
    schema_pattern = r'(<script type="application/ld\+json"[^>]*>)(.*?)(</script>)'
    schema_match = re.search(schema_pattern, content, re.DOTALL)
    
    if schema_match:
        old_json_str = schema_match.group(2)
        # Check if already matching
        if slug in old_json_str and raw_title in old_json_str:
            continue
            
        new_schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Person",
                    "@id": "https://healthfit100.com/#person",
                    "name": "건강노트",
                    "url": "https://healthfit100.com/about",
                    "logo": {
                        "@type": "ImageObject",
                        "@id": "https://healthfit100.com/#logo",
                        "url": "https://healthfit100.com/wp-content/uploads/2026/07/healthfit100.png",
                        "contentUrl": "https://healthfit100.com/wp-content/uploads/2026/07/healthfit100.png",
                        "caption": "건강노트",
                        "inLanguage": "ko-KR",
                        "width": "512",
                        "height": "512"
                    },
                    "image": {"@id": "https://healthfit100.com/#logo"}
                },
                {
                    "@type": "WebSite",
                    "@id": "https://healthfit100.com/#website",
                    "url": "https://healthfit100.com",
                    "name": "건강노트",
                    "alternateName": "healthfit100",
                    "publisher": {"@id": "https://healthfit100.com/#person"},
                    "inLanguage": "ko-KR"
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": f"{canonical_url}#breadcrumb",
                    "itemListElement": [
                        {"@type": "ListItem", "position": "1", "item": {"@id": "https://healthfit100.com", "name": "홈"}},
                        {"@type": "ListItem", "position": "2", "item": {"@id": "https://healthfit100.com/blog", "name": "건강,영양"}},
                        {"@type": "ListItem", "position": "3", "item": {"@id": canonical_url, "name": raw_title}}
                    ]
                },
                {
                    "@type": "WebPage",
                    "@id": f"{canonical_url}#webpage",
                    "url": canonical_url,
                    "name": raw_title,
                    "datePublished": published_date,
                    "dateModified": modified_date,
                    "isPartOf": {"@id": "https://healthfit100.com/#website"},
                    "inLanguage": "ko-KR",
                    "breadcrumb": {"@id": f"{canonical_url}#breadcrumb"}
                },
                {
                    "@type": "BlogPosting",
                    "headline": raw_title,
                    "datePublished": published_date,
                    "dateModified": modified_date,
                    "articleSection": "건강,영양",
                    "author": {"@id": "https://healthfit100.com/#person", "name": "건강노트"},
                    "publisher": {"@id": "https://healthfit100.com/#person"},
                    "description": description,
                    "name": raw_title,
                    "@id": f"{canonical_url}#richSnippet",
                    "isPartOf": {"@id": f"{canonical_url}#webpage"},
                    "inLanguage": "ko-KR",
                    "mainEntityOfPage": {"@id": f"{canonical_url}#webpage"},
                    "image": og_image
                }
            ]
        }
        
        replacement = f'{schema_match.group(1)}{json.dumps(new_schema, ensure_ascii=False)}{schema_match.group(3)}'
        content = content[:schema_match.start()] + replacement + content[schema_match.end():]
        idx.write_text(content, encoding="utf-8")
        updated_count += 1
        print(f"Updated JSON-LD schema for: {slug}")

print(f"\nTotal articles updated with exact JSON-LD schemas: {updated_count}")

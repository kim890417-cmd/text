from __future__ import annotations

import html
import json
import re
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import quote


BASE_URL = "https://healthfit100.com"
KST = timezone(timedelta(hours=9))
ROOT = Path.cwd()

STATIC_PAGES = [
    "/",
    "/blog",
    "/topics/diet/",
    "/topics/nutrition/",
    "/topics/checkup/",
    "/topics/life/",
    "/routine",
    "/checkup",
    "/quiz",
    "/bmi",
    "/calorie",
    "/protein",
    "/exercise",
    "/water",
    "/caffeine",
    "/alcohol",
    "/supplement",
    "/about",
    "/contact",
    "/privacy",
    "/app-privacy",
    "/terms",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def meta_content(content: str, name: str) -> str:
    patterns = (
        rf'<meta\s+name=["\']{re.escape(name)}["\'][^>]+content=["\']([^"\']*)',
        rf'<meta\s+content=["\']([^"\']*)["\'][^>]+name=["\']{re.escape(name)}',
    )
    for pattern in patterns:
        match = re.search(pattern, content, flags=re.IGNORECASE)
        if match:
            return html.unescape(match.group(1).strip())
    return ""


def title_from_html(content: str, slug: str) -> str:
    match = re.search(r"<title[^>]*>([\s\S]*?)</title>", content, flags=re.IGNORECASE)
    if not match:
        return slug.replace("-", " ")
    title = html.unescape(re.sub(r"<[^>]+>", "", match.group(1))).strip()
    return re.sub(r"\s*[-|]\s*건강노트\s*$", "", title).strip()


def schema_dates(content: str) -> tuple[datetime, datetime]:
    published = None
    modified = None
    def nodes(value):
        if isinstance(value, dict):
            yield value
            for child in value.values():
                yield from nodes(child)
        elif isinstance(value, list):
            for child in value:
                yield from nodes(child)

    for block in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>([\s\S]*?)</script>', content, re.IGNORECASE):
        try:
            for node in nodes(json.loads(block)):
                published = published or node.get("datePublished")
                modified = modified or node.get("dateModified")
        except json.JSONDecodeError:
            continue

    def parse(value: str | None) -> datetime | None:
        if not value:
            return None
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=KST)
            return parsed.astimezone(KST)
        except ValueError:
            return None

    now = datetime.now(KST)
    return parse(published) or now, parse(modified) or parse(published) or now


def rfc822(value: datetime) -> str:
    return value.strftime("%a, %d %b %Y %H:%M:%S %z")


def page_file(url_path: str) -> Path:
    if url_path.endswith("/") and url_path != "/":
        return ROOT / url_path.strip("/") / "index.html"
    return ROOT / ("index.html" if url_path == "/" else f"{url_path.strip('/')}.html")


def page_lastmod(url_path: str) -> str:
    path = page_file(url_path)
    if not path.is_file():
        return datetime.now(KST).strftime("%Y-%m-%d")
    try:
        value = subprocess.check_output(
            ["git", "log", "-1", "--format=%aI", "--", str(path.relative_to(ROOT))],
            cwd=ROOT, text=True, stderr=subprocess.DEVNULL,
        ).strip()
        if value:
            return datetime.fromisoformat(value).astimezone(KST).strftime("%Y-%m-%d")
    except (subprocess.SubprocessError, ValueError):
        pass
    return datetime.fromtimestamp(path.stat().st_mtime, KST).strftime("%Y-%m-%d")


posts = []
for post_file in sorted((ROOT / "health").glob("*/index.html")):
    content = read_text(post_file)
    robots = meta_content(content, "robots").lower()
    if "noindex" in robots:
        continue
    published, modified = schema_dates(content)
    posts.append(
        {
            "slug": post_file.parent.name,
            "title": title_from_html(content, post_file.parent.name),
            "description": meta_content(content, "description"),
            "published": published,
            "modified": modified,
        }
    )

posts.sort(key=lambda item: item["published"], reverse=True)

sitemap_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]
for url_path in STATIC_PAGES:
    sitemap_lines.extend(
        [
            "  <url>",
            f"    <loc>{BASE_URL}{url_path}</loc>",
            f"    <lastmod>{page_lastmod(url_path)}</lastmod>",
            "  </url>",
        ]
    )
for post in posts:
    encoded_slug = quote(post["slug"])
    sitemap_lines.extend(
        [
            "  <url>",
            f"    <loc>{BASE_URL}/health/{encoded_slug}/</loc>",
            f'    <lastmod>{post["modified"].strftime("%Y-%m-%d")}</lastmod>',
            "  </url>",
        ]
    )
sitemap_lines.append("</urlset>")
(ROOT / "sitemap.xml").write_text(
    "\n".join(sitemap_lines) + "\n", encoding="utf-8", newline="\n"
)

rss_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<rss version="2.0">',
    "<channel>",
    "  <title>건강노트</title>",
    f"  <link>{BASE_URL}/blog</link>",
    "  <description>영양제·식단·생활습관을 공신력 있는 자료와 비교 예시, 기록 방법으로 정리합니다.</description>",
    "  <language>ko-KR</language>",
    f"  <lastBuildDate>{rfc822(datetime.now(KST))}</lastBuildDate>",
]
for post in posts:
    link = f'{BASE_URL}/health/{quote(post["slug"])}/'
    rss_lines.extend(
        [
            "  <item>",
            f'    <title>{html.escape(post["title"])}</title>',
            f"    <link>{link}</link>",
            f"    <guid isPermaLink=\"true\">{link}</guid>",
            f'    <description>{html.escape(post["description"])}</description>',
            f'    <pubDate>{rfc822(post["published"])}</pubDate>',
            "  </item>",
        ]
    )
rss_lines.extend(["</channel>", "</rss>"])
(ROOT / "rss.xml").write_text(
    "\n".join(rss_lines) + "\n", encoding="utf-8", newline="\n"
)

print(f"sitemap.xml: 고정 페이지 {len(STATIC_PAGES)}개 + 건강 글 {len(posts)}개")
print(f"rss.xml: 건강 글 {len(posts)}개")

import os
import re
from datetime import datetime, timezone, timedelta

BASE_URL = "https://dream95.com"
KST = timezone(timedelta(hours=9))
NOW = datetime.now(KST)
TODAY = NOW.strftime("%Y-%m-%d")

# RFC822(영문 요일/월) — 로케일에 의존하지 않도록 직접 구성
_WD = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
_MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def rfc822(dt):
    return (f"{_WD[dt.weekday()]}, {dt.day:02d} {_MON[dt.month-1]} {dt.year} "
            f"{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d} +0900")

NOW_RSS = rfc822(NOW)

# 블로그 카테고리가 아닌 폴더 (건너뜀)
SKIP_DIRS = {
    'wp-content', 'wp-includes', 'functions', 'js', 'css', 'scripts',
    'tag', 'author', 'category', 'page', 'sample-page', 'feed',
    'netlify', 'node_modules',
}

STATIC_PAGES = [
    {"loc": "/",         "priority": "1.0", "changefreq": "weekly"},
    {"loc": "/blog",     "priority": "0.9", "changefreq": "weekly"},
    {"loc": "/bmi",        "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/calorie",    "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/protein",    "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/water",      "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/supplement", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/about",      "priority": "0.6", "changefreq": "monthly"},
    {"loc": "/contact",  "priority": "0.6", "changefreq": "monthly"},
    {"loc": "/privacy",  "priority": "0.4", "changefreq": "yearly"},
    {"loc": "/terms",    "priority": "0.4", "changefreq": "yearly"},
]

TOOL_ITEMS = [
    {"title": "BMI 계산기",        "link": "/bmi",     "desc": "키와 몸무게로 체질량지수(BMI)와 비만도, 표준체중을 계산하는 무료 도구입니다."},
    {"title": "하루 칼로리 계산기", "link": "/calorie", "desc": "기초대사량(BMR)과 하루 필요 칼로리(TDEE), 목표별 권장 칼로리를 계산합니다."},
    {"title": "단백질 섭취량 계산기", "link": "/protein", "desc": "체중과 활동 수준에 맞는 하루 단백질 권장량(g)을 계산합니다."},
    {"title": "물 섭취량 계산기",   "link": "/water",   "desc": "체중과 운동량으로 하루 권장 수분량을 계산하는 무료 도구입니다."},
    {"title": "영양제 권장량 조회", "link": "/supplement", "desc": "비타민·미네랄별 하루 권장 섭취량과 상한 섭취량을 조회합니다."},
]

def _read(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_title(content, slug):
    match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()
        title = re.split(r'\s*[\-\|]\s*(?:블로그|dream95|kim890417)', title)[0].strip()
        if title:
            return title
    return slug.replace('-', ' ')

def extract_description(content):
    match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    return match.group(1).strip() if match else ""

def extract_pubdate(content):
    """글의 실제 발행일(article:published_time → datePublished 순)을 KST로 반환."""
    m = (re.search(r'article:published_time["\']\s+content=["\']([^"\']+)["\']', content)
         or re.search(r'"datePublished"\s*:\s*"([^"]+)"', content))
    if m:
        try:
            dt = datetime.fromisoformat(m.group(1).replace('Z', '+00:00'))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=KST)
            return dt.astimezone(KST)
        except ValueError:
            pass
    return None

def escape_xml(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# 블로그 카테고리 자동 감지: 하위에 index.html이 있는 폴더를 포함한 디렉토리
posts = []
for cat_dir in sorted(os.listdir('.')):
    if not os.path.isdir(cat_dir) or cat_dir in SKIP_DIRS or cat_dir.startswith('.'):
        continue
    found_posts = False
    for slug in sorted(os.listdir(cat_dir)):
        index_path = os.path.join(cat_dir, slug, 'index.html')
        if os.path.isfile(index_path):
            content = _read(index_path)
            posts.append({
                "cat": cat_dir,
                "slug": slug,
                "title": extract_title(content, slug),
                "desc": extract_description(content),
                "date": extract_pubdate(content) or NOW,
            })
            found_posts = True
    if found_posts:
        print(f"  📁 카테고리 감지: {cat_dir}/")

# 최신 글이 위로 오도록 정렬
posts.sort(key=lambda p: p["date"], reverse=True)

# sitemap.xml 생성
sitemap_parts = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for page in STATIC_PAGES:
    sitemap_parts.append(f"""  <url>
    <loc>{BASE_URL}{page['loc']}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>""")

for post in posts:
    sitemap_parts.append(f"""  <url>
    <loc>{BASE_URL}/{post['cat']}/{post['slug']}/</loc>
    <lastmod>{post['date'].strftime('%Y-%m-%d')}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

sitemap_parts.append('</urlset>')

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sitemap_parts) + '\n')

print(f"✅ sitemap.xml: 도구 {len(STATIC_PAGES)}개 + 블로그 {len(posts)}개")

# rss.xml 생성
rss_items = []

for post in posts:
    rss_items.append(f"""  <item>
    <title>{escape_xml(post['title'])}</title>
    <link>{BASE_URL}/{post['cat']}/{post['slug']}/</link>
    <description>{escape_xml(post['desc'])}</description>
    <pubDate>{rfc822(post['date'])}</pubDate>
  </item>""")

for tool in TOOL_ITEMS:
    rss_items.append(f"""  <item>
    <title>{escape_xml(tool['title'])}</title>
    <link>{BASE_URL}{tool['link']}</link>
    <description>{escape_xml(tool['desc'])}</description>
  </item>""")

rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>건강노트</title>
  <link>{BASE_URL}</link>
  <description>영양제·식단·생활습관 등 일상 건강 정보와 무료 건강 계산기를 제공하는 블로그</description>
  <language>ko</language>
  <lastBuildDate>{NOW_RSS}</lastBuildDate>

{chr(10).join(rss_items)}
</channel>
</rss>
"""

with open('rss.xml', 'w', encoding='utf-8') as f:
    f.write(rss_content)

print(f"✅ rss.xml: 블로그 {len(posts)}개 + 도구 {len(TOOL_ITEMS)}개")

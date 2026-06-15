import os
import re
from datetime import datetime

BASE_URL = "https://dream95.com"
HEALTH_DIR = "health"
TODAY = datetime.now().strftime("%Y-%m-%d")
TODAY_RSS = datetime.now().strftime("%a, %d %b %Y 00:00:00 +0900")

STATIC_PAGES = [
    {"loc": "/",               "priority": "1.0", "changefreq": "weekly"},
    {"loc": "/blog",           "priority": "0.9", "changefreq": "weekly"},
    {"loc": "/short",          "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/compressor",     "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/upscaler",       "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/eraser",         "priority": "0.8", "changefreq": "monthly"},
    {"loc": "/keyword_analyzer","priority": "0.8", "changefreq": "monthly"},
    {"loc": "/about",          "priority": "0.6", "changefreq": "monthly"},
    {"loc": "/contact",        "priority": "0.6", "changefreq": "monthly"},
    {"loc": "/privacy",        "priority": "0.4", "changefreq": "yearly"},
    {"loc": "/terms",          "priority": "0.4", "changefreq": "yearly"},
]

TOOL_ITEMS = [
    {"title": "이미지 용량 줄이기",     "link": "/compressor",      "desc": "화질 저하 없이 이미지 파일 크기를 압축하는 무료 온라인 도구입니다."},
    {"title": "이미지 화질 올리기",     "link": "/upscaler",        "desc": "저해상도 이미지를 AI 기술로 2배·4배 업스케일합니다."},
    {"title": "AI 배경 제거",           "link": "/eraser",          "desc": "AI가 자동으로 이미지 배경을 제거하고 투명 PNG로 저장합니다."},
    {"title": "단축링크 만들기",         "link": "/short",           "desc": "긴 URL을 짧게 만들고 클릭 통계를 확인하는 무료 서비스입니다."},
    {"title": "키워드 연관검색어 조회", "link": "/keyword_analyzer", "desc": "Google·Naver 연관검색어를 한눈에 확인하는 SEO 도구입니다."},
]

def extract_title(html_path):
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            # 사이트명 제거 ( " - 사이트명" 또는 " | 사이트명" 형태)
            title = re.split(r'\s*[\-\|]\s*(?:블로그|dream95|kim890417)', title)[0].strip()
            return title
    except:
        pass
    return None

def extract_description(html_path):
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    except:
        pass
    return ""

def escape_xml(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# health/ 폴더에서 글 목록 수집
posts = []
if os.path.exists(HEALTH_DIR):
    for slug in sorted(os.listdir(HEALTH_DIR)):
        index_path = os.path.join(HEALTH_DIR, slug, 'index.html')
        if os.path.isfile(index_path):
            title = extract_title(index_path) or slug.replace('-', ' ')
            desc = extract_description(index_path)
            posts.append({"slug": slug, "title": title, "desc": desc})

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
    <loc>{BASE_URL}/{HEALTH_DIR}/{post['slug']}/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

sitemap_parts.append('</urlset>')

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sitemap_parts) + '\n')

print(f"✅ sitemap.xml 생성: 도구 {len(STATIC_PAGES)}개 + 블로그 {len(posts)}개")

# rss.xml 생성
rss_items = []

for post in posts:
    rss_items.append(f"""  <item>
    <title>{escape_xml(post['title'])}</title>
    <link>{BASE_URL}/{HEALTH_DIR}/{post['slug']}/</link>
    <description>{escape_xml(post['desc'])}</description>
    <pubDate>{TODAY_RSS}</pubDate>
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
  <title>블로그 도구모음</title>
  <link>{BASE_URL}</link>
  <description>블로그 운영에 필요한 무료 AI 도구와 건강·생활 정보를 제공하는 플랫폼</description>
  <language>ko</language>
  <lastBuildDate>{TODAY_RSS}</lastBuildDate>

{chr(10).join(rss_items)}
</channel>
</rss>
"""

with open('rss.xml', 'w', encoding='utf-8') as f:
    f.write(rss_content)

print(f"✅ rss.xml 생성: 블로그 {len(posts)}개 + 도구 {len(TOOL_ITEMS)}개")

import re
from pathlib import Path

repo_dir = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Update index.html
index_file = repo_dir / "index.html"
index_html = index_file.read_text(encoding="utf-8")

article1_home_card = """<article class="story"><a href="/health/nutrition-facts-sugar-serving-size-calculation/"><div class="story-image"><img src="/images/note/articles/nutrition-facts-sugar-serving-size-calculation.webp" alt="은색 모자를 쓴 흰 고양이 노트가 식품 영양성분표의 1회 제공량과 총내용량을 계산기로 곱하는 일러스트" width="960" height="640" loading="lazy"><span>영양성분표 1회 제공량 계산</span></div><div class="story-copy"><small>영양제·표시 읽기 · 2026.10.15</small><h3>영양성분표 보는법｜1회 제공량과 총내용량 당류 함정 피하는 계산법</h3><p>포장 앞면의 ‘당류 6g’만 보고 골랐는데 한 봉지 다 먹으면 얼마일까? 기준 용량과 총내용량의 곱셈 공식으로 실제 섭취량을 계산합니다.</p></div></a></article>"""

article2_home_card = """<article class="story"><a href="/health/caffeine-daily-intake-drinks-record-method/"><div class="story-image"><img src="/images/note/articles/caffeine-daily-intake-drinks-record-method.webp" alt="은색 모자를 쓴 흰 고양이 노트가 커피잔과 에너지음료 캔의 카페인 밀리그램 수치를 수첩에 적는 일러스트" width="960" height="640" loading="lazy"><span>하루 카페인 섭취량 계산</span></div><div class="story-copy"><small>생활·수면 · 2026.10.15</small><h3>하루 카페인 섭취량 계산 기록법, 캔커피·아메리카노 표시 찾는 순서</h3><p>오늘 마신 커피 두 잔과 에너지음료 한 캔, 카페인 총합은 몇 mg일까? 캔 라벨의 고카페인 표시 위치와 하루 누적 계산법을 정리합니다.</p></div></a></article>"""

# Insert article 1 into nutrition section
if "nutrition-facts-sugar-serving-size-calculation" not in index_html:
    nut_marker = '<section id="nutrition" class="category-section"><div class="section-title"><h2><a href="/topics/nutrition/">영양제·표시 읽기</a></h2><a href="/topics/nutrition/">전체 보기 →</a></div><p class="section-desc">효능 문구에서 바로 구매로 넘어가지 않습니다. 하루분, 단위, 중복 성분과 적용 대상을 먼저 확인합니다.</p><div class="stories">'
    index_html = index_html.replace(nut_marker, nut_marker + article1_home_card)
    print("Added Article 1 to index.html nutrition section")

# Insert article 2 into life section
if "caffeine-daily-intake-drinks-record-method" not in index_html:
    life_marker = '<section id="life" class="category-section"><div class="section-title"><h2><a href="/topics/life/">생활·수면</a></h2><a href="/topics/life/">전체 보기 →</a></div><p class="section-desc">건강 조언이 실제 하루에 들어갈 수 있는지 살펴봅니다. 느낌과 측정값을 구분하고 작은 기록을 남깁니다.</p><div class="stories">'
    index_html = index_html.replace(life_marker, life_marker + article2_home_card)
    print("Added Article 2 to index.html life section")

index_file.write_text(index_html, encoding="utf-8")

# 2. Update blog.html
blog_file = repo_dir / "blog.html"
blog_html = blog_file.read_text(encoding="utf-8")

if "nutrition-facts-sugar-serving-size-calculation" not in blog_html:
    nut_marker_blog = '<section id="nutrition" class="category-section"><div class="section-title"><h2><a href="/topics/nutrition/">영양제·표시 읽기</a></h2>'
    # find stories inside nutrition in blog.html
    idx_nut = blog_html.find('id="nutrition"')
    if idx_nut != -1:
        idx_stories = blog_html.find('<div class="stories">', idx_nut)
        if idx_stories != -1:
            ins_pos = idx_stories + len('<div class="stories">')
            blog_html = blog_html[:ins_pos] + article1_home_card + blog_html[ins_pos:]
            print("Added Article 1 to blog.html nutrition section")

if "caffeine-daily-intake-drinks-record-method" not in blog_html:
    idx_life = blog_html.find('id="life"')
    if idx_life != -1:
        idx_stories = blog_html.find('<div class="stories">', idx_life)
        if idx_stories != -1:
            ins_pos = idx_stories + len('<div class="stories">')
            blog_html = blog_html[:ins_pos] + article2_home_card + blog_html[ins_pos:]
            print("Added Article 2 to blog.html life section")

blog_file.write_text(blog_html, encoding="utf-8")

# 3. Update topics/nutrition/index.html
top_nut_file = repo_dir / "topics" / "nutrition" / "index.html"
top_nut_html = top_nut_file.read_text(encoding="utf-8")
if "nutrition-facts-sugar-serving-size-calculation" not in top_nut_html:
    idx_stories = top_nut_html.find('<div class="stories">')
    if idx_stories != -1:
        ins_pos = idx_stories + len('<div class="stories">')
        top_nut_html = top_nut_html[:ins_pos] + article1_home_card + top_nut_html[ins_pos:]
        top_nut_file.write_text(top_nut_html, encoding="utf-8")
        print("Added Article 1 to topics/nutrition/index.html")

# 4. Update topics/life/index.html
top_life_file = repo_dir / "topics" / "life" / "index.html"
top_life_html = top_life_file.read_text(encoding="utf-8")
if "caffeine-daily-intake-drinks-record-method" not in top_life_html:
    idx_stories = top_life_html.find('<div class="stories">')
    if idx_stories != -1:
        ins_pos = idx_stories + len('<div class="stories">')
        top_life_html = top_life_html[:ins_pos] + article2_home_card + top_life_html[ins_pos:]
        top_life_file.write_text(top_life_html, encoding="utf-8")
        print("Added Article 2 to topics/life/index.html")

# 5. Update sitemap.xml
sitemap_file = repo_dir / "sitemap.xml"
sitemap_xml = sitemap_file.read_text(encoding="utf-8")
sitemap_additions = """  <url>
    <loc>https://healthfit100.com/health/nutrition-facts-sugar-serving-size-calculation/</loc>
    <lastmod>2026-10-15</lastmod>
  </url>
  <url>
    <loc>https://healthfit100.com/health/caffeine-daily-intake-drinks-record-method/</loc>
    <lastmod>2026-10-15</lastmod>
  </url>
</urlset>"""

if "nutrition-facts-sugar-serving-size-calculation" not in sitemap_xml:
    sitemap_xml = sitemap_xml.replace("</urlset>", sitemap_additions)
    sitemap_file.write_text(sitemap_xml, encoding="utf-8")
    print("Added 2 new articles to sitemap.xml")

# 6. Update rss.xml
rss_file = repo_dir / "rss.xml"
rss_xml = rss_file.read_text(encoding="utf-8")
rss_items = """  <item>
    <title>영양성분표 보는법｜1회 제공량과 총내용량 당류 함정 피하는 계산법</title>
    <link>https://healthfit100.com/health/nutrition-facts-sugar-serving-size-calculation/</link>
    <guid isPermaLink="true">https://healthfit100.com/health/nutrition-facts-sugar-serving-size-calculation/</guid>
    <description>영양성분표 보는법과 1회 제공량·총내용량 당류 계산법을 중심으로 근거의 조건과 비교 방법을 정리합니다. 운영자의 실제 식사·구매 경험과 노트의 판단을 함께 읽고 내 상황에서 확인할 질문을 남겨보세요.</description>
    <pubDate>Thu, 15 Oct 2026 10:00:00 +0900</pubDate>
  </item>
  <item>
    <title>하루 카페인 섭취량 계산 기록법, 캔커피·아메리카노 표시 찾는 순서</title>
    <link>https://healthfit100.com/health/caffeine-daily-intake-drinks-record-method/</link>
    <guid isPermaLink="true">https://healthfit100.com/health/caffeine-daily-intake-drinks-record-method/</guid>
    <description>하루 카페인 섭취량 계산법과 캔커피·프랜차이즈 음료 라벨에서 수치 찾는 순서를 정리합니다. 운영자의 실제 식사·구매 경험과 노트의 판단을 함께 읽고 내 상황에서 확인할 질문을 남겨보세요.</description>
    <pubDate>Thu, 15 Oct 2026 10:00:00 +0900</pubDate>
  </item>
"""

if "nutrition-facts-sugar-serving-size-calculation" not in rss_xml:
    rss_xml = rss_xml.replace("<channel>\n", f"<channel>\n{rss_items}")
    rss_file.write_text(rss_xml, encoding="utf-8")
    print("Added 2 new articles to rss.xml")

# 7. Update all_english_urls.txt
urls_file = repo_dir / "all_english_urls.txt"
urls_text = urls_file.read_text(encoding="utf-8")
new_top_urls = """1. [영양성분표 보는법｜1회 제공량과 총내용량 당류 함정 피하는 계산법]
https://healthfit100.com/health/nutrition-facts-sugar-serving-size-calculation/

2. [하루 카페인 섭취량 계산 기록법, 캔커피·아메리카노 표시 찾는 순서]
https://healthfit100.com/health/caffeine-daily-intake-drinks-record-method/

"""
urls_file.write_text(new_top_urls + urls_text, encoding="utf-8")
print("Updated all_english_urls.txt")

print("\nAll site registrations completed successfully!")

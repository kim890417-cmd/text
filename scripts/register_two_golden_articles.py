import re
from pathlib import Path

repo_dir = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

article1_card = """<article class="story"><a href="/health/skeletal-muscle-mass-average-male-female/"><div class="story-image"><img src="/images/note/articles/skeletal-muscle-mass-average-male-female.webp" alt="은색 모자를 쓴 흰 고양이 노트가 인바디 결과지의 골격근량 수치와 체중 비율을 비교하는 일러스트" width="960" height="640" loading="lazy"><span>남녀 골격근량 평균</span></div><div class="story-copy"><small>식단·체중 · 2026.10.18</small><h3>골격근량 평균 남자 여자 기준표, 인바디 검사 후 체중별 정상 범위 계산법</h3><p>인바디 결과지 골격근량 22kg, 35kg… 내 몸무게에서 평균 이상일까? 남녀 체중 대비 표준 근육 비율(%) 계산법과 C자·D자 그래프 해석을 정리합니다.</p></div></a></article>"""

article2_card = """<article class="story"><a href="/health/aquacelle-omega3-rtg-purity-calculation/"><div class="story-image"><img src="/images/note/articles/aquacelle-omega3-rtg-purity-calculation.webp" alt="은색 모자를 쓴 흰 고양이 노트가 콰이퍼셀 오메가3와 알티지 오메가3의 분자 구조와 순도를 계산기로 비교하는 일러스트" width="960" height="640" loading="lazy"><span>콰이퍼셀 오메가3 rTG 차이</span></div><div class="story-copy"><small>영양제·표시 읽기 · 2026.10.18</small><h3>콰이퍼셀 오메가3 알티지와 차이, 흡수율 3배 광고와 EPA DHA 순도 계산법</h3><p>기존 rTG보다 2~3배 비싼 콰이퍼셀 오메가3, 진짜 돈값을 할까? 미셀화 유화 공법의 원리와 캡슐당 순수 EPA+DHA 순도(%) 계산법을 정리합니다.</p></div></a></article>"""

# 1. Update index.html
index_file = repo_dir / "index.html"
index_html = index_file.read_text(encoding="utf-8")

if "skeletal-muscle-mass-average-male-female" not in index_html:
    diet_marker = '<section id="diet" class="category-section"><div class="section-title"><h2><a href="/topics/diet/">식단·체중</a></h2><a href="/topics/diet/">전체 보기 →</a></div><p class="section-desc">숫자보다 한 끼와 생활 조건을 봅니다. 같은 기준으로 비교하고, 오래 지속할 수 있는 선택인지 따져봅니다.</p><div class="stories">'
    index_html = index_html.replace(diet_marker, diet_marker + article1_card)
    print("Added article 1 to index.html diet section")

if "aquacelle-omega3-rtg-purity-calculation" not in index_html:
    nut_marker = '<section id="nutrition" class="category-section"><div class="section-title"><h2><a href="/topics/nutrition/">영양제·표시 읽기</a></h2><a href="/topics/nutrition/">전체 보기 →</a></div><p class="section-desc">효능 문구에서 바로 구매로 넘어가지 않습니다. 하루분, 단위, 중복 성분과 적용 대상을 먼저 확인합니다.</p><div class="stories">'
    index_html = index_html.replace(nut_marker, nut_marker + article2_card)
    print("Added article 2 to index.html nutrition section")

index_file.write_text(index_html, encoding="utf-8")

# 2. Update blog.html
blog_file = repo_dir / "blog.html"
blog_html = blog_file.read_text(encoding="utf-8")

if "skeletal-muscle-mass-average-male-female" not in blog_html:
    idx_diet = blog_html.find('id="diet"')
    if idx_diet != -1:
        idx_stories = blog_html.find('<div class="stories">', idx_diet)
        if idx_stories != -1:
            ins_pos = idx_stories + len('<div class="stories">')
            blog_html = blog_html[:ins_pos] + article1_card + blog_html[ins_pos:]
            print("Added article 1 to blog.html diet section")

if "aquacelle-omega3-rtg-purity-calculation" not in blog_html:
    idx_nut = blog_html.find('id="nutrition"')
    if idx_nut != -1:
        idx_stories = blog_html.find('<div class="stories">', idx_nut)
        if idx_stories != -1:
            ins_pos = idx_stories + len('<div class="stories">')
            blog_html = blog_html[:ins_pos] + article2_card + blog_html[ins_pos:]
            print("Added article 2 to blog.html nutrition section")

blog_file.write_text(blog_html, encoding="utf-8")

# 3. Update topics/diet/index.html
top_diet_file = repo_dir / "topics" / "diet" / "index.html"
top_diet_html = top_diet_file.read_text(encoding="utf-8")
if "skeletal-muscle-mass-average-male-female" not in top_diet_html:
    idx_stories = top_diet_html.find('<div class="stories">')
    if idx_stories != -1:
        ins_pos = idx_stories + len('<div class="stories">')
        top_diet_html = top_diet_html[:ins_pos] + article1_card + top_diet_html[ins_pos:]
        top_diet_file.write_text(top_diet_html, encoding="utf-8")
        print("Added article 1 to topics/diet/index.html")

# 4. Update topics/nutrition/index.html
top_nut_file = repo_dir / "topics" / "nutrition" / "index.html"
top_nut_html = top_nut_file.read_text(encoding="utf-8")
if "aquacelle-omega3-rtg-purity-calculation" not in top_nut_html:
    idx_stories = top_nut_html.find('<div class="stories">')
    if idx_stories != -1:
        ins_pos = idx_stories + len('<div class="stories">')
        top_nut_html = top_nut_html[:ins_pos] + article2_card + top_nut_html[ins_pos:]
        top_nut_file.write_text(top_nut_html, encoding="utf-8")
        print("Added article 2 to topics/nutrition/index.html")

# 5. Update sitemap.xml
sitemap_file = repo_dir / "sitemap.xml"
sitemap_xml = sitemap_file.read_text(encoding="utf-8")
sitemap_addition = """  <url>
    <loc>https://healthfit100.com/health/skeletal-muscle-mass-average-male-female/</loc>
    <lastmod>2026-10-18</lastmod>
  </url>
  <url>
    <loc>https://healthfit100.com/health/aquacelle-omega3-rtg-purity-calculation/</loc>
    <lastmod>2026-10-18</lastmod>
  </url>
</urlset>"""

if "skeletal-muscle-mass-average-male-female" not in sitemap_xml:
    sitemap_xml = sitemap_xml.replace("</urlset>", sitemap_addition)
    sitemap_file.write_text(sitemap_xml, encoding="utf-8")
    print("Added 2 new articles to sitemap.xml")

# 6. Update rss.xml
rss_file = repo_dir / "rss.xml"
rss_xml = rss_file.read_text(encoding="utf-8")
rss_items = """  <item>
    <title>골격근량 평균 남자 여자 기준표, 인바디 검사 후 체중별 정상 범위 계산법</title>
    <link>https://healthfit100.com/health/skeletal-muscle-mass-average-male-female/</link>
    <guid isPermaLink="true">https://healthfit100.com/health/skeletal-muscle-mass-average-male-female/</guid>
    <description>남자 여자 골격근량 평균 기준표와 체중별 정상 비율 계산법, 근육량(Total Muscle)과의 차이를 정리합니다. 운영자의 실제 인바디 측정·식비 경험과 노트의 판단을 함께 읽고 내 상황에서 확인할 질문을 남겨보세요.</description>
    <pubDate>Sun, 18 Oct 2026 02:00:00 +0900</pubDate>
  </item>
  <item>
    <title>콰이퍼셀 오메가3 알티지와 차이, 흡수율 3배 광고와 EPA DHA 순도 계산법</title>
    <link>https://healthfit100.com/health/aquacelle-omega3-rtg-purity-calculation/</link>
    <guid isPermaLink="true">https://healthfit100.com/health/aquacelle-omega3-rtg-purity-calculation/</guid>
    <description>콰이퍼셀 오메가3와 알티지(rTG)의 공법 차이, 흡수율 3배 광고의 전제 조건과 캡슐당 EPA DHA 순도 계산법을 정리합니다. 운영자의 실제 영양제 구매·복용 경험과 노트의 판단을 함께 읽고 내 상황에서 확인할 질문을 남겨보세요.</description>
    <pubDate>Sun, 18 Oct 2026 02:00:00 +0900</pubDate>
  </item>
"""

if "skeletal-muscle-mass-average-male-female" not in rss_xml:
    rss_xml = rss_xml.replace("<channel>\n", f"<channel>\n{rss_items}")
    rss_file.write_text(rss_xml, encoding="utf-8")
    print("Added 2 new articles to rss.xml")

# 7. Update all_english_urls.txt
urls_file = repo_dir / "all_english_urls.txt"
urls_text = urls_file.read_text(encoding="utf-8")
new_top_urls = """1. [골격근량 평균 남자 여자 기준표, 인바디 검사 후 체중별 정상 범위 계산법]
https://healthfit100.com/health/skeletal-muscle-mass-average-male-female/

2. [콰이퍼셀 오메가3 알티지와 차이, 흡수율 3배 광고와 EPA DHA 순도 계산법]
https://healthfit100.com/health/aquacelle-omega3-rtg-purity-calculation/

"""
urls_file.write_text(new_top_urls + urls_text, encoding="utf-8")
print("Updated all_english_urls.txt")

print("\nAll site registrations for 2 articles completed successfully!")

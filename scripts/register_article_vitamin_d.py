import re
from pathlib import Path

repo_dir = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

article_home_card = """<article class="story"><a href="/health/vitamin-d-5000iu-2000iu-daily-dosage/"><div class="story-image"><img src="/images/note/articles/vitamin-d-5000iu-2000iu-daily-dosage.webp" alt="은색 모자를 쓴 흰 고양이 노트가 비타민D 5000IU와 2000IU 영양제 병의 라벨을 비교하는 일러스트" width="960" height="640" loading="lazy"><span>비타민D 5000IU 매일 복용</span></div><div class="story-copy"><small>영양제·표시 읽기 · 2026.10.18</small><h3>비타민D 5000IU 매일 먹어도 될까? 2000IU 차이와 종합비타민 중복 계산법</h3><p>해외직구로 산 5000IU 캡슐, 매일 먹으면 상한량 4000IU를 넘길까? 2000IU와의 목적별 차이와 종합비타민 속 비타민D 합산 계산식을 정리합니다.</p></div></a></article>"""

# 1. Update index.html
index_file = repo_dir / "index.html"
index_html = index_file.read_text(encoding="utf-8")

if "vitamin-d-5000iu-2000iu-daily-dosage" not in index_html:
    nut_marker = '<section id="nutrition" class="category-section"><div class="section-title"><h2><a href="/topics/nutrition/">영양제·표시 읽기</a></h2><a href="/topics/nutrition/">전체 보기 →</a></div><p class="section-desc">효능 문구에서 바로 구매로 넘어가지 않습니다. 하루분, 단위, 중복 성분과 적용 대상을 먼저 확인합니다.</p><div class="stories">'
    index_html = index_html.replace(nut_marker, nut_marker + article_home_card)
    index_file.write_text(index_html, encoding="utf-8")
    print("Added to index.html nutrition section")

# 2. Update blog.html
blog_file = repo_dir / "blog.html"
blog_html = blog_file.read_text(encoding="utf-8")

if "vitamin-d-5000iu-2000iu-daily-dosage" not in blog_html:
    idx_nut = blog_html.find('id="nutrition"')
    if idx_nut != -1:
        idx_stories = blog_html.find('<div class="stories">', idx_nut)
        if idx_stories != -1:
            ins_pos = idx_stories + len('<div class="stories">')
            blog_html = blog_html[:ins_pos] + article_home_card + blog_html[ins_pos:]
            blog_file.write_text(blog_html, encoding="utf-8")
            print("Added to blog.html nutrition section")

# 3. Update topics/nutrition/index.html
top_nut_file = repo_dir / "topics" / "nutrition" / "index.html"
top_nut_html = top_nut_file.read_text(encoding="utf-8")
if "vitamin-d-5000iu-2000iu-daily-dosage" not in top_nut_html:
    idx_stories = top_nut_html.find('<div class="stories">')
    if idx_stories != -1:
        ins_pos = idx_stories + len('<div class="stories">')
        top_nut_html = top_nut_html[:ins_pos] + article_home_card + top_nut_html[ins_pos:]
        top_nut_file.write_text(top_nut_html, encoding="utf-8")
        print("Added to topics/nutrition/index.html")

# 4. Update sitemap.xml
sitemap_file = repo_dir / "sitemap.xml"
sitemap_xml = sitemap_file.read_text(encoding="utf-8")
sitemap_addition = """  <url>
    <loc>https://healthfit100.com/health/vitamin-d-5000iu-2000iu-daily-dosage/</loc>
    <lastmod>2026-10-18</lastmod>
  </url>
</urlset>"""

if "vitamin-d-5000iu-2000iu-daily-dosage" not in sitemap_xml:
    sitemap_xml = sitemap_xml.replace("</urlset>", sitemap_addition)
    sitemap_file.write_text(sitemap_xml, encoding="utf-8")
    print("Added to sitemap.xml")

# 5. Update rss.xml
rss_file = repo_dir / "rss.xml"
rss_xml = rss_file.read_text(encoding="utf-8")
rss_item = """  <item>
    <title>비타민D 5000IU 매일 먹어도 될까? 2000IU 차이와 종합비타민 중복 계산법</title>
    <link>https://healthfit100.com/health/vitamin-d-5000iu-2000iu-daily-dosage/</link>
    <guid isPermaLink="true">https://healthfit100.com/health/vitamin-d-5000iu-2000iu-daily-dosage/</guid>
    <description>비타민D 5000IU 매일 복용 안전성과 2000IU 차이, 상한섭취량 4000IU 및 종합비타민 중복 계산법을 정리합니다. 운영자의 실제 영양제 직구·식사 경험과 노트의 판단을 함께 읽고 내 상황에서 확인할 질문을 남겨보세요.</description>
    <pubDate>Sun, 18 Oct 2026 01:00:00 +0900</pubDate>
  </item>
"""

if "vitamin-d-5000iu-2000iu-daily-dosage" not in rss_xml:
    rss_xml = rss_xml.replace("<channel>\n", f"<channel>\n{rss_item}")
    rss_file.write_text(rss_xml, encoding="utf-8")
    print("Added to rss.xml")

# 6. Update all_english_urls.txt
urls_file = repo_dir / "all_english_urls.txt"
urls_text = urls_file.read_text(encoding="utf-8")
new_top_url = """1. [비타민D 5000IU 매일 먹어도 될까? 2000IU 차이와 종합비타민 중복 계산법]
https://healthfit100.com/health/vitamin-d-5000iu-2000iu-daily-dosage/

"""
urls_file.write_text(new_top_url + urls_text, encoding="utf-8")
print("Updated all_english_urls.txt")

print("\nAll site registrations for vitamin-d-5000iu completed successfully!")

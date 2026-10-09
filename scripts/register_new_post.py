import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Update blog.html
blog_file = REPO_DIR / "blog.html"
blog_content = blog_file.read_text(encoding="utf-8")

new_post_card = """<article class="post-410 post type-post status-publish format-standard has-post-thumbnail hentry ast-article-post" id="post-410">
  <div class="ast-post-format- has-post-thumbnail blog-layout-4 ast-article-inner">
    <div class="post-thumb-img-content">
		<a href="/health/fasting-blood-sugar-normal-range-prediabetes/">
			<img src="/health/fasting-blood-sugar-normal-range-prediabetes/thumbnail.png" alt="공복 혈당 정상 수치 기준과 당뇨 전단계 낮추는 법, 당화혈색소(HbA1c) 관리 가이드" loading="lazy">
		</a>
	</div>
    <div class="post-content ast-grid-common-col">
      <span class="ast-blog-single-element ast-taxonomy-container cat-links default"><a href="/blog" rel="category tag">건강,영양</a></span>
      <h2 class="entry-title ast-blog-single-element" itemprop="headline">
        <a href="/health/fasting-blood-sugar-normal-range-prediabetes/" rel="bookmark">공복 혈당 정상 수치 기준과 당뇨 전단계 낮추는 법, 당화혈색소(HbA1c) 관리 가이드</a>
      </h2>
      <header class="entry-header ast-blog-single-element ast-blog-meta-container">
        <div class="entry-meta"><span class="posted-by vcard author"><a title="건강노트의 모든 글 보기" href="/about" rel="author" class="url fn n"><span class="author-name">건강노트</span></a></span> / <span class="posted-on"><span class="published"> 10월 9, 2026 </span></span></div>
      </header>
      <div class="ast-excerpt-container ast-blog-single-element">
        <p>국가건강검진 공복 혈당 정상 수치(100 mg/dL 미만)와 당뇨 전단계(100~125 mg/dL) 기준, 당화혈색소(HbA1c 5.7~6.4%) 해석법 및 인슐린 저항성을 개선하는 생활수칙을 정리했습니다.</p>
      </div>
      <div style="font-size:0.82rem; color:#0284c7; font-weight:600; margin-top:4px;">
        연관 계산기: <a href="/checkup" style="color:#0284c7; text-decoration:underline;">건강검진 판독 가이드</a> · <a href="/calorie" style="color:#0284c7; text-decoration:underline;">하루 칼로리·TDEE 계산기</a>
      </div>
    </div>
  </div>
</article>
"""

if "fasting-blood-sugar-normal-range-prediabetes" not in blog_content:
    blog_content = blog_content.replace('<div class="ast-row">\n', f'<div class="ast-row">\n{new_post_card}\n', 1)
    blog_file.write_text(blog_content, encoding="utf-8")
    print("blog.html updated with new post card.")
else:
    print("blog.html already contains new post.")

# 2. Update index.html
index_file = REPO_DIR / "index.html"
index_content = index_file.read_text(encoding="utf-8")

new_index_item = """          <!-- Article 0: 공복 혈당 정상 수치 & 당뇨 전단계 -->
          <a href="/health/fasting-blood-sugar-normal-range-prediabetes/" class="article-feed-item">
            <div class="article-feed-thumb">
              <img src="/health/fasting-blood-sugar-normal-range-prediabetes/thumbnail.png" alt="공복 혈당 정상 수치 기준과 당뇨 전단계 낮추는 법" loading="lazy">
            </div>
            <div class="article-feed-content">
              <div class="article-feed-meta">
                <span class="article-feed-cat">혈당·검진</span>
                <span>5분 읽기 · 대한당뇨병학회 기준</span>
              </div>
              <h3 class="article-feed-title">공복 혈당 정상 수치 기준과 당뇨 전단계 낮추는 법, 당화혈색소(HbA1c) 관리 가이드</h3>
              <p class="article-feed-excerpt">국가건강검진 공복 혈당 100~125 mg/dL 구간의 진짜 의미와 당화혈색소(HbA1c) 판독법, 야식 차단과 하체 근력 운동으로 인슐린 저항성을 개선하는 과학적 생활 수칙을 정리했습니다.</p>
              <div class="article-feed-related">
                연관 도구: 건강검진 판독 가이드 · 하루 칼로리(TDEE) 계산기
              </div>
            </div>
          </a>
"""

if "fasting-blood-sugar-normal-range-prediabetes" not in index_content:
    # Update badge count from "8편 엄선" to "9편 엄선"
    index_content = index_content.replace('8편 엄선', '9편 엄선')
    index_content = index_content.replace('<div class="article-feed">\n', f'<div class="article-feed">\n{new_index_item}\n', 1)
    index_file.write_text(index_content, encoding="utf-8")
    print("index.html updated with new magazine item.")
else:
    print("index.html already contains new item.")

# 3. Update sitemap.xml
sitemap_file = REPO_DIR / "sitemap.xml"
if sitemap_file.exists():
    sitemap_content = sitemap_file.read_text(encoding="utf-8")
    if "fasting-blood-sugar-normal-range-prediabetes" not in sitemap_content:
        new_url_entry = """  <url>
    <loc>https://healthfit100.com/health/fasting-blood-sugar-normal-range-prediabetes/</loc>
    <lastmod>2026-10-09T09:00:00+09:00</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
        sitemap_content = sitemap_content.replace('</urlset>', f'{new_url_entry}</urlset>')
        sitemap_file.write_text(sitemap_content, encoding="utf-8")
        print("sitemap.xml updated.")

# 4. Update rss.xml
rss_file = REPO_DIR / "rss.xml"
if rss_file.exists():
    rss_content = rss_file.read_text(encoding="utf-8")
    if "fasting-blood-sugar-normal-range-prediabetes" not in rss_content:
        new_rss_item = """    <item>
      <title>공복 혈당 정상 수치 기준과 당뇨 전단계 낮추는 법, 당화혈색소(HbA1c) 관리 가이드</title>
      <link>https://healthfit100.com/health/fasting-blood-sugar-normal-range-prediabetes/</link>
      <guid>https://healthfit100.com/health/fasting-blood-sugar-normal-range-prediabetes/</guid>
      <pubDate>Fri, 09 Oct 2026 09:00:00 +0900</pubDate>
      <description><![CDATA[국가건강검진 공복 혈당 정상 수치(100 mg/dL 미만)와 당뇨 전단계(100~125 mg/dL) 기준, 당화혈색소(HbA1c 5.7~6.4%) 해석법 및 인슐린 저항성을 개선하는 생활수칙을 정리했습니다.]]></description>
    </item>
"""
        rss_content = rss_content.replace('<channel>\n', f'<channel>\n{new_rss_item}\n', 1)
        rss_file.write_text(rss_content, encoding="utf-8")
        print("rss.xml updated.")

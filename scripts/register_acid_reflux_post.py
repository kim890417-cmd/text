import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Update blog.html
blog_file = REPO_DIR / "blog.html"
blog_content = blog_file.read_text(encoding="utf-8")

new_post_card = """<article class="post-411 post type-post status-publish format-standard has-post-thumbnail hentry ast-article-post" id="post-411">
  <div class="ast-post-format- has-post-thumbnail blog-layout-4 ast-article-inner">
    <div class="post-thumb-img-content">
		<a href="/health/acid-reflux-gerd-symptoms-diet-foods/">
			<img src="/health/acid-reflux-gerd-symptoms-diet-foods/thumbnail.png" alt="역류성 식도염 증상과 좋은 음식 피해야 할 음식, 목 이물감 없애는 식후 습관" loading="lazy">
		</a>
	</div>
    <div class="post-content ast-grid-common-col">
      <span class="ast-blog-single-element ast-taxonomy-container cat-links default"><a href="/blog" rel="category tag">건강,영양</a></span>
      <h2 class="entry-title ast-blog-single-element" itemprop="headline">
        <a href="/health/acid-reflux-gerd-symptoms-diet-foods/" rel="bookmark">역류성 식도염 증상과 좋은 음식 피해야 할 음식, 목 이물감 없애는 식후 습관</a>
      </h2>
      <header class="entry-header ast-blog-single-element ast-blog-meta-container">
        <div class="entry-meta"><span class="posted-by vcard author"><a title="건강노트의 모든 글 보기" href="/about" rel="author" class="url fn n"><span class="author-name">건강노트</span></a></span> / <span class="posted-on"><span class="published"> 10월 11, 2026 </span></span></div>
      </header>
      <div class="ast-excerpt-container ast-blog-single-element">
        <p>가슴 쓰림과 목 이물감, 신트림을 유발하는 역류성 식도염(GERD)의 원인과 하부식도괄약근 보호 원리, 양배추·바나나 등 위벽을 살리는 식단과 식후 3시간 생활수칙을 정리했습니다.</p>
      </div>
      <div style="font-size:0.82rem; color:#0284c7; font-weight:600; margin-top:4px;">
        연관 계산기: <a href="/caffeine" style="color:#0284c7; text-decoration:underline;">카페인 안전 섭취량</a> · <a href="/water" style="color:#0284c7; text-decoration:underline;">하루 물 섭취량</a>
      </div>
    </div>
  </div>
</article>
"""

if "acid-reflux-gerd-symptoms-diet-foods" not in blog_content:
    blog_content = blog_content.replace('<div class="ast-row">\n', f'<div class="ast-row">\n{new_post_card}\n', 1)
    blog_file.write_text(blog_content, encoding="utf-8")
    print("blog.html updated with acid reflux post.")

# 2. Update index.html
index_file = REPO_DIR / "index.html"
index_content = index_file.read_text(encoding="utf-8")

new_index_item = """          <!-- Article: 역류성 식도염 -->
          <a href="/health/acid-reflux-gerd-symptoms-diet-foods/" class="article-feed-item">
            <div class="article-feed-thumb">
              <img src="/health/acid-reflux-gerd-symptoms-diet-foods/thumbnail.png" alt="역류성 식도염 증상과 좋은 음식 피해야 할 음식" loading="lazy">
            </div>
            <div class="article-feed-content">
              <div class="article-feed-meta">
                <span class="article-feed-cat">위장·소화기</span>
                <span>5분 읽기 · 소화기학회 지침 기반</span>
              </div>
              <h3 class="article-feed-title">역류성 식도염 증상과 좋은 음식 피해야 할 음식, 목 이물감 없애는 식후 습관</h3>
              <p class="article-feed-excerpt">가슴 쓰림과 목 이물감을 유발하는 하부식도괄약근(LES) 이완 원인과 양배추·바나나 등 위벽 보호 식단, 식후 3시간 눕기 금지 생활수칙을 상세히 안내합니다.</p>
              <div class="article-feed-related">
                연관 도구: 카페인 안전 섭취량 · 하루 물 권장 섭취량
              </div>
            </div>
          </a>
"""

if "acid-reflux-gerd-symptoms-diet-foods" not in index_content:
    index_content = index_content.replace('9편 엄선', '10편 엄선')
    index_content = index_content.replace('<div class="article-feed">\n', f'<div class="article-feed">\n{new_index_item}\n', 1)
    index_file.write_text(index_content, encoding="utf-8")
    print("index.html updated with acid reflux magazine item.")

# 3. Update sitemap.xml
sitemap_file = REPO_DIR / "sitemap.xml"
if sitemap_file.exists():
    s_content = sitemap_file.read_text(encoding="utf-8")
    if "acid-reflux-gerd-symptoms-diet-foods" not in s_content:
        new_url = """  <url>
    <loc>https://healthfit100.com/health/acid-reflux-gerd-symptoms-diet-foods/</loc>
    <lastmod>2026-10-11T09:00:00+09:00</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
        s_content = s_content.replace('</urlset>', f'{new_url}</urlset>')
        sitemap_file.write_text(s_content, encoding="utf-8")
        print("sitemap.xml updated.")

# 4. Update rss.xml
rss_file = REPO_DIR / "rss.xml"
if rss_file.exists():
    r_content = rss_file.read_text(encoding="utf-8")
    if "acid-reflux-gerd-symptoms-diet-foods" not in r_content:
        new_item = """    <item>
      <title>역류성 식도염 증상과 좋은 음식 피해야 할 음식, 목 이물감 없애는 식후 습관</title>
      <link>https://healthfit100.com/health/acid-reflux-gerd-symptoms-diet-foods/</link>
      <guid>https://healthfit100.com/health/acid-reflux-gerd-symptoms-diet-foods/</guid>
      <pubDate>Sun, 11 Oct 2026 09:00:00 +0900</pubDate>
      <description><![CDATA[가슴 쓰림과 목 이물감, 신트림을 유발하는 역류성 식도염(GERD)의 원인과 하부식도괄약근 보호 원리, 양배추·바나나 등 위벽을 살리는 식단과 식후 3시간 생활수칙을 정리했습니다.]]></description>
    </item>
"""
        r_content = r_content.replace('<channel>\n', f'<channel>\n{new_item}\n', 1)
        rss_file.write_text(r_content, encoding="utf-8")
        print("rss.xml updated.")

# 5. Update all_40_english_urls.txt to all_41_english_urls.txt
all_urls_file = REPO_DIR / "all_40_english_urls.txt"
if all_urls_file.exists():
    all_urls_file.unlink()

items = re.findall(r'<item>\s*<title>(.*?)</title>\s*<link>(.*?)</link>', r_content, re.DOTALL)
with open("all_english_urls.txt", "w", encoding="utf-8") as f:
    for i, (t, l) in enumerate(items, 1):
        f.write(f"{i}. [{t.strip()}]\n{l.strip()}\n\n")
print(f"all_english_urls.txt updated with {len(items)} items.")

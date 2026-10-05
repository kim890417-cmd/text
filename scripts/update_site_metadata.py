import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Update blog.html
blog_path = REPO_DIR / "blog.html"
blog_content = blog_path.read_text(encoding="utf-8-sig")

blog_entries = """
<article class="post-402 post type-post status-publish format-standard hentry category-health ast-grid-common-col ast-full-width ast-article-post remove-featured-img-padding" id="post-402" itemtype="https://schema.org/CreativeWork" itemscope="itemscope">
		<div class="ast-post-format- ast-no-thumb blog-layout-4 ast-article-inner">
	<div class="post-content ast-grid-common-col">
		<span class="ast-blog-single-element ast-taxonomy-container cat-links default"><a href="/blog" rel="category tag">건강,영양</a></span><h2 class="entry-title ast-blog-single-element" itemprop="headline"><a href="https://healthfit100.com/health/blood-pressure-stages-hypertension-diet" rel="bookmark">고혈압 전단계 수치 기준과 낮추는 법, DASH 식단과 칼륨으로 나트륨 배출하기</a></h2>
		<header class="entry-header ast-blog-single-element ast-blog-meta-container">
			<div class="entry-meta"><span class="posted-by vcard author" itemtype="https://schema.org/Person" itemscope="itemscope" itemprop="author"><a title="건강노트의 모든 글 보기" href="https://healthfit100.com/about" rel="author" class="url fn n" itemprop="url"><span class="author-name" itemprop="name">건강노트</span></a></span> / <span class="posted-on"><span class="published" itemprop="datePublished"> 10월 5, 2026 </span></span></div>
		</header>
		<div class="ast-excerpt-container ast-blog-single-element"><p>수축기 120~139 mmHg 고혈압 전단계 수치 기준과 약 복용 전 3개월 혈압 낮추는 생활요법, DASH 식단 및 칼륨이 풍부한 나트륨 배출 음식을 체계적으로 안내합니다.</p></div>
		<div class="entry-content clear" itemprop="text"></div>
	</div>
</div>
	</article>
<article class="post-400 post type-post status-publish format-standard hentry category-health ast-grid-common-col ast-full-width ast-article-post remove-featured-img-padding" id="post-400" itemtype="https://schema.org/CreativeWork" itemscope="itemscope">
		<div class="ast-post-format- ast-no-thumb blog-layout-4 ast-article-inner">
	<div class="post-content ast-grid-common-col">
		<span class="ast-blog-single-element ast-taxonomy-container cat-links default"><a href="/blog" rel="category tag">건강,영양</a></span><h2 class="entry-title ast-blog-single-element" itemprop="headline"><a href="https://healthfit100.com/health/blood-sugar-spike-prevention-diet" rel="bookmark">식후 혈당 스파이크 증상과 낮추는 법, 거꾸로 식사법과 15분 걷기 효과</a></h2>
		<header class="entry-header ast-blog-single-element ast-blog-meta-container">
			<div class="entry-meta"><span class="posted-by vcard author" itemtype="https://schema.org/Person" itemscope="itemscope" itemprop="author"><a title="건강노트의 모든 글 보기" href="https://healthfit100.com/about" rel="author" class="url fn n" itemprop="url"><span class="author-name" itemprop="name">건강노트</span></a></span> / <span class="posted-on"><span class="published" itemprop="datePublished"> 10월 4, 2026 </span></span></div>
		</header>
		<div class="ast-excerpt-container ast-blog-single-element"><p>밥 먹고 쏟아지는 극심한 졸음의 원인 혈당 스파이크 기준(140 mg/dL), 식이섬유부터 먹는 거꾸로 식사법과 식후 15분 걷기가 인슐린에 미치는 과학적 효과를 정리했습니다.</p></div>
		<div class="entry-content clear" itemprop="text"></div>
	</div>
</div>
	</article>
<article class="post-398 post type-post status-publish format-standard hentry category-health ast-grid-common-col ast-full-width ast-article-post remove-featured-img-padding" id="post-398" itemtype="https://schema.org/CreativeWork" itemscope="itemscope">
		<div class="ast-post-format- ast-no-thumb blog-layout-4 ast-article-inner">
	<div class="post-content ast-grid-common-col">
		<span class="ast-blog-single-element ast-taxonomy-container cat-links default"><a href="/blog" rel="category tag">건강,영양</a></span><h2 class="entry-title ast-blog-single-element" itemprop="headline"><a href="https://healthfit100.com/health/vitamin-d-benefits-daily-intake-timing" rel="bookmark">비타민D 복용시간과 하루 권장량, 마그네슘과 함께 먹어야 하는 이유</a></h2>
		<header class="entry-header ast-blog-single-element ast-blog-meta-container">
			<div class="entry-meta"><span class="posted-by vcard author" itemtype="https://schema.org/Person" itemscope="itemscope" itemprop="author"><a title="건강노트의 모든 글 보기" href="https://healthfit100.com/about" rel="author" class="url fn n" itemprop="url"><span class="author-name" itemprop="name">건강노트</span></a></span> / <span class="posted-on"><span class="published" itemprop="datePublished"> 10월 3, 2026 </span></span></div>
		</header>
		<div class="ast-excerpt-container ast-blog-single-element"><p>한국인 80%가 겪는 비타민D 결핍 기준(30 ng/mL), 지용성 흡수율을 높이는 점심 식후 복용법, 성인 1000~2000 IU 하루 권장량과 마그네슘 결합 이유를 정리했습니다.</p></div>
		<div class="entry-content clear" itemprop="text"></div>
	</div>
</div>
	</article>
"""

if '<div class="ast-row">' in blog_content:
    blog_content = blog_content.replace('<div class="ast-row">', f'<div class="ast-row">{blog_entries}', 1)
    blog_path.write_text(blog_content, encoding="utf-8")
    print("Updated blog.html")

# 2. Update index.html
index_path = REPO_DIR / "index.html"
index_content = index_path.read_text(encoding="utf-8-sig")

home_cards = """
        <!-- New Post 1: Blood Pressure -->
        <article class="custom-card-list-item">
          <a href="/health/blood-pressure-stages-hypertension-diet/" class="custom-card-thumb-link" aria-label="고혈압 전단계 수치 기준과 낮추는 법">
            <img src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400&h=260&fit=crop&q=80" alt="고혈압 전단계 수치와 DASH 식단" loading="lazy">
          </a>
          <div class="custom-card-body">
            <div class="custom-card-meta">
              <span class="custom-card-category">혈압·혈관</span>
              <span>5분 읽기 · 대한고혈압학회 지침 기반</span>
            </div>
            <h3 class="custom-card-title">
              <a href="/health/blood-pressure-stages-hypertension-diet/">고혈압 전단계 수치 기준과 낮추는 법, DASH 식단과 칼륨으로 나트륨 배출하기</a>
            </h3>
            <p class="custom-card-excerpt">
              수축기 120~139 mmHg 고혈압 전단계 수치 판정 기준과 혈압약 복용 전 실천하는 3개월 생활요법, 나트륨-칼륨 펌프 원리를 활용한 배출 식단과 DASH 식단을 상세히 정리했습니다.
            </p>
          </div>
        </article>

        <!-- New Post 2: Blood Sugar Spike -->
        <article class="custom-card-list-item">
          <a href="/health/blood-sugar-spike-prevention-diet/" class="custom-card-thumb-link" aria-label="식후 혈당 스파이크 증상과 낮추는 법">
            <img src="https://images.unsplash.com/photo-1505576399279-565b52d4ac71?w=400&h=260&fit=crop&q=80" alt="혈당 스파이크 증상과 식단 관리" loading="lazy">
          </a>
          <div class="custom-card-body">
            <div class="custom-card-meta">
              <span class="custom-card-category">혈당·당뇨</span>
              <span>5분 읽기 · 대한당뇨병학회 자료 기반</span>
            </div>
            <h3 class="custom-card-title">
              <a href="/health/blood-sugar-spike-prevention-diet/">식후 혈당 스파이크 증상과 낮추는 법, 거꾸로 식사법과 15분 걷기 효과</a>
            </h3>
            <p class="custom-card-excerpt">
              식후 쏟아지는 극심한 피로와 졸음의 주원인인 혈당 스파이크 기준(140 mg/dL), 식이섬유부터 먹는 거꾸로 식사법과 식후 15분 대근육 걷기 운동의 인슐린 안정 효과를 과학적으로 설명합니다.
            </p>
          </div>
        </article>

        <!-- New Post 3: Vitamin D -->
        <article class="custom-card-list-item">
          <a href="/health/vitamin-d-benefits-daily-intake-timing/" class="custom-card-thumb-link" aria-label="비타민D 복용시간과 하루 권장량">
            <img src="https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=400&h=260&fit=crop&q=80" alt="비타민D 영양제 복용법과 권장량" loading="lazy">
          </a>
          <div class="custom-card-body">
            <div class="custom-card-meta">
              <span class="custom-card-category">영양제</span>
              <span>5분 읽기 · 보건복지부 섭취기준 기반</span>
            </div>
            <h3 class="custom-card-title">
              <a href="/health/vitamin-d-benefits-daily-intake-timing/">비타민D 복용시간과 하루 권장량, 마그네슘과 함께 먹어야 하는 이유</a>
            </h3>
            <p class="custom-card-excerpt">
              한국인의 80%가 겪는 비타민D 결핍 혈중 수치 기준과 지용성 흡수율을 50% 높이는 점심 식후 복용법, 1000~2000 IU 적정 권장량 및 마그네슘·비타민K2와의 필수 시너지를 정리했습니다.
            </p>
          </div>
        </article>
"""

marker = '<div style="display:flex;flex-direction:column;gap:18px;margin-bottom:55px;">'
if marker in index_content:
    index_content = index_content.replace(marker, f'{marker}\n{home_cards}', 1)
    index_path.write_text(index_content, encoding="utf-8")
    print("Updated index.html")

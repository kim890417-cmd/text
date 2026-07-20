import os
import re

repo_path = r'C:\Users\User\Desktop\키워드 글쓰기\healthfit_repo'

THUMB_MAP = {
    '아연-효능': ('https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=500&h=300&fit=crop&q=80', '아연 효능과 하루 권장량'),
    '단백질-하루-섭취량': ('https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=500&h=300&fit=crop&q=80', '단백질 하루 섭취량 계산법'),
    '철분제-효능': ('https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=500&h=300&fit=crop&q=80', '철분제 효능과 빈혈 예방'),
    '잠-잘-오는-음식': ('https://images.unsplash.com/photo-1541480601022-2308c0f02487?w=500&h=300&fit=crop&q=80', '잠 잘 오는 음식과 멜라토닌'),
    '눈-뻑뻑함': ('https://images.unsplash.com/photo-1576678927484-cc907957088c?w=500&h=300&fit=crop&q=80', '루테인 철분제 복용법'),
    '멀티비타민': ('https://images.unsplash.com/photo-1516997121675-4c2d1684aa3e?w=500&h=300&fit=crop&q=80', '멀티비타민 복용 시간'),
    '칼슘-하루': ('https://images.unsplash.com/photo-1563636619-e9143da7973b?w=500&h=300&fit=crop&q=80', '칼슘 하루 권장 섭취량'),
    '마그네슘-하루': ('https://images.unsplash.com/photo-1498557850523-fd3d118b962e?w=500&h=300&fit=crop&q=80', '마그네슘 하루 권장량'),
    '단백질-권장량': ('https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=500&h=300&fit=crop&q=80', '단백질 권장량'),
    '근육-유지': ('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&h=300&fit=crop&q=80', '근육 유지와 다이어트 단백질'),
    'tdee': ('https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=500&h=300&fit=crop&q=80', 'TDEE 계산하는 법'),
    '오메가3': ('https://images.unsplash.com/photo-1519682577862-22b62b24e493?w=500&h=300&fit=crop&q=80', '오메가3 복용시간'),
    '다이어트를-하는-분들': ('https://images.unsplash.com/photo-1535914254981-b5012eebbd15?w=500&h=300&fit=crop&q=80', '다이어트 체중 관리'),
    '기초대사량-계산': ('https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=500&h=300&fit=crop&q=80', '기초대사량 계산법'),
    '여자-적정-체중': ('https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=500&h=300&fit=crop&q=80', '여자 적정 체중'),
    '영양제-상한': ('https://images.unsplash.com/photo-1587854680352-936b22b91030?w=500&h=300&fit=crop&q=80', '영양제 상한 섭취량'),
    '소주-주량': ('https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&h=300&fit=crop&q=80', '소주 주량 계산'),
    '임산부-엽산': ('https://images.unsplash.com/photo-1476703993599-0035a21b17a9?w=500&h=300&fit=crop&q=80', '임산부 엽산 권장량'),
    '서브웨이-칼로리': ('https://images.unsplash.com/photo-1509722747041-616f39b57569?w=500&h=300&fit=crop&q=80', '서브웨이 칼로리'),
    '스타벅스-칼로리': ('https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=500&h=300&fit=crop&q=80', '스타벅스 칼로리'),
    '와인칼로리': ('https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=500&h=300&fit=crop&q=80', '와인 칼로리'),
    '임산부-체중증가': ('https://images.unsplash.com/photo-1491013516836-7db643ee125a?w=500&h=300&fit=crop&q=80', '임산부 체중 증가'),
    '생리주기': ('https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?w=500&h=300&fit=crop&q=80', '생리주기 계산법'),
    '운동-소모-칼로리': ('https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500&h=300&fit=crop&q=80', '운동 소모 칼로리'),
    'bmi-계산법': ('https://images.unsplash.com/photo-1576678927484-cc907957088c?w=500&h=300&fit=crop&q=80', 'BMI 계산법'),
    '하루-물-섭취량': ('https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=500&h=300&fit=crop&q=80', '하루 물 섭취량'),
    '하루-카페인': ('https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=500&h=300&fit=crop&q=80', '하루 카페인 권장량'),
    '헬스장-트레이너': ('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&h=300&fit=crop&q=80', '헬스장 트레이너'),
}

DEFAULT_THUMB = ('https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=500&h=300&fit=crop&q=80', '건강노트 블로그')

def get_thumb(title, url):
    for key, (img, alt) in THUMB_MAP.items():
        if key in url or key in title:
            return img, alt
    return DEFAULT_THUMB

# Clean global override CSS to ensure 100% perfect flex layout
CLEAN_CSS = '''<style id="clean-left-thumb-list-css">
/* 그리드 무효화 및 1열 리스트 레이아웃 강제 */
.ast-blog-layout-4-grid .ast-row {
  display: flex !important;
  flex-direction: column !important;
  gap: 16px !important;
  margin: 0 !important;
}

.ast-blog-layout-4-grid .ast-article-post {
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 0 16px 0 !important;
  padding: 0 !important;
  float: none !important;
}

.custom-card-list-item {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  gap: 20px !important;
  padding: 16px 20px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 12px !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease !important;
  box-sizing: border-box !important;
}

.custom-card-list-item:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08) !important;
  border-color: #cbd5e1 !important;
}

.custom-card-thumb-link {
  flex-shrink: 0 !important;
  width: 200px !important;
  height: 130px !important;
  border-radius: 8px !important;
  overflow: hidden !important;
  display: block !important;
  background: #f1f5f9 !important;
}

.custom-card-thumb-link img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  display: block !important;
  transition: transform 0.3s ease !important;
}

.custom-card-list-item:hover .custom-card-thumb-link img {
  transform: scale(1.05) !important;
}

.custom-card-body {
  flex: 1 !important;
  min-width: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 6px !important;
}

.custom-card-meta {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  font-size: 13px !important;
  color: #64748b !important;
}

.custom-card-category {
  background: #eff6ff !important;
  color: #1d4ed8 !important;
  padding: 2px 8px !important;
  border-radius: 4px !important;
  font-weight: 600 !important;
  font-size: 12px !important;
  text-decoration: none !important;
  white-space: nowrap !important;
}

.custom-card-title {
  margin: 0 !important;
  font-size: 1.15rem !important;
  font-weight: 700 !important;
  line-height: 1.4 !important;
}

.custom-card-title a {
  color: #0f172a !important;
  text-decoration: none !important;
}

.custom-card-title a:hover {
  color: #046bd2 !important;
}

.custom-card-excerpt {
  margin: 0 !important;
  font-size: 0.92rem !important;
  color: #475569 !important;
  line-height: 1.5 !important;
  display: -webkit-box !important;
  -webkit-line-clamp: 2 !important;
  -webkit-box-orient: vertical !important;
  overflow: hidden !important;
}

@media (max-width: 640px) {
  .custom-card-list-item {
    flex-direction: column !important;
    align-items: flex-start !important;
  }
  .custom-card-thumb-link {
    width: 100% !important;
    height: 170px !important;
  }
}
</style>
'''

target_list_files = [
    'blog.html',
    'index.html',
    r'author\kim890417\index.html',
    r'author\kim890417\page\2\index.html',
    r'author\kim890417\page\3\index.html',
    r'category\health\index.html',
    r'category\health\page\2\index.html',
    r'category\health\page\3\index.html',
    r'category\uncategorized\index.html',
    r'page\2\index.html',
    r'page\3\index.html',
    r'sample-page\index.html',
]

def reformat_article(art_match):
    art_html = art_match.group(0)
    
    # Extract post URL & Title
    m_title = re.search(r'<h2[^>]*class="[^"]*entry-title[^"]*"[^>]*>\s*<a\s+href="([^"]+)"[^>]*>(.*?)</a>', art_html, re.DOTALL)
    if not m_title:
        return art_html
    
    post_url = m_title.group(1).strip()
    post_title = m_title.group(2).strip()
    
    # Extract date
    m_date = re.search(r'<span class="published"[^>]*>(.*?)</span>', art_html, re.DOTALL)
    date_str = m_date.group(1).strip() if m_date else '7월 20, 2026'
    
    # Extract category
    m_cat = re.search(r'<span class="ast-blog-single-element ast-taxonomy-container[^"]*">(.*?)</span>', art_html, re.DOTALL)
    cat_str = '건강,영양'
    if m_cat:
        m_cat_link = re.search(r'<a[^>]*>(.*?)</a>', m_cat.group(1))
        if m_cat_link:
            cat_str = m_cat_link.group(1).strip()
            
    # Extract excerpt
    m_exc = re.search(r'<div class="ast-excerpt-container[^"]*">\s*<p>(.*?)</p>\s*</div>', art_html, re.DOTALL)
    excerpt_str = m_exc.group(1).strip() if m_exc else ''
    
    img_url, img_alt = get_thumb(post_title, post_url)
    
    card_html = f'''<article class="post-345 post type-post status-publish format-standard hentry category-health ast-grid-common-col ast-full-width ast-article-post" style="width:100%;margin-bottom:16px;">
  <div class="custom-card-list-item">
    <a href="{post_url}" class="custom-card-thumb-link">
      <img src="{img_url}" alt="{img_alt}" loading="lazy">
    </a>
    <div class="custom-card-body">
      <div class="custom-card-meta">
        <span class="custom-card-category">{cat_str}</span>
        <span>•</span>
        <span>건강노트</span>
        <span>•</span>
        <span>{date_str}</span>
      </div>
      <h2 class="custom-card-title">
        <a href="{post_url}">{post_title}</a>
      </h2>
      <p class="custom-card-excerpt">{excerpt_str}</p>
    </div>
  </div>
</article>'''
    return card_html

updated = 0
for rel_path in target_list_files:
    full_path = os.path.join(repo_path, rel_path)
    if not os.path.exists(full_path):
        continue

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old custom css if present
    content = re.sub(r'<style id="custom-left-thumb-list-css">.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style id="clean-left-thumb-list-css">.*?</style>', '', content, flags=re.DOTALL)

    # Insert clean CSS in head
    if '</head>' in content:
        content = content.replace('</head>', CLEAN_CSS + '\n</head>', 1)

    # Replace all <article ...>...</article> tags
    content = re.sub(r'<article class="[^"]*ast-article-post[^"]*".*?</article>', reformat_article, content, flags=re.DOTALL)

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    updated += 1
    print(f'[REFORMATTED] {rel_path}')

print(f'\n총 {updated}개 페이지 완벽 리스트 뷰 구조 교체 완료!')

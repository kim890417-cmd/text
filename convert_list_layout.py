import os
import re

repo_path = r'C:\Users\User\Desktop\키워드 글쓰기\healthfit_repo'

# Map post URL keywords to thumbnail image URLs & ALT
THUMB_MAP = {
    '아연-효능': (
        'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=500&h=300&fit=crop&q=80',
        '아연 효능과 하루 권장량'
    ),
    '단백질-하루-섭취량': (
        'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=500&h=300&fit=crop&q=80',
        '단백질 하루 섭취량 계산법'
    ),
    '철분제-효능': (
        'https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=500&h=300&fit=crop&q=80',
        '철분제 효능과 빈혈 예방'
    ),
    '잠-잘-오는-음식': (
        'https://images.unsplash.com/photo-1541480601022-2308c0f02487?w=500&h=300&fit=crop&q=80',
        '잠 잘 오는 음식과 멜라토닌'
    ),
    '눈-뻑뻑함': (
        'https://images.unsplash.com/photo-1576678927484-cc907957088c?w=500&h=300&fit=crop&q=80',
        '루테인 철분제 복용법'
    ),
    '멀티비타민': (
        'https://images.unsplash.com/photo-1516997121675-4c2d1684aa3e?w=500&h=300&fit=crop&q=80',
        '멀티비타민 복용 시간'
    ),
    '칼슘-하루': (
        'https://images.unsplash.com/photo-1563636619-e9143da7973b?w=500&h=300&fit=crop&q=80',
        '칼슘 하루 권장 섭취량'
    ),
    '마그네슘-하루': (
        'https://images.unsplash.com/photo-1498557850523-fd3d118b962e?w=500&h=300&fit=crop&q=80',
        '마그네슘 하루 권장량'
    ),
    '단백질-권장량': (
        'https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=500&h=300&fit=crop&q=80',
        '단백질 권장량'
    ),
    '근육-유지': (
        'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&h=300&fit=crop&q=80',
        '근육 유지와 다이어트 단백질'
    ),
    'tdee': (
        'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=500&h=300&fit=crop&q=80',
        'TDEE 계산하는 법'
    ),
    '오메가3': (
        'https://images.unsplash.com/photo-1519682577862-22b62b24e493?w=500&h=300&fit=crop&q=80',
        '오메가3 복용시간'
    ),
    '다이어트를-하는-분들': (
        'https://images.unsplash.com/photo-1535914254981-b5012eebbd15?w=500&h=300&fit=crop&q=80',
        '다이어트 체중 관리'
    ),
    '기초대사량-계산': (
        'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=500&h=300&fit=crop&q=80',
        '기초대사량 계산법'
    ),
    '여자-적정-체중': (
        'https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=500&h=300&fit=crop&q=80',
        '여자 적정 체중'
    ),
    '영양제-상한': (
        'https://images.unsplash.com/photo-1587854680352-936b22b91030?w=500&h=300&fit=crop&q=80',
        '영양제 상한 섭취량'
    ),
    '소주-주량': (
        'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&h=300&fit=crop&q=80',
        '소주 주량 계산'
    ),
    '임산부-엽산': (
        'https://images.unsplash.com/photo-1476703993599-0035a21b17a9?w=500&h=300&fit=crop&q=80',
        '임산부 엽산 권장량'
    ),
    '서브웨이-칼로리': (
        'https://images.unsplash.com/photo-1509722747041-616f39b57569?w=500&h=300&fit=crop&q=80',
        '서브웨이 칼로리'
    ),
    '스타벅스-칼로리': (
        'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=500&h=300&fit=crop&q=80',
        '스타벅스 칼로리'
    ),
    '와인칼로리': (
        'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=500&h=300&fit=crop&q=80',
        '와인 칼로리'
    ),
    '임산부-체중증가': (
        'https://images.unsplash.com/photo-1491013516836-7db643ee125a?w=500&h=300&fit=crop&q=80',
        '임산부 체중 증가'
    ),
    '생리주기': (
        'https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?w=500&h=300&fit=crop&q=80',
        '생리주기 계산법'
    ),
    '운동-소모-칼로리': (
        'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500&h=300&fit=crop&q=80',
        '운동 소모 칼로리'
    ),
    'bmi-계산법': (
        'https://images.unsplash.com/photo-1576678927484-cc907957088c?w=500&h=300&fit=crop&q=80',
        'BMI 계산법'
    ),
    '하루-물-섭취량': (
        'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=500&h=300&fit=crop&q=80',
        '하루 물 섭취량'
    ),
    '하루-카페인': (
        'https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=500&h=300&fit=crop&q=80',
        '하루 카페인 권장량'
    ),
    '헬스장-트레이너': (
        'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&h=300&fit=crop&q=80',
        '헬스장 트레이너'
    ),
}

DEFAULT_THUMB = (
    'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=500&h=300&fit=crop&q=80',
    '건강노트 블로그'
)

# Custom CSS for Left Thumbnail Layout
LEFT_THUMB_CSS = '''<style id="custom-left-thumb-list-css">
/* 블로그 목록: 왼쪽에 썸네일, 오른쪽에 제목/글 정보 배치 */
.ast-blog-layout-4-grid .ast-row {
  display: flex !important;
  flex-direction: column !important;
  gap: 20px !important;
}

.ast-blog-layout-4-grid .ast-article-post {
  width: 100% !important;
  max-width: 100% !important;
  margin-bottom: 0 !important;
  padding: 0 !important;
}

.ast-blog-layout-4-grid .ast-article-inner {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  padding: 20px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 12px !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

.ast-blog-layout-4-grid .ast-article-inner:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08) !important;
}

.ast-blog-layout-4-grid .post-content {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  width: 100% !important;
  gap: 24px !important;
}

.ast-blog-layout-4-grid .ast-blog-featured-section.post-thumb {
  width: 220px !important;
  min-width: 220px !important;
  height: 140px !important;
  flex-shrink: 0 !important;
  margin: 0 !important;
  border-radius: 8px !important;
  overflow: hidden !important;
  background: #f1f5f9 !important;
}

.ast-blog-layout-4-grid .ast-blog-featured-section.post-thumb img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  display: block !important;
  transition: transform 0.3s ease !important;
}

.ast-blog-layout-4-grid .ast-article-inner:hover .ast-blog-featured-section.post-thumb img {
  transform: scale(1.05) !important;
}

.ast-blog-layout-4-grid .entry-title {
  font-size: 1.25rem !important;
  font-weight: 700 !important;
  margin-top: 6px !important;
  margin-bottom: 8px !important;
  line-height: 1.4 !important;
}

.ast-blog-layout-4-grid .entry-title a {
  color: #0f172a !important;
  text-decoration: none !important;
}

.ast-blog-layout-4-grid .entry-title a:hover {
  color: #046bd2 !important;
}

.ast-blog-layout-4-grid .ast-excerpt-container p {
  margin: 0 !important;
  color: #475569 !important;
  font-size: 0.95rem !important;
  line-height: 1.6 !important;
  display: -webkit-box !important;
  -webkit-line-clamp: 2 !important;
  -webkit-box-orient: vertical !important;
  overflow: hidden !important;
}

@media (max-width: 640px) {
  .ast-blog-layout-4-grid .ast-article-inner,
  .ast-blog-layout-4-grid .post-content {
    flex-direction: column !important;
    align-items: flex-start !important;
  }
  .ast-blog-layout-4-grid .ast-blog-featured-section.post-thumb {
    width: 100% !important;
    min-width: 100% !important;
    height: 180px !important;
  }
}
</style>
'''

# List of list HTML files to update
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

def find_thumb_for_post(post_html):
    # Match post URL in <h2 class="entry-title..."><a href="...">
    m = re.search(r'<h2 class="entry-title[^"]*"[^>]*><a href="([^"]+)"', post_html)
    if m:
        url = m.group(1)
        for key, (img_url, alt) in THUMB_MAP.items():
            if key in url or key in url.lower():
                return img_url, alt, url
        return DEFAULT_THUMB[0], DEFAULT_THUMB[1], url
    return DEFAULT_THUMB[0], DEFAULT_THUMB[1], ''

updated_files_count = 0

for rel_path in target_list_files:
    full_path = os.path.join(repo_path, rel_path)
    if not os.path.exists(full_path):
        continue

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add custom CSS before </head>
    if '</head>' in content and 'id="custom-left-thumb-list-css"' not in content:
        content = content.replace('</head>', LEFT_THUMB_CSS + '\n</head>', 1)

    # Process each article tag to inject thumbnail
    articles = re.findall(r'<article class="[^"]*ast-article-post[^"]*".*?</article>', content, re.DOTALL)
    
    modified_in_file = False
    for art_html in articles:
        img_url, alt, post_url = find_thumb_for_post(art_html)
        
        # Target: <div class="ast-blog-featured-section post-thumb ast-blog-single-element"></div>
        empty_thumb_tag = '<div class="ast-blog-featured-section post-thumb ast-blog-single-element"></div>'
        new_thumb_tag = f'<div class="ast-blog-featured-section post-thumb ast-blog-single-element"><a href="{post_url}"><img src="{img_url}" alt="{alt}" loading="lazy"></a></div>'
        
        if empty_thumb_tag in art_html:
            new_art_html = art_html.replace(empty_thumb_tag, new_thumb_tag, 1)
            content = content.replace(art_html, new_art_html, 1)
            modified_in_file = True

    if modified_in_file or 'id="custom-left-thumb-list-css"' in content:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_files_count += 1
        print(f'[DONE] Updated list layout & thumbs: {rel_path}')

print(f'\n총 {updated_files_count}개 목록 페이지 왼쪽 썸네일형 레이아웃 변환 완료!')

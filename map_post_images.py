import os
import re
from urllib.parse import unquote

repo_path = r'C:\Users\User\Desktop\키워드 글쓰기\healthfit_repo'
health_dir = os.path.join(repo_path, 'health')

# Map each post folder / url slug to its exact featured image URL
POST_EXACT_IMG = {}

for folder in os.listdir(health_dir):
    folder_path = os.path.join(health_dir, folder)
    if os.path.isdir(folder_path):
        html_file = os.path.join(folder_path, 'index.html')
        if os.path.exists(html_file):
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Find the figure or img src inside the post
            m = re.search(r'class="post-thumb-img-content".*?<img\s+src="([^"]+)"', content, re.DOTALL)
            if not m:
                m = re.search(r'<img\s+[^>]*src="([^"]+)"', content, re.DOTALL)

            if m:
                img_url = m.group(1)
                POST_EXACT_IMG[folder] = img_url
                print(f'Mapped [{folder[:30]}] -> {img_url[:70]}')

print(f'\n총 {len(POST_EXACT_IMG)}개 포스팅 정밀 이미지 매핑 성공!')

# Now update all archive list pages
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

def update_article_img(art_match):
    art_html = art_match.group(0)
    
    # Find post URL
    m_url = re.search(r'href="([^"]*health/[^"]*)"', art_html)
    if not m_url:
        return art_html
        
    full_url = m_url.group(1)
    
    # Extract folder slug from full_url
    # e.g. https://healthfit100.com/health/서브웨이-칼로리/ -> 서브웨이-칼로리
    unquoted_url = unquote(full_url)
    slug = unquoted_url.rstrip('/').split('/')[-1]
    
    # Find exact image for this slug
    matched_img = None
    for folder, img_url in POST_EXACT_IMG.items():
        if folder == slug or folder in unquoted_url or unquote(folder) == slug:
            matched_img = img_url
            break
            
    if matched_img:
        # Replace the img src inside custom-card-thumb-link
        art_html = re.sub(r'(<a\s+href="[^"]*"\s+class="custom-card-thumb-link">\s*<img\s+src=")[^"]+(")', r'\g<1>' + matched_img + r'\g<2>', art_html)

    return art_html

updated_count = 0
for rel_path in target_list_files:
    full_path = os.path.join(repo_path, rel_path)
    if not os.path.exists(full_path):
        continue

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(r'<article class="[^"]*ast-article-post[^"]*".*?</article>', update_article_img, content, flags=re.DOTALL)

    if new_content != content:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1
        print(f'[UPDATED] {rel_path}')

print(f'\n총 {updated_count}개 목록 페이지의 썸네일을 실제 본문 이미지로 1:1 완벽 교체 완료!')

import re
import os
import urllib.parse

def main():
    with open('blog.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Pattern to match <article ...> blocks
    article_pattern = re.compile(r'(<article\s+class=[\'"][^\'"]*ast-article-post[^\'"]*[\'"][^>]*>)(.*?)(</article>)', re.DOTALL)

    updated_count = 0

    def replace_article(match):
        nonlocal updated_count
        open_tag = match.group(1)
        body = match.group(2)
        close_tag = match.group(3)

        # Check if already has img
        if '<img ' in body:
            return match.group(0)

        # Find link in headline
        link_match = re.search(r'<h2[^>]*>\s*<a\s+href=[\'"]([^\'"]+)[\'"]', body)
        if not link_match:
            return match.group(0)

        href = link_match.group(1)
        # Parse path
        path = href.replace('https://healthfit100.com', '').strip('/')
        # e.g. health/fasting-cardio-fat-loss-timing
        parts = path.split('/')
        if len(parts) >= 2 and parts[0] == 'health':
            slug = parts[1]
            # decode url if percent-encoded
            decoded_slug = urllib.parse.unquote(slug)
            
            # check if folder exists in health/
            local_folder = os.path.join('health', decoded_slug)
            if not os.path.exists(local_folder):
                local_folder = os.path.join('health', slug)

            thumb_file = os.path.join(local_folder, 'thumbnail.png')
            if os.path.exists(thumb_file):
                web_thumb_path = f"/{local_folder.replace(os.sep, '/')}/thumbnail.png"
                
                # Get title for alt
                title_match = re.search(r'<h2[^>]*><a[^>]*>(.*?)</a></h2>', body)
                alt_text = title_match.group(1) if title_match else "건강 칼럼 썸네일"

                thumb_html = f'''<div class="post-thumb-img-content" style="border-radius:8px; overflow:hidden; margin-bottom:12px;">
		<a href="{href}">
			<img src="{web_thumb_path}" alt="{alt_text}" width="100%" style="width:100%; height:auto; aspect-ratio:1200/630; object-fit:cover; display:block; border-radius:8px;">
		</a>
	</div>\n\t'''
                # Insert inside ast-article-inner before post-content
                if '<div class="post-content' in body:
                    body = body.replace('<div class="post-content', thumb_html + '<div class="post-content', 1)
                    body = body.replace('ast-no-thumb', 'has-post-thumbnail')
                    updated_count += 1

        return open_tag + body + close_tag

    new_html = article_pattern.sub(replace_article, html)

    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"Updated {updated_count} cards in blog.html with thumbnails!")

if __name__ == '__main__':
    main()

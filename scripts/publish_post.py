import os
import re
from datetime import datetime

ROOT = r"c:\Users\User\Documents\GitHub\text"
DRAFT_FILE = os.path.join(ROOT, "drafts", "철분제 효능과 빈혈 증상 예방 가이드 복용 시 주의할 음식 및 부작용.txt")
TEMPLATE_POST = os.path.join(ROOT, "health", "눈-뻑뻑함과-계단-어지러움-루테인과-철분제-낭비-없", "index.html")

def parse_draft(filepath):
    metadata = {}
    body_lines = []
    in_body = False
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if not in_body:
                if line_str.startswith("[제목]"):
                    metadata["title"] = line_str.replace("[제목]", "").strip()
                elif line_str.startswith("[카테고리]"):
                    metadata["category"] = line_str.replace("[카테고리]", "").strip()
                elif line_str.startswith("[태그]"):
                    metadata["tags"] = [t.strip() for t in line_str.replace("[태그]", "").split(",")]
                elif line_str.startswith("[설명]"):
                    metadata["desc"] = line_str.replace("[설명]", "").strip()
                elif line_str.startswith("[발행일]"):
                    metadata["date"] = line_str.replace("[발행일]", "").strip()
                elif line_str.startswith("[본문]"):
                    in_body = True
            else:
                body_lines.append(line.rstrip())
                
    date_str = metadata.get("date", "")
    if not date_str:
        now = datetime.now()
        metadata["pub_time"] = now.strftime("%Y-%m-%dT%H:%M:%S+09:00")
        metadata["display_date"] = f"{now.month}월 {now.day}, {now.year}"
        metadata["short_date"] = now.strftime("%Y-%m-%d")
    else:
        parsed = None
        for fmt in ("%Y-%m-%d-%H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
            try:
                parsed = datetime.strptime(date_str, fmt)
                break
            except ValueError:
                continue
        if parsed:
            metadata["pub_time"] = parsed.strftime("%Y-%m-%dT%H:%M:%S+09:00")
            metadata["display_date"] = f"{parsed.month}월 {parsed.day}, {parsed.year}"
            metadata["short_date"] = parsed.strftime("%Y-%m-%d")
        else:
            now = datetime.now()
            metadata["pub_time"] = now.strftime("%Y-%m-%dT%H:%M:%S+09:00")
            metadata["display_date"] = f"{now.month}월 {now.day}, {now.year}"
            metadata["short_date"] = now.strftime("%Y-%m-%d")
            
    return metadata, body_lines

def convert_body_to_html(lines):
    html_blocks = []
    current_list = []
    
    def close_list():
        if current_list:
            items_html = "\n".join(f"<li>{item}</li>" for item in current_list)
            html_blocks.append(f'<ul class="wp-block-list">\n{items_html}\n</ul>')
            current_list.clear()
            
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            close_list()
            i += 1
            continue
            
        # Headers explicitly with #
        if line.startswith("# "):
            close_list()
            h_text = line[2:].strip()
            h_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", h_text)
            html_blocks.append(f'<h2 class="wp-block-heading">{h_text}</h2>')
        elif line.startswith("## "):
            close_list()
            h_text = line[3:].strip()
            h_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", h_text)
            html_blocks.append(f'<h3 class="wp-block-heading">{h_text}</h3>')
        # Numbered headers: e.g. "1. 빈혈의 정확한 정의..."
        elif re.match(r"^\d+\.\s+", line):
            close_list()
            h_text = line.strip()
            h_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", h_text)
            html_blocks.append(f'<h2 class="wp-block-heading">{h_text}</h2>')
        # Lists
        elif line.startswith("- "):
            item_text = line[2:].strip()
            item_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", item_text)
            current_list.append(item_text)
        # Check subheaders/list items like "제1철 (황산철...):" or "카페인 및 타닌..."
        # If it's a short line ending with ":" or "：" or has bold title at start, let's treat it as a strong paragraph or h3
        elif (line.endswith(":") or line.endswith("：")) and len(line) < 100:
            close_list()
            h_text = line.strip()
            h_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", h_text)
            html_blocks.append(f'<h3 class="wp-block-heading">{h_text}</h3>')
        # Paragraphs
        else:
            close_list()
            p_text = line.strip()
            p_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", p_text)
            html_blocks.append(f'<p class="wp-block-paragraph">{p_text}</p>')
        i += 1
        
    close_list()
    return "\n\n".join(html_blocks)

def publish():
    print("Parsing draft...")
    metadata, body_lines = parse_draft(DRAFT_FILE)
    body_html = convert_body_to_html(body_lines)
    
    slug = "철분제-효능과-빈혈-증상-예방-가이드-복용-시-주의할-음식-및-부작용"
    post_dir = os.path.join(ROOT, "health", slug)
    os.makedirs(post_dir, exist_ok=True)
    
    print(f"Slug: {slug}")
    print(f"Title: {metadata['title']}")
    print(f"Date: {metadata['pub_time']}")
    
    with open(TEMPLATE_POST, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    new_html = template_content
    old_title = "눈 뻑뻑함과 계단 어지러움: 루테인과 철분제 낭비 없는 식후 복용 법칙"
    new_title = metadata["title"]
    
    new_html = new_html.replace(f"{old_title} - 건강노트", f"{new_title} - 건강노트")
    new_html = new_html.replace(old_title, new_title)
    
    old_desc = "하루의 절반 이상을 모니터와 씨름하는 현대인들에게 가장 절실한 루테인과 철분제의 핵심 효능, 그리고 돈 버리지 않고 온전히 흡수시키는 현실적인 복용법을 날것 그대로 정리해 드립니다."
    new_desc = metadata["desc"]
    new_html = new_html.replace(old_desc, new_desc)
    
    old_slug = "눈-뻑뻑함과-계단-어지러움-루테인과-철분제-낭비-없"
    new_html = new_html.replace(old_slug, slug)
    
    new_html = re.sub(r'2026-07-13T14:10:28\+00:00', metadata["pub_time"], new_html)
    new_html = re.sub(r'2026-07-13T14:10:32\+00:00', metadata["pub_time"], new_html)
    new_html = re.sub(r'7월 13, 2026', metadata["display_date"], new_html)
    new_html = re.sub(r'"datePublished"\s*:\s*"[^"]+"', f'"datePublished":"{metadata["pub_time"]}"', new_html)
    new_html = re.sub(r'"dateModified"\s*:\s*"[^"]+"', f'"dateModified":"{metadata["pub_time"]}"', new_html)
    
    new_html = new_html.replace('post-345', 'post-350')
    new_html = new_html.replace('postid-345', 'postid-350')
    
    tag_lines = [f'<meta property="article:tag" content="{tag}">' for tag in metadata["tags"]]
    tag_block = "\n".join(tag_lines)
    new_html = re.sub(r'(<meta property="article:tag" content="[^"]+">\s*)+', tag_block + "\n", new_html)
    
    content_pattern = r'(<div class="entry-content clear"[^>]* itemprop="text">).*?(</div><!-- \.entry-content \.clear -->)'
    match = re.search(content_pattern, new_html, re.DOTALL)
    if match:
        header_part = f"""
<div class="entry-content clear" data-ast-blocks-layout="true" itemprop="text">
{body_html}
"""
        new_html = re.sub(content_pattern, header_part + "</div><!-- .entry-content .clear -->", new_html, flags=re.DOTALL)
    else:
        print("ERROR: could not find entry-content block in template!")
        return
        
    new_post_file = os.path.join(post_dir, "index.html")
    with open(new_post_file, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Generated post HTML: {new_post_file}")
    
    update_post_list(os.path.join(ROOT, "blog.html"), slug, metadata)
    update_post_list(os.path.join(ROOT, "category", "health", "index.html"), slug, metadata)
    update_post_list(os.path.join(ROOT, "author", "kim890417", "index.html"), slug, metadata)

def update_post_list(filepath, slug, metadata):
    if not os.path.exists(filepath):
        print(f"Skipping update for missing file: {filepath}")
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if already added (remove it if it exists so we can replace/update it with correct title/metadata)
    # Actually, we can just replace if it's there, but to be safe, let's restore first or discard changes in git if re-running
    pass

    # Find the first article tag to prepend before
    article_match = re.search(r'(<article[^>]*id="post-(\d+)"[^>]*>.*?/article>)', content, re.DOTALL)
    if not article_match:
        print(f"Could not find any article block in {filepath}!")
        return
        
    first_article = article_match.group(1)
    
    # We want to use post-345 block structure as template since we know its structure
    # Let's search specifically for the post-345 article block to use as template
    template_match = re.search(r'(<article[^>]*id="post-345"[^>]*>.*?/article>)', content, re.DOTALL)
    if template_match:
        template_article = template_match.group(1)
    else:
        template_article = first_article
        
    new_article = template_article
    new_article = new_article.replace('id="post-345"', 'id="post-350"')
    new_article = new_article.replace('id="post-343"', 'id="post-350"')
    new_article = re.sub(r'health/[^/"]+', f'health/{slug}', new_article)
    new_article = re.sub(r'(<a href="https://healthfit100\.com/health/[^"]+" rel="bookmark">).*?(</a>)', f'\\1{metadata["title"]}\\2', new_article)
    new_article = re.sub(r'\d+월 \d+, \d{4}', metadata["display_date"], new_article)
    
    excerpt_pattern = r'(<div class="ast-excerpt-container[^>]*>.*?<p>).*?(</p>)'
    new_excerpt = metadata["desc"][:100] + "..."
    new_article = re.sub(excerpt_pattern, f'\\1{new_excerpt}\\2', new_article, flags=re.DOTALL)
    
    # If the post is already in the list (e.g. from previous run), let's remove it first
    # So we don't duplicate it.
    if f'id="post-350"' in content:
        # remove old post-350 article block
        content = re.sub(r'<article[^>]*id="post-350"[^>]*>.*?/article>\s*', '', content, flags=re.DOTALL)
        # re-evaluate first article match
        article_match = re.search(r'(<article[^>]*id="post-(\d+)"[^>]*>.*?/article>)', content, re.DOTALL)
        first_article = article_match.group(1)
        
    updated_content = content.replace(first_article, new_article + "\n" + first_article)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"Updated article list in: {filepath}")

if __name__ == "__main__":
    publish()

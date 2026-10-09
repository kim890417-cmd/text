import re

with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
css_pattern = r'<style id="healthfit-blog-cleanup">[\s\S]*?</style>'
new_css = """<style id="healthfit-blog-cleanup">
#masthead,#secondary{display:none!important}
.content-area.primary{width:100%!important;max-width:980px;margin:0 auto}
.healthfit-blog-intro{padding:18px 4px 28px}
.healthfit-blog-intro h1{margin:0 0 8px;font-size:2rem;font-weight:800;color:#0f172a}
.healthfit-blog-intro p{margin:0;color:#64748b;font-size:0.95rem}
.ast-row{display:flex!important;flex-direction:column!important;gap:18px}
.ast-article-post{width:100%!important;max-width:100%!important;padding:0!important;background:transparent!important;border:none!important;box-shadow:none!important}
.ast-article-inner{border:1px solid #e2e8f0!important;border-radius:16px!important;padding:16px 20px!important;box-shadow:0 4px 14px rgba(15,23,42,.04)!important;background:#fff!important;display:grid!important;grid-template-columns:145px minmax(0,1fr)!important;column-gap:22px!important;align-items:center!important;transition:transform .2s ease,box-shadow .2s ease}
.ast-article-inner:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(15,23,42,.08)!important}
.post-thumb-img-content{width:145px!important;height:181px!important;aspect-ratio:4/5!important;border-radius:12px!important;overflow:hidden!important;margin:0!important;flex-shrink:0!important;background:#0f172a;box-shadow:0 4px 12px rgba(0,0,0,0.08)!important}
.post-thumb-img-content a{display:block;width:100%;height:100%}
.post-thumb-img-content img{width:100%!important;height:100%!important;object-fit:cover!important;display:block!important;transition:transform .3s ease}
.ast-article-inner:hover .post-thumb-img-content img{transform:scale(1.04)}
.post-content{min-width:0}
.post-content .entry-title{font-size:1.15rem!important;line-height:1.45!important;margin:4px 0 8px!important}
.post-content .entry-title a{color:#0f172a!important;text-decoration:none!important;transition:color .2s}
.post-content .entry-title a:hover{color:#0284c7!important}
.ast-excerpt-container p{color:#475569!important;font-size:0.88rem!important;line-height:1.55!important;margin:0 0 6px!important;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.entry-meta{font-size:0.8rem!important;color:#94a3b8!important;margin-bottom:6px!important}
.cat-links a{display:inline-block;font-size:0.75rem!important;font-weight:700!important;color:#0284c7!important;background:#f0f9ff!important;padding:2px 8px!important;border-radius:999px!important;text-decoration:none!important;margin-bottom:6px!important}

@media (max-width: 640px) {
  .ast-article-inner{grid-template-columns:110px minmax(0,1fr)!important;column-gap:14px!important;padding:12px 14px!important}
  .post-thumb-img-content{width:110px!important;height:138px!important}
  .post-content .entry-title{font-size:0.98rem!important;line-height:1.4!important}
  .ast-excerpt-container p{font-size:0.82rem!important;-webkit-line-clamp:2}
}
</style>"""

html = re.sub(css_pattern, new_css, html, count=1)

# 2. Process articles
article_pattern = r'(<article\s+[^>]*>[\s\S]*?</article>)'

def process_one_article(match):
    art = match.group(0)
    
    # Extract slug
    link_m = re.search(r'href=[\'"](?:https://healthfit100\.com)?/health/([^\'\"/]+)/?[\'"]', art)
    if not link_m:
        return art
    slug = link_m.group(1)
    
    # Extract title
    title_m = re.search(r'<h2 class=[\'"]entry-title[^\'"]*[\'"][^>]*>\s*<a[^>]*>(.*?)</a>\s*</h2>', art, re.S)
    title = title_m.group(1).strip() if title_m else slug
    
    clean_thumb = f"""<div class="post-thumb-img-content">
		<a href="/health/{slug}/">
			<img src="/health/{slug}/thumbnail.png" alt="{title}" loading="lazy">
		</a>
	</div>"""

    if 'post-thumb-img-content' in art:
        # replace existing thumb
        art = re.sub(r'<div class=[\'"]post-thumb-img-content[\'"][^>]*>[\s\S]*?</a>\s*</div>', clean_thumb, art, count=1)
    else:
        # was ast-no-thumb
        art = art.replace('ast-no-thumb', 'has-post-thumbnail')
        art = re.sub(r'<div class=[\'"]ast-blog-featured-section[^\'"]*[\'"][^>]*>[\s\S]*?</a>\s*</div>', '', art, count=1)
        art = art.replace('<div class="post-content ast-grid-common-col">', f"{clean_thumb}\n\t<div class=\"post-content ast-grid-common-col\">", 1)

    return art

new_html = re.sub(article_pattern, process_one_article, html)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Applied blog.html layout successfully!")

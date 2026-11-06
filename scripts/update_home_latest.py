"""Refresh the homepage feature from the latest actually published article."""
from pathlib import Path
from datetime import datetime, timezone
import re, json, html
ROOT = Path(__file__).resolve().parents[1]
def update(now=None):
    now = now or datetime.now(timezone.utc)
    posts=[]
    for p in (ROOT/'health').glob('*/index.html'):
        text=p.read_text(encoding='utf-8')
        if re.search(r'<meta[^>]*(?:content=["\'][^"\']*noindex)',text,re.I): continue
        published=None
        for block in re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',text,re.S):
            try:
                data=json.loads(block)
                def walk(v):
                    if isinstance(v,dict):
                        yield v
                        for child in v.values(): yield from walk(child)
                    elif isinstance(v,list):
                        for child in v: yield from walk(child)
                for node in walk(data):
                    if node.get('datePublished'): published=datetime.fromisoformat(node['datePublished'].replace('Z','+00:00'))
            except (ValueError,TypeError): continue
        if published is None: continue
        if published.tzinfo is None: published=published.replace(tzinfo=timezone.utc)
        if published>now: continue
        title=re.search(r'<h1[^>]*>(.*?)</h1>',text,re.S)
        if not title: continue
        title=html.unescape(re.sub('<[^>]+>','',title[1]))
        meta=re.search(r'<meta[^>]*name="description"[^>]*>',text)
        if not meta:meta=re.search(r'<meta[^>]*content="[^"]*"[^>]*name="description"[^>]*>',text)
        desc=re.search(r'content="([^"]*)"',meta[0])[1] if meta else ''
        image=re.search(r'<meta[^>]*property="og:image"[^>]*>',text)
        if not image:image=re.search(r'<meta[^>]*content="[^"]*"[^>]*property="og:image"[^>]*>',text)
        src=html.unescape(re.search(r'content="([^"]*)"',image[0])[1]) if image else '/images/note/note-home.webp'
        posts.append((published,p.parent.name,title,html.unescape(desc),src))
    if not posts:raise RuntimeError('No dated published article found')
    date,slug,title,desc,src=max(posts,key=lambda row:(row[0],row[1]))
    e=html.escape
    feature=f'<article class="story feature-story"><a href="/health/{slug}/"><div class="story-image"><img alt="{e(title)}" fetchpriority="high" height="640" src="{e(src)}" width="960"/></div><div class="story-copy"><small>최신 글, <time datetime="{date.isoformat()}">{date:%Y.%m.%d}</time></small><h2>{e(title)}</h2><p>{e(desc)}</p></div></a></article>'
    p=ROOT/'index.html';text=p.read_text(encoding='utf-8')
    text,count=re.subn(r'<article class="story feature-story">.*?</article>',lambda m:feature,text,count=1,flags=re.S)
    if count!=1:raise RuntimeError('Homepage feature missing')
    text=re.sub(r'(<div class="eyebrow">).*?(</div>)(?=<article class="story feature-story">)',r'\1가장 최근에 발행한 글\2',text,count=1,flags=re.S)
    p.write_text(text,encoding='utf-8',newline='\n')
    print('Homepage latest:',slug,date.isoformat())
    return slug
if __name__=='__main__':update()

import glob
import re
import urllib.request
import urllib.error
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

files = glob.glob('health/*/index.html')
print(f'Checking {len(files)} articles...')

external_links = {}
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    # find all href
    matches = re.findall(r'href=["\'](https?://[^"\']+)["\']', content)
    for m in matches:
        if 'healthfit100.com' not in m and 'fonts.googleapis.com' not in m and 'fonts.gstatic.com' not in m and 'schema.org' not in m and 'w3.org' not in m:
            external_links.setdefault(m, []).append(f)

print(f'Total unique external links found: {len(external_links)}')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

broken_links = {}
working_links = {}

for url, flist in external_links.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        # try HEAD first, then GET
        try:
            req.get_method = lambda: 'HEAD'
            resp = urllib.request.urlopen(req, context=ctx, timeout=7)
            code = resp.getcode()
        except Exception:
            req.get_method = lambda: 'GET'
            resp = urllib.request.urlopen(req, context=ctx, timeout=7)
            code = resp.getcode()
            
        if code in [200, 301, 302, 307, 308]:
            working_links[url] = code
        else:
            broken_links[url] = (code, 'HTTP Status', flist)
    except urllib.error.HTTPError as e:
        broken_links[url] = (e.code, str(e), flist)
    except Exception as e:
        broken_links[url] = ('ERROR', str(e), flist)
    time.sleep(0.1)

print(f'\n--- SUMMARY ---')
print(f'Working links: {len(working_links)}')
print(f'Broken/Problematic links: {len(broken_links)}')
for u, info in broken_links.items():
    print(f'[BROKEN {info[0]}] {u}')
    print(f'  Reason: {info[1]}')
    print(f'  Used in ({len(info[2])} files): {info[2][:3]}')

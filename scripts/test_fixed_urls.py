import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    "https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6547",
    "https://www.starbucks.co.kr/menu/drink_list.do",
    "https://www.fda.gov/food/dietary-supplements/pure-and-highly-concentrated-caffeine"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        resp = urllib.request.urlopen(req, context=ctx, timeout=10)
        print(f"[OK {resp.getcode()}] {u}")
    except urllib.error.HTTPError as e:
        print(f"[FAIL {e.code}] {u}")
    except Exception as e:
        print(f"[ERR] {e} {u}")

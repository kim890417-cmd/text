import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    "https://www.fda.gov/food/information-dietary-supplement-ingredients-and-other-substances/fda-warns-consumers-about-pure-and-highly-concentrated-caffeine",
    "https://health.seoulmc.or.kr/uploadFiles/2025_%ED%95%9C%EA%B5%AD%EC%9D%B8%EC%98%81%EC%96%91%EC%86%8C%EC%84%AD%EC%B7%A8%EA%B8%B0%EC%A4%80_%ED%99%9C%EC%9A%A9.pdf",
    "https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6547",
    "https://www.starbucks.co.kr/app/menu/drink_list.do",
    "https://ods.od.nih.gov/factsheets/Calcium-Consumer/",
    "https://pubmed.ncbi.nlm.nih.gov/38242596/",
    "https://www.cdc.gov/alcohol/standard-drink-sizes/index.html",
    "https://www.heart.org/en/health-topics/cholesterol/hdl-good-ldl-bad-cholesterol-and-triglycerides",
    "https://academic.oup.com/ajcn/article/72/3/696/4729402"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        resp = urllib.request.urlopen(req, context=ctx, timeout=10)
        print(f"[OK {resp.getcode()}] {u[:60]}")
    except urllib.error.HTTPError as e:
        print(f"[FAIL {e.code}] {u[:60]}")
    except Exception as e:
        print(f"[ERR] {e} {u[:60]}")

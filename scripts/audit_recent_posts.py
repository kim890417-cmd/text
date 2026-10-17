import re, sys
from pathlib import Path

repo = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")
articles = [
    "nutrition-facts-sugar-serving-size-calculation",
    "caffeine-daily-intake-drinks-record-method",
    "standard-weight-calculator-height-male-female"
]

with open("audit_recent_posts.txt", "w", encoding="utf-8") as out:
    for slug in articles:
        p = repo / "health" / slug / "index.html"
        if not p.exists():
            continue
        content = p.read_text(encoding="utf-8")
        
        m_title = re.search(r"<title>(.*?)</title>", content)
        title = m_title.group(1) if m_title else ""
        
        m_h1 = re.search(r"<h1>(.*?)</h1>", content)
        h1 = m_h1.group(1) if m_h1 else ""
        
        m_q = re.search(r'<p class="article-question">(.*?)</p>', content)
        q = m_q.group(1) if m_q else ""
        
        h2s = re.findall(r"<h2>(.*?)</h2>", content)
        
        text_only = re.sub(r"<[^>]+>", "", content)
        clean_text = "".join(text_only.split())
        
        has_table = "<table" in content
        has_csv = ".csv" in content
        has_calc = ("<form" in content) or ("×" in content and "=" in content)
        
        out.write(f"=== {slug} ===\n")
        out.write(f"제목: {h1}\n")
        out.write(f"독자 질문: {q}\n")
        out.write(f"공백 제외 글자수: {len(clean_text):,}자\n")
        out.write(f"실습 요소: 비교표({has_table}), 계산공식({has_calc}), CSV기록표다운로드({has_csv})\n")
        out.write("소제목(H2):\n")
        for h in h2s:
            clean_h = re.sub(r"<[^>]+>", "", h)
            out.write(f"  * {clean_h}\n")
        out.write("\n")

print("Report generated in audit_recent_posts.txt")

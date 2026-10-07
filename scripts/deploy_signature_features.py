import os
import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Update index.html with Signature Tools Section
index_path = REPO_DIR / "index.html"
index_c = index_path.read_text(encoding="utf-8-sig")

sig_section = """
      <h2 class="section-title">✨ 건강노트 시그니처 맞춤 도구</h2>
      <p class="section-sub">나만을 위한 영양제 복용 시간표, 건강검진 종합 신호등 리포트, 30초 건강 자가진단을 무료로 이용하세요.</p>
      <div class="tool-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin-bottom: 45px;">
        <!-- Signature Tool 1: Routine Planner -->
        <a href="/routine" class="tool-card" style="border: 2px solid #bae6fd; background: #f0f9ff;">
          <div class="tool-icon">📋</div>
          <h3 style="color:#0369a1;">내 영양제 복용 시간표 & 궁합 플래너</h3>
          <p>복용 중인 영양제를 체크하면 아침 공복, 점심 식후, 취침 전 최적의 복용 시간표와 흡수를 방해하는 상극 충돌을 즉시 분석합니다.</p>
          <span class="tool-tag" style="background:#0284c7; color:#fff;">강력 추천 · 시그니처</span>
        </a>

        <!-- Signature Tool 2: Checkup Lab Analyzer -->
        <a href="/checkup" class="tool-card" style="border: 2px solid #fde68a; background: #fefce8;">
          <div class="tool-icon">🩺</div>
          <h3 style="color:#854d0e;">건강검진 수치 신호등 리포트</h3>
          <p>혈압, 공복혈당, LDL 콜레스테롤, 간수치(ALT)를 입력하면 정상·주의·위험 신호등 등급과 질환별 맞춤 실천 가이드를 진단합니다.</p>
          <span class="tool-tag" style="background:#ca8a04; color:#fff;">초록·노랑·빨강 판정</span>
        </a>

        <!-- Signature Tool 3: Diagnostic Quiz -->
        <a href="/quiz" class="tool-card" style="border: 2px solid #e9d5ff; background: #faf5ff;">
          <div class="tool-icon">⚡</div>
          <h3 style="color:#6b21a8;">30초 맞춤 건강 자가진단 퀴즈</h3>
          <p>피로 시간대, 식사 습관, 운동 패턴 등 4가지 간단한 질문으로 지금 내 몸에 가장 시급한 1순위 건강 관리법과 영양소를 찾아드립니다.</p>
          <span class="tool-tag" style="background:#9333ea; color:#fff;">30초 간편 테스트</span>
        </a>
      </div>
"""

# Place above <h2 class="section-title">🧮 건강 계산기</h2>
calc_marker = '<h2 class="section-title">🧮 건강 계산기</h2>'
if calc_marker in index_c and "건강노트 시그니처 맞춤 도구" not in index_c:
    index_c = index_c.replace(calc_marker, f'{sig_section}\n{calc_marker}', 1)
    index_path.write_text(index_c, encoding="utf-8")
    print("Updated index.html with Signature Tools")

# 2. Update navigation dropdown across all HTML files
dropdown_old = """<div class="dropdown-content">
            <a href="/bmi">BMI 계산기</a>
            <a href="/calorie">칼로리 계산기</a>
            <a href="/protein">단백질 계산기</a>
            <a href="/water">물 섭취량 계산기</a>
            <a href="/supplement">영양제 권장량</a>
          </div>"""

dropdown_new = """<div class="dropdown-content">
            <a href="/routine">영양제 시간표 플래너</a>
            <a href="/checkup">건강검진 신호등 리포트</a>
            <a href="/quiz">건강 자가진단 퀴즈</a>
            <a href="/bmi">BMI 계산기</a>
            <a href="/calorie">칼로리 계산기</a>
            <a href="/protein">단백질 계산기</a>
            <a href="/water">물 섭취량 계산기</a>
            <a href="/supplement">영양제 권장량 조회</a>
          </div>"""

footer_calc_old = """<h4>건강 계산기</h4>
        <ul>
          <li><a href="/bmi">BMI 계산기</a></li>
          <li><a href="/calorie">칼로리 계산기</a></li>
          <li><a href="/protein">단백질 계산기</a></li>
          <li><a href="/water">물 섭취량 계산기</a></li>
          <li><a href="/supplement">영양제 권장량</a></li>
          <li><a href="/blog">건강 블로그</a></li>
        </ul>"""

footer_calc_new = """<h4>건강 계산기 & 도구</h4>
        <ul>
          <li><a href="/routine">영양제 시간표 플래너</a></li>
          <li><a href="/checkup">건강검진 신호등 리포트</a></li>
          <li><a href="/quiz">건강 자가진단 퀴즈</a></li>
          <li><a href="/bmi">BMI 계산기</a></li>
          <li><a href="/calorie">칼로리 계산기</a></li>
          <li><a href="/protein">단백질 계산기</a></li>
          <li><a href="/water">물 섭취량 계산기</a></li>
          <li><a href="/supplement">영양제 권장량 조회</a></li>
        </ul>"""

all_html_files = list(REPO_DIR.glob("*.html"))
for hf in all_html_files:
    text = hf.read_text(encoding="utf-8-sig", errors="ignore")
    changed = False
    
    # Update dropdown
    if '<a href="#" class="dropbtn">건강 계산기</a>' in text:
        text = text.replace('<a href="#" class="dropbtn">건강 계산기</a>', '<a href="#" class="dropbtn">건강 계산기 & 도구</a>')
        changed = True
        
    if '/routine' not in text:
        # replace dropdown content
        m = re.search(r'<div class="dropdown-content">[\s\S]*?</div>', text)
        if m:
            text = text[:m.start()] + dropdown_new + text[m.end():]
            changed = True
            
    # update footer if present
    if '<h4>건강 계산기</h4>' in text:
        text = text.replace(footer_calc_old, footer_calc_new)
        changed = True

    if changed:
        hf.write_text(text, encoding="utf-8")
        print(f"Updated nav & footer in {hf.name}")

# 3. Update scripts/generate_sitemap.py to include new static pages
sitemap_gen_path = REPO_DIR / "scripts" / "generate_sitemap.py"
sg_text = sitemap_gen_path.read_text(encoding="utf-8-sig")
if '"/routine"' not in sg_text:
    old_static_pages = """STATIC_PAGES = [
    "/",
    "/blog",
    "/bmi",
    "/calorie",
    "/protein",
    "/water",
    "/supplement",
    "/about",
    "/contact",
    "/privacy",
    "/terms",
]"""

    new_static_pages = """STATIC_PAGES = [
    "/",
    "/blog",
    "/routine",
    "/checkup",
    "/quiz",
    "/bmi",
    "/calorie",
    "/protein",
    "/water",
    "/supplement",
    "/about",
    "/contact",
    "/privacy",
    "/terms",
]"""
    sg_text = sg_text.replace(old_static_pages, new_static_pages)
    sitemap_gen_path.write_text(sg_text, encoding="utf-8")
    print("Updated generate_sitemap.py with new static pages")

print("All signature features deployed successfully!")

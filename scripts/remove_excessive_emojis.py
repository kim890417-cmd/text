import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Clean Navigation Bar in all files
# We replace emoji navbar with sleek, text-based professional navbar
clean_navbar = """  <nav class="navbar">
    <div class="nav-container">
      <a href="/" class="nav-logo">건강노트</a>
      <ul class="nav-menu">
        <li class="dropdown">
          <a href="#" class="dropbtn">건강 진단·분석</a>
          <div class="dropdown-content">
            <a href="/routine">영양제 복용 플래너</a>
            <a href="/checkup">건강검진 수치 해석기</a>
            <a href="/quiz">맞춤 건강 자가진단</a>
          </div>
        </li>
        <li class="dropdown">
          <a href="#" class="dropbtn">건강 계산기</a>
          <div class="dropdown-content">
            <a href="/bmi">BMI·표준체중</a>
            <a href="/calorie">하루 칼로리·기초대사량</a>
            <a href="/protein">단백질 섭취량</a>
            <a href="/exercise">운동 소모 칼로리</a>
            <a href="/water">물 섭취량 계산</a>
            <a href="/caffeine">카페인 안전 섭취량</a>
            <a href="/alcohol">알코올 분해 시간</a>
            <a href="/supplement">영양제 권장·상한량</a>
          </div>
        </li>
        <li><a href="/blog">건강 칼럼</a></li>
        <li><a href="/about">소개</a></li>
        <li><a href="/contact">문의하기</a></li>
      </ul>
    </div>
  </nav>"""

clean_footer_tools = """        <h4>건강 도구 및 계산기</h4>
        <ul>
          <li><a href="/routine">영양제 복용 플래너</a></li>
          <li><a href="/checkup">건강검진 수치 해석기</a></li>
          <li><a href="/quiz">맞춤 건강 자가진단</a></li>
          <li><a href="/bmi">BMI·표준체중 계산기</a></li>
          <li><a href="/calorie">하루 칼로리·기초대사량</a></li>
          <li><a href="/protein">단백질 섭취량 계산기</a></li>
          <li><a href="/exercise">운동 소모 칼로리 계산기</a></li>
          <li><a href="/water">물 섭취량 계산기</a></li>
          <li><a href="/caffeine">카페인 안전 섭취량 계산기</a></li>
          <li><a href="/alcohol">알코올 분해 시간 계산기</a></li>
          <li><a href="/supplement">영양제 권장·상한량 조회</a></li>
        </ul>"""

for hf in REPO_DIR.glob("*.html"):
    text = hf.read_text(encoding="utf-8-sig", errors="ignore")
    # Replace navbar
    m_nav = re.search(r'<nav class="navbar">[\s\S]*?</nav>', text)
    if m_nav:
        text = text[:m_nav.start()] + clean_navbar + text[m_nav.end():]
        
    # Replace footer tools
    m_foot = re.search(r'<h4>건강 계산기[^<]*</h4>\s*<ul>[\s\S]*?</ul>', text)
    if m_foot:
        text = text[:m_foot.start()] + clean_footer_tools + text[m_foot.end():]
        
    hf.write_text(text, encoding="utf-8")

print("Cleaned navbar and footer in all HTML files")

# 2. Clean index.html headings and cards
index_path = REPO_DIR / "index.html"
index_c = index_path.read_text(encoding="utf-8-sig")

# Replace emojis in index.html
replacements = [
    ("✨ 시그니처 맞춤 분석 도구", "전문 건강 분석 도구"),
    ("✨ 건강노트 시그니처 맞춤 도구", "전문 건강 분석 도구"),
    ("🍂 10월 테마 큐레이션", "10월 기획 칼럼"),
    ("🍂 10월 환절기", "10월 환절기"),
    ("✍️ 최신 & 추천 건강 칼럼", "최신 건강 칼럼"),
    ("🌿 에디터의 3대 건강 관리 원칙", "건강노트 3대 건강 관리 원칙"),
    ("🛡️ 건강노트의 3대 콘텐츠 검증 및 작성 원칙", "건강노트 3대 콘텐츠 검증 및 편집 원칙"),
    ("🧮 건강 계산기", "건강 계산기"),
    ("⚖️ 체중 & 다이어트 계산기", "체중 및 다이어트 계산기"),
    ("☕ 일상 생활습관 & 영양 계산기", "일상 생활습관 및 영양 계산기"),
    ("건강 블로그", "건강 칼럼"),
    ("✨", ""),
    ("🌟", ""),
    ("📋 ", ""),
    ("🩺 ", ""),
    ("⚡ ", ""),
    ("⚖️ ", ""),
    ("🔥 ", ""),
    ("🍗 ", ""),
    ("🏃 ", ""),
    ("💧 ", ""),
    ("☕ ", ""),
    ("🍺 ", ""),
    ("💊 ", ""),
    ("🌿 ", ""),
    ("🛡️ ", ""),
    ("🍂 ", ""),
    ("✍️ ", ""),
    ("🧮 ", ""),
    ("🌾 ", ""),
    ("❤️ ", ""),
    ("☀️ ", ""),
    ("🥛 ", ""),
    ("🩸 ", ""),
    ("🍋 ", ""),
    ("🐟 ", ""),
    ("👁️ ", ""),
    ("🦴 ", ""),
    ("🌙 ", "")
]

for old, new in replacements:
    index_c = index_c.replace(old, new)

index_path.write_text(index_c, encoding="utf-8")
print("Cleaned index.html emojis")

# 3. Clean tool pages: routine.html, checkup.html, quiz.html, caffeine.html, alcohol.html, exercise.html
tools = ["routine.html", "checkup.html", "quiz.html", "caffeine.html", "alcohol.html", "exercise.html", "bmi.html", "calorie.html", "protein.html", "water.html", "supplement.html"]

for t_name in tools:
    tp = REPO_DIR / t_name
    if not tp.exists():
        continue
    tc = tp.read_text(encoding="utf-8-sig")
    for old, new in replacements:
        tc = tc.replace(old, new)
        
    # Replace common emoji badges in tool headers
    tc = tc.replace("⚠️", "[주의]")
    tc = tc.replace("🚨", "[경고]")
    tc = tc.replace("🎉", "[완료]")
    tc = tc.replace("💡", "[추천]")
    tc = tc.replace("ℹ️", "[참고]")
    
    tp.write_text(tc, encoding="utf-8")
    print(f"Cleaned emojis in {t_name}")

print("Emoji cleanup complete!")

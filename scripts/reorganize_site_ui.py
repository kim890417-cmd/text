import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Prepare new compact tools section for index.html
compact_tools_html = """
      <!-- 1. 시그니처 분석 도구 -->
      <div style="margin-bottom: 35px;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom: 14px;">
          <div>
            <h2 style="font-size: 1.25rem; font-weight: 800; margin: 0; color: #0f172a;">✨ 시그니처 맞춤 분석 도구</h2>
            <p style="font-size: 0.88rem; color: #64748b; margin: 3px 0 0;">건강노트에서만 제공하는 1:1 맞춤형 진단 & 분석 서비스입니다.</p>
          </div>
          <span style="font-size: 0.8rem; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 3px 10px; border-radius: 999px;">3종 추천</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
          <a href="/routine" style="display:flex; align-items:flex-start; gap:14px; background:#f0f9ff; border:1.5px solid #bae6fd; border-radius:14px; padding:16px 18px; text-decoration:none; color:inherit; transition:transform 0.2s, box-shadow 0.2s;">
            <div style="font-size:1.8rem; line-height:1;">📋</div>
            <div style="flex:1;">
              <strong style="font-size:0.98rem; color:#0369a1; display:block; margin-bottom:3px;">영양제 시간표 & 상극 궁합 플래너</strong>
              <p style="font-size:0.84rem; color:#475569; margin:0 0 6px; line-height:1.4;">먹는 영양제 체크 시 4단계 시간표와 상극 충돌 자동 분석</p>
              <span style="font-size:0.75rem; font-weight:700; color:#0284c7; background:#e0f2fe; padding:2px 8px; border-radius:999px;">골든타임 추천</span>
            </div>
          </a>
          <a href="/checkup" style="display:flex; align-items:flex-start; gap:14px; background:#fefce8; border:1.5px solid #fde68a; border-radius:14px; padding:16px 18px; text-decoration:none; color:inherit; transition:transform 0.2s, box-shadow 0.2s;">
            <div style="font-size:1.8rem; line-height:1;">🩺</div>
            <div style="flex:1;">
              <strong style="font-size:0.98rem; color:#854d0e; display:block; margin-bottom:3px;">건강검진 수치 신호등 리포트</strong>
              <p style="font-size:0.84rem; color:#475569; margin:0 0 6px; line-height:1.4;">혈압, 혈당, 콜레스테롤, 간수치 정상·주의·위험 신호등 판정</p>
              <span style="font-size:0.75rem; font-weight:700; color:#a16207; background:#fef3c7; padding:2px 8px; border-radius:999px;">종합 해석</span>
            </div>
          </a>
          <a href="/quiz" style="display:flex; align-items:flex-start; gap:14px; background:#faf5ff; border:1.5px solid #e9d5ff; border-radius:14px; padding:16px 18px; text-decoration:none; color:inherit; transition:transform 0.2s, box-shadow 0.2s;">
            <div style="font-size:1.8rem; line-height:1;">⚡</div>
            <div style="flex:1;">
              <strong style="font-size:0.98rem; color:#6b21a8; display:block; margin-bottom:3px;">30초 맞춤 건강 자가진단 퀴즈</strong>
              <p style="font-size:0.84rem; color:#475569; margin:0 0 6px; line-height:1.4;">4가지 질문으로 내 몸에 가장 시급한 1순위 케어 솔루션 처방</p>
              <span style="font-size:0.75rem; font-weight:700; color:#7e22ce; background:#f3e8ff; padding:2px 8px; border-radius:999px;">30초 간편 테스트</span>
            </div>
          </a>
        </div>
      </div>

      <!-- 2. 체중 & 다이어트 계산기 -->
      <div style="margin-bottom: 35px;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom: 14px;">
          <div>
            <h2 style="font-size: 1.25rem; font-weight: 800; margin: 0; color: #0f172a;">⚖️ 체중 & 다이어트 계산기</h2>
            <p style="font-size: 0.88rem; color: #64748b; margin: 3px 0 0;">체성분 분석과 과학적 다이어트 감량 플랜을 위한 정밀 계산기입니다.</p>
          </div>
          <span style="font-size: 0.8rem; font-weight: 700; color:#2563eb; background:#eff6ff; padding:3px 10px; border-radius:999px;">4종 계산</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
          <a href="/bmi" style="background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-decoration:none; color:inherit; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:1.4rem; margin-bottom:6px;">⚖️</div>
              <strong style="font-size:0.95rem; color:#1e293b; display:block; margin-bottom:3px;">BMI·표준체중 계산기</strong>
              <p style="font-size:0.82rem; color:#64748b; margin:0 0 8px; line-height:1.4;">키·몸무게 기반 아시아 기준 비만도 및 표준체중</p>
            </div>
            <span style="font-size:0.75rem; font-weight:700; color:#0284c7; background:#f0f9ff; padding:2px 8px; border-radius:999px; align-self:flex-start;">비만도·체지방</span>
          </a>
          <a href="/calorie" style="background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-decoration:none; color:inherit; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:1.4rem; margin-bottom:6px;">🔥</div>
              <strong style="font-size:0.95rem; color:#1e293b; display:block; margin-bottom:3px;">하루 칼로리·BMR 계산기</strong>
              <p style="font-size:0.82rem; color:#64748b; margin:0 0 8px; line-height:1.4;">기초대사량 및 감량·유지·증량 목표 TDEE 산출</p>
            </div>
            <span style="font-size:0.75rem; font-weight:700; color:#0284c7; background:#f0f9ff; padding:2px 8px; border-radius:999px; align-self:flex-start;">BMR · TDEE</span>
          </a>
          <a href="/protein" style="background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-decoration:none; color:inherit; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:1.4rem; margin-bottom:6px;">🍗</div>
              <strong style="font-size:0.95rem; color:#1e293b; display:block; margin-bottom:3px;">단백질 권장 섭취량 계산기</strong>
              <p style="font-size:0.82rem; color:#64748b; margin:0 0 8px; line-height:1.4;">활동량과 체중에 따른 근육 유지 일일 단백질량(g)</p>
            </div>
            <span style="font-size:0.75rem; font-weight:700; color:#0284c7; background:#f0f9ff; padding:2px 8px; border-radius:999px; align-self:flex-start;">근육 유지·감량</span>
          </a>
          <a href="/exercise" style="background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-decoration:none; color:inherit; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:1.4rem; margin-bottom:6px;">🏃</div>
              <strong style="font-size:0.95rem; color:#1e293b; display:block; margin-bottom:3px;">운동 소모 칼로리 계산기</strong>
              <p style="font-size:0.82rem; color:#64748b; margin:0 0 8px; line-height:1.4;">걷기·러닝·수영·웨이트 등 METs 소비 칼로리 정밀 계산</p>
            </div>
            <span style="font-size:0.75rem; font-weight:700; color:#0284c7; background:#f0f9ff; padding:2px 8px; border-radius:999px; align-self:flex-start;">체지방 연소</span>
          </a>
        </div>
      </div>

      <!-- 3. 일상 생활습관 & 영양 계산기 -->
      <div style="margin-bottom: 45px;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom: 14px;">
          <div>
            <h2 style="font-size: 1.25rem; font-weight: 800; margin: 0; color: #0f172a;">☕ 일상 생활습관 & 영양 계산기</h2>
            <p style="font-size: 0.88rem; color: #64748b; margin: 3px 0 0;">물, 커피, 알코올, 영양제 등 매일 실천하는 건강 기준치를 확인하세요.</p>
          </div>
          <span style="font-size: 0.8rem; font-weight: 700; color:#0d9488; background:#f0fdfa; padding:3px 10px; border-radius:999px;">4종 계산</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
          <a href="/water" style="background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-decoration:none; color:inherit; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:1.4rem; margin-bottom:6px;">💧</div>
              <strong style="font-size:0.95rem; color:#1e293b; display:block; margin-bottom:3px;">하루 물 섭취량 계산기</strong>
              <p style="font-size:0.82rem; color:#64748b; margin:0 0 8px; line-height:1.4;">체중과 운동량에 따른 하루 수분량(L) 및 잔 수</p>
            </div>
            <span style="font-size:0.75rem; font-weight:700; color:#0284c7; background:#f0f9ff; padding:2px 8px; border-radius:999px; align-self:flex-start;">수분 균형</span>
          </a>
          <a href="/caffeine" style="background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-decoration:none; color:inherit; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:1.4rem; margin-bottom:6px;">☕</div>
              <strong style="font-size:0.95rem; color:#1e293b; display:block; margin-bottom:3px;">카페인 안전량 계산기</strong>
              <p style="font-size:0.82rem; color:#64748b; margin:0 0 8px; line-height:1.4;">커피·음료 속 카페인 총량 및 성인 400mg 대비 섭취율</p>
            </div>
            <span style="font-size:0.75rem; font-weight:700; color:#0284c7; background:#f0f9ff; padding:2px 8px; border-radius:999px; align-self:flex-start;">안전 한도</span>
          </a>
          <a href="/alcohol" style="background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-decoration:none; color:inherit; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:1.4rem; margin-bottom:6px;">🍺</div>
              <strong style="font-size:0.95rem; color:#1e293b; display:block; margin-bottom:3px;">알코올 분해시간 계산기</strong>
              <p style="font-size:0.82rem; color:#64748b; margin:0 0 8px; line-height:1.4;">소주·맥주 잔 수와 체중 기준 위드마크 완전 해독 시간</p>
            </div>
            <span style="font-size:0.75rem; font-weight:700; color:#0284c7; background:#f0f9ff; padding:2px 8px; border-radius:999px; align-self:flex-start;">간 해독 시간</span>
          </a>
          <a href="/supplement" style="background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-decoration:none; color:inherit; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:1.4rem; margin-bottom:6px;">💊</div>
              <strong style="font-size:0.95rem; color:#1e293b; display:block; margin-bottom:3px;">영양제 권장·상한량 조회</strong>
              <p style="font-size:0.82rem; color:#64748b; margin:0 0 8px; line-height:1.4;">비타민·미네랄별 하루 권장 섭취량 및 과다 부작용 상한선</p>
            </div>
            <span style="font-size:0.75rem; font-weight:700; color:#0284c7; background:#f0f9ff; padding:2px 8px; border-radius:999px; align-self:flex-start;">권장·상한 기준</span>
          </a>
        </div>
      </div>
"""

# Replace tools in index.html
index_path = REPO_DIR / "index.html"
index_c = index_path.read_text(encoding="utf-8-sig")

# Cut out everything from <section class="hero"> to <!-- 10월 특별 기획 큐레이션 -->
hero_end = '</section>'
banner_start = '<!-- 10월 특별 기획 큐레이션 -->'

p1 = index_c.split(hero_end)[0] + hero_end + "\n"
p2 = banner_start + index_c.split(banner_start)[1]

new_index_c = p1 + "\n" + compact_tools_html + "\n" + p2
index_path.write_text(new_index_c, encoding="utf-8")
print("Updated index.html with organized compact 11-tool hub")

# 2. Universal Navigation Bar (Organized into 2 Dropdowns)
unified_navbar = """  <nav class="navbar">
    <div class="nav-container">
      <a href="/" class="nav-logo">건강노트</a>
      <ul class="nav-menu">
        <li class="dropdown">
          <a href="#" class="dropbtn">🌟 시그니처 진단</a>
          <div class="dropdown-content">
            <a href="/routine">📋 영양제 시간표 플래너</a>
            <a href="/checkup">🩺 건강검진 신호등 리포트</a>
            <a href="/quiz">⚡ 건강 자가진단 퀴즈</a>
          </div>
        </li>
        <li class="dropdown">
          <a href="#" class="dropbtn">🧮 건강 계산기 (8종)</a>
          <div class="dropdown-content">
            <a href="/bmi">⚖️ BMI·표준체중</a>
            <a href="/calorie">🔥 하루 칼로리·BMR</a>
            <a href="/protein">🍗 단백질 권장량</a>
            <a href="/exercise">🏃 운동 소모 칼로리</a>
            <a href="/water">💧 하루 물 섭취량</a>
            <a href="/caffeine">☕ 카페인 안전량</a>
            <a href="/alcohol">🍺 알코올 분해시간</a>
            <a href="/supplement">💊 영양제 권장·상한량</a>
          </div>
        </li>
        <li><a href="/blog">건강 블로그</a></li>
        <li><a href="/about">소개</a></li>
        <li><a href="/contact">문의하기</a></li>
      </ul>
    </div>
  </nav>"""

unified_footer_tools = """        <h4>건강 계산기 & 도구 (11종)</h4>
        <ul>
          <li><a href="/routine">영양제 시간표 플래너</a></li>
          <li><a href="/checkup">건강검진 신호등 리포트</a></li>
          <li><a href="/quiz">건강 자가진단 퀴즈</a></li>
          <li><a href="/bmi">BMI·표준체중 계산기</a></li>
          <li><a href="/calorie">하루 칼로리·BMR 계산기</a></li>
          <li><a href="/protein">단백질 섭취량 계산기</a></li>
          <li><a href="/exercise">운동 소모 칼로리 계산기</a></li>
          <li><a href="/water">물 섭취량 계산기</a></li>
          <li><a href="/caffeine">카페인 안전량 계산기</a></li>
          <li><a href="/alcohol">알코올 분해시간 계산기</a></li>
          <li><a href="/supplement">영양제 권장량 조회</a></li>
        </ul>"""

for hf in REPO_DIR.glob("*.html"):
    text = hf.read_text(encoding="utf-8-sig", errors="ignore")
    # Replace navbar
    m_nav = re.search(r'<nav class="navbar">[\s\S]*?</nav>', text)
    if m_nav:
        text = text[:m_nav.start()] + unified_navbar + text[m_nav.end():]
        
    # Replace footer tools
    m_foot = re.search(r'<h4>건강 계산기[^<]*</h4>\s*<ul>[\s\S]*?</ul>', text)
    if m_foot:
        text = text[:m_foot.start()] + unified_footer_tools + text[m_foot.end():]
        
    hf.write_text(text, encoding="utf-8")
    print(f"Updated unified navbar & footer in {hf.name}")

# 3. Update generate_sitemap.py with all 14 static pages
sg_path = REPO_DIR / "scripts" / "generate_sitemap.py"
sg_text = sg_path.read_text(encoding="utf-8-sig")

complete_static = """STATIC_PAGES = [
    "/",
    "/blog",
    "/routine",
    "/checkup",
    "/quiz",
    "/bmi",
    "/calorie",
    "/protein",
    "/exercise",
    "/water",
    "/caffeine",
    "/alcohol",
    "/supplement",
    "/about",
    "/contact",
    "/privacy",
    "/terms",
]"""

m_sp = re.search(r'STATIC_PAGES = \[[\s\S]*?\]', sg_text)
if m_sp:
    sg_text = sg_text[:m_sp.start()] + complete_static + sg_text[m_sp.end():]
    sg_path.write_text(sg_text, encoding="utf-8")
    print("Updated generate_sitemap.py with all 17 static pages")

print("Reorganization completed!")

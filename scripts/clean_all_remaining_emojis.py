import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Update index.html
index_file = REPO_DIR / "index.html"
index_html = index_file.read_text(encoding="utf-8")

# Replace card emojis with sleek modern SVGs
svg_routine = '''<div style="width:38px; height:38px; border-radius:10px; background:#e0f2fe; display:flex; align-items:center; justify-content:center; color:#0284c7; flex-shrink:0;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
            </div>'''

svg_checkup = '''<div style="width:38px; height:38px; border-radius:10px; background:#fef3c7; display:flex; align-items:center; justify-content:center; color:#b45309; flex-shrink:0;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>
            </div>'''

svg_quiz = '''<div style="width:38px; height:38px; border-radius:10px; background:#f3e8ff; display:flex; align-items:center; justify-content:center; color:#7e22ce; flex-shrink:0;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            </div>'''

svg_bmi = '''<div style="width:32px; height:32px; border-radius:8px; background:#eff6ff; display:flex; align-items:center; justify-content:center; color:#2563eb; margin-bottom:8px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="7" r="4"></circle><path d="M5.5 21a8.38 8.38 0 0 1 13 0"></path></svg>
              </div>'''

svg_calorie = '''<div style="width:32px; height:32px; border-radius:8px; background:#fef2f2; display:flex; align-items:center; justify-content:center; color:#dc2626; margin-bottom:8px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 3.5z"></path></svg>
              </div>'''

svg_protein = '''<div style="width:32px; height:32px; border-radius:8px; background:#f0fdf4; display:flex; align-items:center; justify-content:center; color:#16a34a; margin-bottom:8px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2v20M18 2v20M6 12h12M4 7h4M4 17h4M16 7h4M16 17h4"></path></svg>
              </div>'''

svg_exercise = '''<div style="width:32px; height:32px; border-radius:8px; background:#eff6ff; display:flex; align-items:center; justify-content:center; color:#3b82f6; margin-bottom:8px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              </div>'''

svg_water = '''<div style="width:32px; height:32px; border-radius:8px; background:#ecfeff; display:flex; align-items:center; justify-content:center; color:#0891b2; margin-bottom:8px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"></path></svg>
              </div>'''

svg_caffeine = '''<div style="width:32px; height:32px; border-radius:8px; background:#fdf4ff; display:flex; align-items:center; justify-content:center; color:#9333ea; margin-bottom:8px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path><line x1="6" y1="1" x2="6" y2="4"></line><line x1="10" y1="1" x2="10" y2="4"></line><line x1="14" y1="1" x2="14" y2="4"></line></svg>
              </div>'''

svg_alcohol = '''<div style="width:32px; height:32px; border-radius:8px; background:#fff7ed; display:flex; align-items:center; justify-content:center; color:#ea580c; margin-bottom:8px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M12 15v6M5 3l7 8 7-8z"></path></svg>
              </div>'''

svg_supplement = '''<div style="width:32px; height:32px; border-radius:8px; background:#f0fdfa; display:flex; align-items:center; justify-content:center; color:#0d9488; margin-bottom:8px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              </div>'''

index_html = index_html.replace('<div style="font-size:1.8rem; line-height:1;">📋</div>', svg_routine)
index_html = index_html.replace('<div style="font-size:1.8rem; line-height:1;">🩺</div>', svg_checkup)
index_html = index_html.replace('<div style="font-size:1.8rem; line-height:1;">⚡</div>', svg_quiz)
index_html = index_html.replace('<div style="font-size:1.4rem; margin-bottom:6px;">⚖️</div>', svg_bmi)
index_html = index_html.replace('<div style="font-size:1.4rem; margin-bottom:6px;">🔥</div>', svg_calorie)
index_html = index_html.replace('<div style="font-size:1.4rem; margin-bottom:6px;">🍗</div>', svg_protein)
index_html = index_html.replace('<div style="font-size:1.4rem; margin-bottom:6px;">🏃</div>', svg_exercise)
index_html = index_html.replace('<div style="font-size:1.4rem; margin-bottom:6px;">💧</div>', svg_water)
index_html = index_html.replace('<div style="font-size:1.4rem; margin-bottom:6px;">☕</div>', svg_caffeine)
index_html = index_html.replace('<div style="font-size:1.4rem; margin-bottom:6px;">🍺</div>', svg_alcohol)
index_html = index_html.replace('<div style="font-size:1.4rem; margin-bottom:6px;">💊</div>', svg_supplement)

# Replace remaining text emojis in index.html
index_html = index_html.replace('📚 분야별 핵심 건강 가이드', '분야별 핵심 건강 가이드')
index_html = index_html.replace('🥗 식단 &amp; 영양 관리 가이드', '식단 및 영양 관리 가이드')
index_html = index_html.replace('💡 건강노트가 추구하는 근거 중심 건강 관리 원칙', '건강노트의 근거 중심 건강 관리 원칙')
index_html = index_html.replace('📚 인기 건강 주제', '인기 건강 주제')
index_html = index_html.replace('<h2>📖 건강 칼럼</h2>', '<h2>건강 칼럼</h2>')
index_html = index_html.replace('<p class="disclaimer">⚠️ 건강노트의 모든 글과', '<p class="disclaimer">[안내] 건강노트의 모든 글과')

index_file.write_text(index_html, encoding="utf-8")
print("Cleaned index.html")

# 2. Update about.html
about_file = REPO_DIR / "about.html"
about_html = about_file.read_text(encoding="utf-8")
about_html = about_html.replace('<div class="value-icon">📖</div>', '<div class="value-icon" style="font-size:1.2rem; font-weight:800; color:#0284c7;">01</div>')
about_html = about_html.replace('<div class="value-icon">🩺</div>', '<div class="value-icon" style="font-size:1.2rem; font-weight:800; color:#0284c7;">02</div>')
about_html = about_html.replace('<div class="value-icon">🙋</div>', '<div class="value-icon" style="font-size:1.2rem; font-weight:800; color:#0284c7;">03</div>')
about_html = about_html.replace('<div class="value-icon">⚖️</div>', '<div class="value-icon" style="font-size:1.2rem; font-weight:800; color:#0284c7;">04</div>')
about_html = about_html.replace('<div class="disclaimer">⚠️ 건강노트는', '<div class="disclaimer">[법적 고지] 건강노트는')
about_file.write_text(about_html, encoding="utf-8")
print("Cleaned about.html")

# 3. Update contact.html
contact_file = REPO_DIR / "contact.html"
contact_html = contact_file.read_text(encoding="utf-8")
svg_mail = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#007bff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; vertical-align:middle;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>'
svg_clock = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#007bff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; vertical-align:middle;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'
contact_html = contact_html.replace('<span class="contact-icon">📧</span>', f'<span class="contact-icon">{svg_mail}</span>')
contact_html = contact_html.replace('<span class="contact-icon">⏱️</span>', f'<span class="contact-icon">{svg_clock}</span>')
contact_file.write_text(contact_html, encoding="utf-8")
print("Cleaned contact.html")

# 4. Update routine.html
routine_file = REPO_DIR / "routine.html"
routine_html = routine_file.read_text(encoding="utf-8")
# Remove emojis from supplement definitions
routine_html = re.sub(r'icon:\s*"[^"]*",', 'icon: "",', routine_html)
routine_html = routine_html.replace('<span>${s.icon}</span> <span>${s.name}</span>', '<span>${s.name}</span>')
routine_html = routine_html.replace('🌅 기상 직후 (아침 공복)', '기상 직후 (아침 공복)')
routine_html = routine_html.replace('🌆 저녁 식사 직후', '저녁 식사 직후')
routine_file.write_text(routine_html, encoding="utf-8")
print("Cleaned routine.html")

# 5. Update checkup.html
checkup_file = REPO_DIR / "checkup.html"
checkup_html = checkup_file.read_text(encoding="utf-8")
checkup_html = checkup_html.replace('🎯 우선순위 추천 행동 가이드', '우선순위 추천 행동 가이드')
checkup_html = checkup_html.replace('🔴 적극적 집중 관리 및 전문의 진료 권장', '[집중 관리] 전문의 상담 및 정밀 검진 권장')
checkup_html = checkup_html.replace('🟡 주의 필요: 골든타임 생활습관 개선 단계', '[주의 단계] 식단 및 생활습관 적극 개선 필요')
checkup_html = checkup_html.replace('🟢 매우 우수: 현재의 건강한 습관 유지', '[정상 기준] 현재의 건강한 생활습관 유지 권장')
checkup_file.write_text(checkup_html, encoding="utf-8")
print("Cleaned checkup.html")

# 6. Update quiz.html
quiz_file = REPO_DIR / "quiz.html"
quiz_html = quiz_file.read_text(encoding="utf-8")
quiz_html = quiz_html.replace('📖 맞춤 추천 건강노트 심층 가이드', '맞춤 추천 건강노트 심층 가이드')
quiz_file.write_text(quiz_html, encoding="utf-8")
print("Cleaned quiz.html")

# 7. Update caffeine.html
caffeine_file = REPO_DIR / "caffeine.html"
caffeine_html = caffeine_file.read_text(encoding="utf-8")
caffeine_html = caffeine_html.replace('🥤 믹스커피 / 캔커피', '믹스커피 / 캔커피')
caffeine_html = caffeine_html.replace('🍵 녹차 / 홍차 / 콜라', '녹차 / 홍차 / 콜라')
caffeine_html = caffeine_html.replace('🟢 적정하고 안전한 수준입니다. 피로 회복과 집중에 도움이 됩니다.', '[안전] 적정하고 안전한 수준입니다. 피로 회복과 집중에 도움이 됩니다.')
caffeine_html = caffeine_html.replace('🟡 성인 하루 상한선에 근접했습니다. 오후 늦은 시간에는 디카페인을 권장합니다.', '[주의] 성인 하루 상한선에 근접했습니다. 늦은 시간에는 섭취를 제한하세요.')
caffeine_html = caffeine_html.replace('🔴 성인 최대 권장 한도(400mg)를 초과했습니다! 가슴 두근거림이나 불면증에 유의하세요.', '[초과 경고] 성인 일일 최대 안전 한도(400mg)를 초과했습니다! 추가 섭취를 중단하세요.')
caffeine_file.write_text(caffeine_html, encoding="utf-8")
print("Cleaned caffeine.html")

print("All remaining emojis cleaned successfully!")

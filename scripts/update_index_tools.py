import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Group 1: 3 signature tools (routine, checkup, quiz)
# Replace svg icon with rich thumbnail preview
# routine
routine_pat = r'(<a href="/routine"[^>]*>)\s*<div style="width:38px; height:38px;[^"]*">[\s\S]*?</div>'
routine_repl = r'''\1
            <div style="width:105px; height:78px; border-radius:10px; overflow:hidden; flex-shrink:0; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
              <img src="/images/thumbnails/banner_routine.jpg" alt="영양제 복용 시간표 플래너" style="width:100%; height:100%; object-fit:cover; display:block;">
            </div>'''
html = re.sub(routine_pat, routine_repl, html, count=1)

# checkup
checkup_pat = r'(<a href="/checkup"[^>]*>)\s*<div style="width:38px; height:38px;[^"]*">[\s\S]*?</div>'
checkup_repl = r'''\1
            <div style="width:105px; height:78px; border-radius:10px; overflow:hidden; flex-shrink:0; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
              <img src="/images/thumbnails/banner_checkup.jpg" alt="건강검진 수치 판독 리포트" style="width:100%; height:100%; object-fit:cover; display:block;">
            </div>'''
html = re.sub(checkup_pat, checkup_repl, html, count=1)

# quiz
quiz_pat = r'(<a href="/quiz"[^>]*>)\s*<div style="width:38px; height:38px;[^"]*">[\s\S]*?</div>'
quiz_repl = r'''\1
            <div style="width:105px; height:78px; border-radius:10px; overflow:hidden; flex-shrink:0; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
              <img src="/images/thumbnails/banner_quiz.jpg" alt="30초 맞춤 건강 자가진단 퀴즈" style="width:100%; height:100%; object-fit:cover; display:block;">
            </div>'''
html = re.sub(quiz_pat, quiz_repl, html, count=1)

# 2. Update Group 2: Diet tools (bmi, calorie, protein, exercise)
# Replace 32x32 svg icon with full top banner
diet_tools = [
    ('bmi', 'BMI·표준체중 비만도 계산기'),
    ('calorie', '하루 칼로리·기초대사량(BMR) 계산기'),
    ('protein', '단백질 권장 섭취량 계산기'),
    ('exercise', '운동별 소모 칼로리 계산기')
]

for tid, ttitle in diet_tools:
    pat = rf'(<a href="/{tid}"[^>]*>\s*<div>)\s*<div style="width:32px; height:32px;[^"]*">[\s\S]*?</div>'
    repl = rf'''\1
              <div style="width:100%; height:110px; border-radius:8px; overflow:hidden; margin-bottom:12px; box-shadow:0 2px 6px rgba(0,0,0,0.06);">
                <img src="/images/thumbnails/banner_{tid}.jpg" alt="{ttitle}" style="width:100%; height:100%; object-fit:cover; display:block;">
              </div>'''
    html = re.sub(pat, repl, html, count=1)

# 3. Update Group 3: Lifestyle tools (water, caffeine, alcohol, supplement)
life_tools = [
    ('water', '하루 물 섭취량 계산기'),
    ('caffeine', '카페인 안전량 계산기'),
    ('alcohol', '알코올 분해시간 계산기'),
    ('supplement', '영양제 권장·상한량 조회')
]

for tid, ttitle in life_tools:
    pat = rf'(<a href="/{tid}"[^>]*>\s*<div>)\s*<div style="width:32px; height:32px;[^"]*">[\s\S]*?</div>'
    repl = rf'''\1
              <div style="width:100%; height:110px; border-radius:8px; overflow:hidden; margin-bottom:12px; box-shadow:0 2px 6px rgba(0,0,0,0.06);">
                <img src="/images/thumbnails/banner_{tid}.jpg" alt="{ttitle}" style="width:100%; height:100%; object-fit:cover; display:block;">
              </div>'''
    html = re.sub(pat, repl, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated with beautiful tool thumbnails successfully!")

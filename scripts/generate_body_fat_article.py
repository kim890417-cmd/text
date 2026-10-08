import os
import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Template from cholesterol-test-results-guide
template_path = REPO_DIR / "health" / "cholesterol-test-results-guide" / "index.html"
template = template_path.read_text(encoding="utf-8-sig")

slug = "body-fat-loss-calorie-deficit-calculator"
title = "체지방 1kg 빼는 칼로리와 현실적인 일일 감량 식단 계산법"
meta_desc = "체지방 1kg을 빼려면 정확히 7,700kcal의 에너지 적자가 필요합니다. 기초대사량과 활동대사량(TDEE) 계산법, 요요 없는 하루 500kcal 적자 식단 및 운동 소모 칼로리 공식을 정리했습니다."
published_iso = "2026-10-08T18:00:00+09:00"
modified_iso = "2026-10-08T18:00:00+09:00"
display_date = "10월 8, 2026"
img_url = "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=800&h=450&fit=crop&q=80"
img_alt = "체지방 1kg 감량에 필요한 칼로리 적자 계산과 다이어트 식단"
tags = ["체지방 1kg", "칼로리 계산기", "TDEE", "기초대사량", "다이어트 식단", "운동 소모 칼로리"]

body_html = """
<p>다이어트를 결심하고 체중계에 올라선 첫 주, 물만 덜 마셔도 1~2kg은 뚝 떨어집니다. 하지만 이건 지방이 빠진 게 아니라 체내 수분과 글리코겐이 빠져나간 일시적인 착시에 불과합니다. 우리가 진짜 빼야 하는 순수 체지방 1kg을 태워 없애려면 정확히 <strong>7,700kcal</strong>라는 막대한 에너지 결손(Calorie Deficit)을 만들어내야 합니다.</p>

<p>저 역시 과거 방송 제작(PD) 시절, 빡빡한 촬영 마감에 쫓기다 2주 만에 5kg을 빼겠다고 하루에 고구마 한 개와 아메리카노만 들이붓는 극단적인 초저열량 단식을 감행했던 적이 있습니다. (지금 생각하면 몸을 망치는 미련한 짓이었죠.) 결과는 어땠을까요? 체중계 바늘은 잠깐 내려갔지만 얼굴은 흙빛이 되었고, 극심한 탈모와 무기력증, 그리고 뇌에서 터져 나온 끔찍한 보상성 폭식으로 3주 만에 원래 체중보다 4kg이 더 찌는 처참한 요요를 맞았습니다. 게다가 망가진 위장 점막 때문에 수개월 동안 속 쓰림으로 병원을 다녀야 했습니다.</p>

<p>대학에서 식품학을 공부하며 인체 생화학과 대사 메커니즘을 다시 복기했을 때 비로소 진실이 보였습니다. 체지방은 무작정 굶는다고 빠지는 게 아닙니다. <strong>내 몸의 하루 유지 칼로리(TDEE)를 정확히 파악하고, 하루 500~700kcal의 안전한 적자 폭을 설계하여 몸이 눈치채지 못하게 지방만 태우는 것</strong>이 요요 없는 다이어트의 유일한 과학적 정답입니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>체지방 1kg이 정확히 7,700kcal인 과학적 이유</h2>
<p><strong>순수 지방 1g의 열량은 9kcal이지만, 인체 체지방 조직은 순수 지방 약 87%와 수분·단백질 세포 기질 약 13%로 이루어져 있어 체지방 1kg을 완전히 연소하려면 약 7,700kcal의 에너지 적자가 필요합니다.</strong></p>

<p>많은 분들이 "지방 1g이 9kcal니까 1kg(1,000g)이면 9,000kcal를 태워야 하는 것 아닌가?"라고 오해하십니다. 하지만 우리 몸의 지방세포(Adipocyte)는 순수한 기름 덩어리가 아닙니다. 세포벽과 결합조직 단백질, 그리고 약간의 세포 내 수분이 13%가량 포함되어 있습니다.</p>

<ul>
  <li><strong>계산 공식:</strong> 1,000g × 87% (순수 트리글리세리드) = 870g</li>
  <li><strong>총 에너지 환산:</strong> 870g × 9kcal/g = <strong>7,830kcal</strong> (대사 소모율 감안 시 통상 <strong>7,700kcal</strong>로 정의)</li>
</ul>

<p>이 7,700kcal라는 숫자가 왜 중요할까요? 하루아침에 굶는다고 해서 체지방 1kg이 빠질 수 없다는 차가운 생리학적 한계를 증명하기 때문입니다. 성인의 하루 총 대사량이 2,000kcal 안팎인데, 하루를 통째로 굶어도 기껏해야 2,000kcal 결손입니다. 체지방 환산으로는 겨우 260g 남짓입니다. 단식 하루 만에 체중이 1.5kg 빠졌다면, 1.2kg 이상은 소변과 글리코겐 결합 수분이 빠져나간 신기루입니다. 체중계 숫자에 속아 일희일비할 필요가 전혀 없는 이유입니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>내 몸의 유지 칼로리(TDEE)와 일일 감량 적자 계산법</h2>
<p>체지방을 빼기 위한 첫 번째 실천 단계는 "내가 하루에 가만히 있어도 쓰는 에너지"와 "활동하며 쓰는 총에너지"를 숫자로 정확히 산출하는 것입니다. 이를 <strong>TDEE (Total Daily Energy Expenditure, 일일 총에너지 소비량)</strong>라고 부릅니다.</p>

<table>
  <thead>
    <tr>
      <th>단계</th>
      <th>산출 지표</th>
      <th>계산 원리 및 설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1단계</strong></td>
      <td><strong>기초대사량 (BMR)</strong></td>
      <td>심장 박동, 호흡, 체온 유지 등 생명 유지에 드는 최소 열량 (미플린-세인트 지어 공식 권장)</td>
    </tr>
    <tr>
      <td><strong>2단계</strong></td>
      <td><strong>활동대사량 (TDEE)</strong></td>
      <td>BMR × 활동계수 (좌식 1.2, 가벼운 운동 1.375, 보통 활동 1.55, 활동적 1.725)</td>
    </tr>
    <tr>
      <td><strong>3단계</strong></td>
      <td><strong>목표 섭취 칼로리</strong></td>
      <td><strong>TDEE - 500kcal</strong> (안전한 감량을 위한 매일의 식사 목표치)</td>
    </tr>
  </tbody>
</table>

<p>왜 하필 '하루 500kcal 적자'일까요? 계산기를 두드려보면 명쾌한 답이 나옵니다.</p>
<ul>
  <li>하루 500kcal 적자 × 15일 = <strong>7,500kcal 적자</strong> (약 2주 만에 순수 체지방 1kg 감량)</li>
  <li>하루 500kcal 적자 × 30일 = <strong>15,000kcal 적자</strong> (한 달에 순수 체지방 약 2kg 감량)</li>
</ul>

<p>미국스포츠의학회(ACSM)와 보건복지부 비만 진료지침에서도 <strong>한 달에 자기 체중의 2~3kg (또는 체중의 5% 이내) 감량을 가장 이상적이고 안전한 속도</strong>로 권고합니다. 이보다 빠른 속도로 빼려고 하루 1,000kcal 이상 굶어버리면, 몸은 기아 상태(Starvation Mode)로 인식해 렙틴 호르몬을 억제하고 기초대사량을 강제로 깎아내립니다. 나중에 밥 반 공기만 더 먹어도 살이 찌는 최악의 '체질 변화'가 시작되는 것입니다.</p>

<div style="background:#f0f9ff; border:1.5px solid #bae6fd; border-radius:12px; padding:20px; margin:28px 0;">
  <strong style="color:#0369a1; font-size:1.05rem; display:block; margin-bottom:6px;">[실시간 계산] 나의 기초대사량(BMR) &amp; 유지 칼로리(TDEE) 확인하기</strong>
  <p style="font-size:0.92rem; color:#475569; margin:0 0 14px; line-height:1.5;">복잡한 공식으로 직접 계산할 필요 없습니다. 성별, 나이, 키, 체중, 평소 활동량을 입력하시면 나의 TDEE와 감량 목표별 섭취 칼로리를 즉시 산출해 드립니다.</p>
  <a href="/calorie" style="display:inline-block; background:#0284c7; color:#fff; padding:10px 20px; border-radius:8px; font-weight:700; text-decoration:none; font-size:0.9rem;">하루 칼로리·기초대사량 계산기 바로가기 →</a>
</div>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>식단 300kcal 절감 + 운동 200kcal 소모: 황금 분할 전략</h2>
<p>하루 500kcal 적자를 만들 때 가장 흔히 저지르는 실수가 <strong>"식단으로만 500kcal를 덜 먹으려는 것"</strong>입니다. 평소 2,000kcal를 먹던 사람이 갑자기 1,500kcal로 줄이면 1주일도 못 가 야식의 유혹에 무너집니다. 식욕 억제 호르몬 그렐린이 폭발하기 때문입니다.</p>

<p>성공률을 90% 이상 끌어올리는 현실적인 분할 전략은 <strong>식단에서 300kcal 줄이고, 운동으로 200kcal를 추가 연소</strong>하는 것입니다.</p>

<h3>1. 식단에서 300kcal 줄이기 (눈에 띄는 식판의 변화)</h3>
<ul>
  <li>매 끼니 밥공기의 1/4을 덜어내기 (하루 3끼 합산 약 200~250kcal 절감)</li>
  <li>설탕 든 믹스커피나 달콤한 음료를 블랙커피나 물로 전환 (하루 150~200kcal 절감)</li>
  <li>튀김류 반찬을 찜·구이류로 변경 (드레싱은 부먹 대신 찍먹)</li>
</ul>

<h3>2. 운동으로 200kcal 태우기 (METs 활동 계수 기준)</h3>
<p>운동 생리학에서 에너지 소비는 체중과 <strong>METs(신진대사 해당치)</strong> 공식으로 계산됩니다. 체중 70kg 성인 기준으로 200~250kcal를 소모하는 데 필요한 실제 운동량은 다음과 같습니다:</p>

<table>
  <thead>
    <tr>
      <th>운동 종목</th>
      <th>운동 강도 (METs)</th>
      <th>200kcal 소모 소요 시간 (체중 70kg 기준)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>빠르게 걷기 (시속 5.5km)</strong></td>
      <td>3.8 METs</td>
      <td>약 45분 (약 5,500~6,000보)</td>
    </tr>
    <tr>
      <td><strong>가벼운 조깅 (시속 8km)</strong></td>
      <td>8.0 METs</td>
      <td>약 22분</td>
    </tr>
    <tr>
      <td><strong>실내 자전거 (중간 저항)</strong></td>
      <td>6.8 METs</td>
      <td>약 26분</td>
    </tr>
    <tr>
      <td><strong>웨이트 트레이닝 (전신 서킷)</strong></td>
      <td>5.5 METs</td>
      <td>약 32분</td>
    </tr>
    <tr>
      <td><strong>계단 오르기</strong></td>
      <td>8.8 METs</td>
      <td>약 20분</td>
    </tr>
  </tbody>
</table>

<p>보시다시피 하루 40분 정도 빠르게 걷거나 20분 정도 가볍게 조깅하는 것만으로도 200kcal는 충분히 연소됩니다. 이렇게 식단 300kcal와 운동 200kcal가 결합되면, 배고픔에 허덕이지 않으면서도 매일 정확히 500kcal의 지방 연소 환경이 구축됩니다.</p>

<div style="background:#fefce8; border:1.5px solid #fde68a; border-radius:12px; padding:20px; margin:28px 0;">
  <strong style="color:#854d0e; font-size:1.05rem; display:block; margin-bottom:6px;">[실시간 계산] 내 체중 기준 운동별 실제 소모 칼로리 확인</strong>
  <p style="font-size:0.92rem; color:#475569; margin:0 0 14px; line-height:1.5;">체중이 60kg인 사람과 80kg인 사람은 같은 운동을 해도 소모 칼로리가 30% 이상 차이 납니다. 내 몸무게 기준 정밀 METs 소비 칼로리와 지방 연소량을 계산해 보세요.</p>
  <a href="/exercise" style="display:inline-block; background:#d97706; color:#fff; padding:10px 20px; border-radius:8px; font-weight:700; text-decoration:none; font-size:0.9rem;">운동 소모 칼로리 계산기 바로가기 →</a>
</div>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>근손실을 막고 체지방만 털어내는 단백질과 수분의 핵심 규칙</h2>
<p>칼로리 적자 다이어트를 진행할 때 인체 내부에서는 비상사태가 선포됩니다. 에너지가 부족해지면 간은 지방만 태우는 것이 아니라, 근육 단백질을 아미노산으로 분해해 포도당을 만들어내는 <strong>포도당신생합성(Gluconeogenesis)</strong>을 가동합니다. 즉, 방심하면 근육부터 빠져나갑니다.</p>

<p>제가 군 복무 시절 대위로 중대원들을 지휘하며 혹한기 야외 기동훈련을 뛸 때 뼈저리게 느낀 원칙이 있습니다. 악조건일수록 규칙적인 단백질과 수분 보급이 무너지면 병사들의 체력과 면역력은 며칠 만에 바닥을 드러냅니다. 다이어트 역시 내 몸과의 지구전입니다.</p>

<h3>1. 감량기 단백질 섭취량: 체중당 1.6g ~ 2.0g 확보</h3>
<ul>
  <li>평소 유지기에는 체중 1kg당 1.0~1.2g이면 충분하지만, <strong>칼로리 적자 감량기에는 근손실 억제를 위해 체중 1kg당 1.6~2.0g으로 단백질 비율을 높여야</strong> 합니다.</li>
  <li>체중 70kg 성인 기준: 하루 약 <strong>110g ~ 130g</strong>의 순수 단백질 섭취 필요.</li>
  <li>한 끼에 몰아서 먹으면 흡수 효율이 떨어지므로, 아침 30g / 점심 35g / 저녁 35g / 간식 15g처럼 3~4회로 분할 섭취하는 것이 생체 이용률을 극대화합니다.</li>
</ul>

<h3>2. 체중당 30~35ml의 충분한 수분 공급</h3>
<p>지방세포에 저장된 중성지방이 글리세롤과 유리지방산으로 분해되어 에너지로 쓰이려면 <strong>가수분해(Hydrolysis)</strong> 반응이 필수적입니다. 체내 수분이 부족하면 탈수 상태가 되어 지방 연소 효율이 20% 이상 저하됩니다. 또한 물은 식사 전 포만감을 주어 과식을 방지합니다.</p>

<div style="background:#f0fdf4; border:1.5px solid #bbf7d0; border-radius:12px; padding:20px; margin:28px 0;">
  <strong style="color:#166534; font-size:1.05rem; display:block; margin-bottom:6px;">[실시간 계산] 내 몸에 딱 맞는 하루 단백질 &amp; 수분 필요량 산출</strong>
  <p style="font-size:0.92rem; color:#475569; margin:0 0 14px; line-height:1.5;">현재 체중과 다이어트 강도에 맞춘 1일 단백질 권장량(g)과 수분 섭취량(L), 그리고 나의 현재 비만도(BMI) 상태를 아래 계산기로 점검해 보세요.</p>
  <div style="display:flex; gap:10px; flex-wrap:wrap;">
    <a href="/protein" style="display:inline-block; background:#16a34a; color:#fff; padding:8px 16px; border-radius:8px; font-weight:700; text-decoration:none; font-size:0.88rem;">단백질 계산기 →</a>
    <a href="/water" style="display:inline-block; background:#0891b2; color:#fff; padding:8px 16px; border-radius:8px; font-weight:700; text-decoration:none; font-size:0.88rem;">물 섭취량 계산기 →</a>
    <a href="/bmi" style="display:inline-block; background:#475569; color:#fff; padding:8px 16px; border-radius:8px; font-weight:700; text-decoration:none; font-size:0.88rem;">BMI·표준체중 계산기 →</a>
  </div>
</div>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>다이어터들이 가장 많이 빠지는 3가지 치명적 함정</h2>
<ol>
  <li><strong>주말 치팅데이로 평일 적자 전부 날리기:</strong> 월~금 5일간 매일 500kcal씩 줄여 가까스로 2,500kcal 적자를 만들어놓고, 토요일 저녁 삼겹살에 소주와 볶음밥으로 3,000kcal를 폭식하면 한 주의 노력이 0이 아니라 플러스가 됩니다. 치팅은 '폭식의 날'이 아니라 평소 부족했던 '클린 탄수화물 재충전(Refeed)'이어야 합니다.</li>
  <li><strong>매일 아침 체중계 소수점에 집착하기:</strong> 전날 짠 음식을 먹었거나 근력 운동 후 근육에 염증 반응이 생기면 몸이 수분을 머금어 체중이 1~2kg 늘어납니다. 지방이 찐 게 아닙니다. 매일의 체중보다 주간 평균 체중과 허리둘레(눈바디)의 변화를 신뢰하세요.</li>
  <li><strong>액상과당과 숨은 오일 방심하기:</strong> 샐러드를 먹으면서 마요네즈 기반 드레싱을 듬뿍 뿌리거나, 무설탕이라 적힌 음료의 당알코올을 간과하면 알게 모르게 300kcal가 추가됩니다. 식품 성분표의 원재료명을 꼼꼼히 확인하세요.</li>
</ol>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>에디터의 3줄 요약과 오늘 당장 실천할 1가지</h2>
<ul>
  <li><strong>핵심 1:</strong> 체지방 1kg 감량에는 7,700kcal 적자가 필요하며, 현실적인 목표는 하루 500kcal 결손으로 2주에 1kg(한 달 2kg)을 빼는 것입니다.</li>
  <li><strong>핵심 2:</strong> 굶어서 빼지 말고, 식단에서 밥 1/4공기 줄이기(300kcal)와 40분 걷기 운동(200kcal)의 황금 분할을 실천하세요.</li>
  <li><strong>핵심 3:</strong> 체지방만 태우려면 체중 1kg당 1.6~2.0g의 단백질과 충분한 수분을 공급해 기초대사량을 지켜내야 합니다.</li>
</ul>

<p>오늘 글을 읽고 당장 하셔야 할 행동은 단 하나입니다. 스마트폰을 켜고 <a href="/calorie">하루 칼로리 계산기</a>에 내 키와 몸무게를 넣어 나의 <strong>TDEE(유지 칼로리)</strong>를 메모장에 적어두세요. 내 출발점이 몇 칼로리인지 아는 순간, 막연했던 다이어트의 안개가 걷히고 선명한 지도가 펼쳐질 것입니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>참고자료</h2>
<ul>
  <li>보건복지부·한국영양학회 – 2020 한국인 영양소 섭취기준 (에너지 및 다량영양소 대사 지침)</li>
  <li>질병관리청 국가건강정보포털 – 비만 예방을 위한 신체활동 및 식사 가이드라인</li>
  <li>American College of Sports Medicine (ACSM) – Appropriate Physical Activity Intervention Strategies for Weight Loss and Prevention of Weight Regain for Adults</li>
  <li>Hall KD, et al. – Quantification of the effect of energy imbalance on bodyweight. The Lancet.</li>
</ul>

<blockquote><p>[법적 고지] 본 칼럼은 공인된 스포츠의학 및 영양학 학술 데이터를 바탕으로 작성된 일반 건강 정보입니다. 당뇨, 신장 질환, 갑상선 기능 이상 등 기저질환이 있는 분은 칼로리 제한 식단을 시작하기 전 반드시 내과 전문의 및 임상영양사와의 개별 상담을 우선하시기 바랍니다.</p></blockquote>
"""

# 2. Build HTML from template
art_dir = REPO_DIR / "health" / slug
art_dir.mkdir(parents=True, exist_ok=True)
art_file = art_dir / "index.html"

content = template

# Title & Meta
content = re.sub(r"<title>.*?</title>", f"<title>{title} | 건강노트</title>", content)
content = re.sub(r'<meta name="description" content=".*?"/>', f'<meta name="description" content="{meta_desc}"/>', content)
content = re.sub(r'<meta property="og:title" content=".*?" />', f'<meta property="og:title" content="{title}" />', content)
content = re.sub(r'<meta property="og:description" content=".*?" />', f'<meta property="og:description" content="{meta_desc}" />', content)
content = re.sub(r'<meta property="og:url" content=".*?" />', f'<meta property="og:url" content="https://healthfit100.com/health/{slug}/" />', content)
content = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="https://healthfit100.com/health/{slug}/" />', content)
content = re.sub(r'<meta name="twitter:title" content=".*?" />', f'<meta name="twitter:title" content="{title}" />', content)
content = re.sub(r'<meta name="twitter:description" content=".*?" />', f'<meta name="twitter:description" content="{meta_desc}" />', content)
content = re.sub(r'<meta property="article:published_time" content=".*?" />', f'<meta property="article:published_time" content="{published_iso}" />', content)
content = re.sub(r'<meta property="article:modified_time" content=".*?" />', f'<meta property="article:modified_time" content="{modified_iso}" />', content)
content = re.sub(r'<meta property="og:updated_time" content=".*?" />', f'<meta property="og:updated_time" content="{modified_iso}" />', content)

# Schema JSON
content = re.sub(r'https://healthfit100.com/health/cholesterol-test-results-guide/', f'https://healthfit100.com/health/{slug}/', content)
content = re.sub(r'2026-08-07T09:00:00\+09:00', published_iso, content)
content = re.sub(r'2026-08-08T17:32:54\+09:00', modified_iso, content)

# Entry Title & Date
content = re.sub(r'<h1 class="entry-title" itemprop="headline">.*?</h1>', f'<h1 class="entry-title" itemprop="headline">{title}</h1>', content)
content = re.sub(r'<span class="published" itemprop="datePublished">.*?</span>', f'<span class="published" itemprop="datePublished"> {display_date} </span>', content)

# Insert Image
fig_html = f'''<figure class="post-thumb-img-content" style="margin:0 0 1.5em 0;border-radius:8px;overflow:hidden;text-align:center;">
<img src="{img_url}" alt="{img_alt}" width="800" height="450" loading="lazy" style="width:100%;height:auto;display:block;object-fit:cover;">
<figcaption style="font-size:12px;color:#888888;margin-top:6px;text-align:center;">사진 출처: Unsplash</figcaption>
</figure>'''

if '<header class="entry-header ">' in content:
    content = content.replace('<header class="entry-header ">', f'{fig_html}\n<header class="entry-header ">', 1)

# Replace entry-content
start_tag = '<div class="entry-content clear"\n\titemprop="text"\t>'
if start_tag not in content:
    start_tag = '<div class="entry-content clear" itemprop="text">'
if start_tag not in content:
    m = re.search(r'<div class="entry-content clear"[^>]*>', content)
    if m:
        start_tag = m.group(0)

end_tag = '</div><!-- .entry-content .clear -->'

parts = content.split(start_tag)
before_body = parts[0] + start_tag
after_body = end_tag + parts[1].split(end_tag)[1]

full_art_html = before_body + "\n" + body_html + "\n" + after_body
art_file.write_text(full_art_html, encoding="utf-8")
print(f"Created article: {art_file}")

# 3. Add to blog.html list
blog_file = REPO_DIR / "blog.html"
blog_html = blog_file.read_text(encoding="utf-8")

new_post_card = f'''<article class="post-356 post type-post status-publish format-standard has-post-thumbnail hentry ast-article-post" style="border:1px solid #e2e8f0; border-radius:12px; padding:20px; box-shadow:0 4px 12px rgba(15,23,42,.04); margin-bottom:20px; background:#fff;">
  <div class="post-content" style="display:grid; grid-template-columns:220px minmax(0,1fr); column-gap:24px; align-items:start;">
    <div class="post-thumb-img-content" style="border-radius:8px; overflow:hidden;">
      <a href="/health/{slug}/">
        <img src="{img_url}" alt="{img_alt}" width="220" height="140" style="width:100%; height:140px; object-fit:cover; display:block;">
      </a>
    </div>
    <div class="entry-header">
      <div class="entry-meta" style="font-size:0.85rem; color:#64748b; margin-bottom:6px;">
        <span>건강,영양</span> · <span>{display_date}</span>
      </div>
      <h2 class="entry-title" style="font-size:1.22rem; font-weight:700; margin:0 0 8px; line-height:1.4;">
        <a href="/health/{slug}/" style="color:#0f172a; text-decoration:none;">{title}</a>
      </h2>
      <p style="font-size:0.9rem; color:#475569; margin:0 0 10px; line-height:1.5;">{meta_desc}</p>
      <div style="font-size:0.8rem; color:#0284c7; font-weight:600;">
        연관 계산기: <a href="/calorie" style="color:#0284c7; text-decoration:underline;">하루 칼로리·기초대사량</a> · <a href="/exercise" style="color:#0284c7; text-decoration:underline;">운동 소모 칼로리</a>
      </div>
    </div>
  </div>
</article>'''

# Insert after <div class="ast-row"> or at the top of post list
if '<div class="ast-row">' in blog_html:
    blog_html = blog_html.replace('<div class="ast-row">', f'<div class="ast-row">\n{new_post_card}', 1)
    blog_file.write_text(blog_html, encoding="utf-8")
    print("Added new article card to blog.html")

# 4. Add to index.html featured list
index_file = REPO_DIR / "index.html"
index_html = index_file.read_text(encoding="utf-8")

new_index_card = f'''        <div style="background:#fff; border:1px solid #e2e8f0; border-radius:14px; padding:20px; box-shadow:0 4px 12px rgba(15,23,42,0.03); display:flex; gap:20px; align-items:center;">
          <img src="{img_url}" alt="{img_alt}" style="width:160px; height:105px; border-radius:10px; object-fit:cover; flex-shrink:0;">
          <div style="flex:1;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span style="background:#eff6ff; color:#2563eb; font-size:0.75rem; font-weight:700; padding:2px 8px; border-radius:999px;">체중·칼로리 분석</span>
              <span style="font-size:0.8rem; color:#94a3b8;">{display_date}</span>
            </div>
            <h3 style="margin:0 0 6px; font-size:1.1rem; font-weight:700;">
              <a href="/health/{slug}/" style="color:#0f172a; text-decoration:none;">{title}</a>
            </h3>
            <p style="margin:0 0 8px; font-size:0.88rem; color:#64748b; line-height:1.4;">체지방 1kg을 빼기 위한 7,700kcal 적자 원리와 TDEE 유지 칼로리, 단백질·운동 결합 공식</p>
            <div style="font-size:0.78rem; color:#0284c7; font-weight:600;">
              연관 도구: <a href="/calorie" style="color:#0284c7; text-decoration:underline;">기초대사량·TDEE 계산기</a> · <a href="/exercise" style="color:#0284c7; text-decoration:underline;">운동 소모 칼로리</a>
            </div>
          </div>
        </div>'''

# Insert in index.html post list
marker = '<div style="display:flex;flex-direction:column;gap:18px;margin-bottom:55px;">'
if marker in index_html:
    index_html = index_html.replace(marker, f'{marker}\n{new_index_card}')
    index_file.write_text(index_html, encoding="utf-8")
    print("Added new article card to index.html")

print("Article generation script finished successfully!")

import os
import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Base template from blood-sugar-spike-prevention-diet
template_path = REPO_DIR / "health" / "blood-sugar-spike-prevention-diet" / "index.html"
template = template_path.read_text(encoding="utf-8")

slug = "fasting-blood-sugar-normal-range-prediabetes"
title = "공복 혈당 정상 수치 기준과 당뇨 전단계 낮추는 법, 당화혈색소(HbA1c) 관리 가이드"
meta_desc = "국가건강검진 공복 혈당 정상 수치(100 mg/dL 미만)와 당뇨 전단계(100~125 mg/dL) 기준, 당화혈색소(HbA1c 5.7~6.4%) 해석법 및 인슐린 저항성을 개선하는 생활수칙을 정리했습니다."
published_iso = "2026-10-09T09:00:00+09:00"
modified_iso = "2026-10-09T09:00:00+09:00"
display_date = "10월 9, 2026"
post_id = "410"

body_html = """
<p>건강검진 결과지를 받아 들었을 때 공복 혈당 칸에 적힌 '108' 또는 '115'라는 숫자를 보고 당황하셨던 경험, 직장인이라면 한 번쯤 겪어보셨을 겁니다. "아직 당뇨병은 아니니까 괜찮겠지"라며 대수롭지 않게 넘기기 쉽지만, 의학적으로 이 구간은 이미 췌장이 비명을 지르기 시작한 <strong>'공복혈당장애(당뇨병 전단계)'</strong>입니다.</p>

<p>저 역시 과거 방송 제작(PD) 시절, 며칠 밤을 새우며 편집실에서 믹스커피와 컵라면으로 끼니를 때우던 시절이 있었습니다. 30대 초반에 받은 종합검진에서 공복 혈당이 114 mg/dL로 찍혀 나온 것을 보고 의사 선생님이 "이대로 2년만 더 살면 곧바로 당뇨약 처방 들어갑니다"라고 엄중히 경고하셨던 기억이 아직도 생생합니다. (그때는 젊음만 믿고 간식이 대사에 미치는 독성을 전혀 몰랐었죠.)</p>

<p>식품학을 전공하며 영양소 대사와 호르몬 회로를 집요하게 파고들었을 때 깨달은 사실은 분명했습니다. 공복 혈당 100~125 mg/dL 구간은 질병으로 굳어지기 전, <strong>내 몸의 인슐린 감수성을 정상으로 되돌릴 수 있는 '마지막 골든타임'</strong>이라는 점입니다. 오늘 공복 혈당의 진짜 의미와 당화혈색소 판독법, 그리고 약 없이 수치를 안정화시키는 핵심 실천법을 정리해 드립니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>공복 혈당 정상 수치와 당뇨 전단계 위험 기준</h2>
<p><strong>공복 혈당의 성인 정상 기준은 100 mg/dL 미만이며, 100~125 mg/dL은 공복혈당장애(당뇨 전단계), 126 mg/dL 이상은 당뇨병으로 진단되어 적극적인 치료와 관리가 필요합니다.</strong></p>

<p>공복 혈당(Fasting Blood Sugar)이란 최소 8시간 이상(권장 10~12시간) 물 이외의 음식이나 음료를 전혀 섭취하지 않은 상태에서 정맥혈을 채취해 측정한 혈중 포도당 농도를 뜻합니다. 밤새 음식을 먹지 않았는데도 혈액 속에 당분이 많이 남아있다는 것은, 간에서 포도당을 지나치게 많이 뿜어내고 있거나 근육 세포가 당을 제대로 흡수하지 못하고 있다는 명백한 증거입니다.</p>

<table>
  <thead>
    <tr>
      <th>진단 구분</th>
      <th>공복 혈당 (mg/dL)</th>
      <th>식후 2시간 혈당 (mg/dL)</th>
      <th>당화혈색소 (HbA1c, %)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>정상 범위</strong></td>
      <td><strong>70 ~ 99 미만</strong></td>
      <td><strong>140 미만</strong></td>
      <td><strong>5.6 이하</strong></td>
    </tr>
    <tr>
      <td><strong>당뇨 전단계</strong></td>
      <td><strong>100 ~ 125</strong> (공복혈당장애)</td>
      <td><strong>140 ~ 199</strong> (내당능장애)</td>
      <td><strong>5.7 ~ 6.4</strong></td>
    </tr>
    <tr>
      <td><strong>당뇨병 진단</strong></td>
      <td><strong>126 이상</strong></td>
      <td><strong>200 이상</strong></td>
      <td><strong>6.5 이상</strong></td>
    </tr>
  </tbody>
</table>

<p>질병관리청 국민건강영양조사에 따르면 국내 30세 이상 성인 10명 중 3명이 이미 당뇨 전단계에 해당합니다. 문제는 당뇨 전단계 환자의 약 30~50%가 특별한 관리 없이 지낼 경우 5~10년 이내에 진짜 당뇨병 환자로 전환된다는 통계입니다. 혈관 내피세포 손상과 동맥경화 위험은 이미 '전단계' 상태에서부터 정상인 대비 1.5~2배 이상 치솟기 시작합니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>검진 전날 굶어도 못 속이는 '당화혈색소(HbA1c)'의 진실</h2>
<p>건강검진을 앞두고 전날 저녁을 굶거나 며칠간 식사를 조절하면 당일 아침 공복 혈당은 일시적으로 90대로 낮게 나올 수 있습니다. 하지만 혈액검사 항목 중 <strong>당화혈색소(HbA1c)</strong>는 절대로 속일 수 없습니다.</p>

<ul>
  <li><strong>당화혈색소의 생성 원리:</strong> 혈액 속 적혈구에는 산소를 운반하는 단백질인 헤모글로빈이 들어 있습니다. 혈당이 높으면 포도당이 헤모글로빈에 달라붙어 떨어지지 않는 결합체를 만드는데, 이것이 당화혈색소입니다.</li>
  <li><strong>2~3개월의 평균 성적표:</strong> 적혈구의 평균 수명은 약 120일(4개월)입니다. 따라서 당화혈색소 수치를 측정하면 검진 직전의 식사와 무관하게, 지난 2~3개월 동안 내 혈관이 얼마나 높은 당분에 절여져 있었는지를 백분율(%)로 정확히 알 수 있습니다.</li>
  <li><strong>판독 기준:</strong> 5.6% 이하라면 매우 건강한 상태입니다. <strong>5.7%부터 6.4%까지는 당뇨 전단계</strong>로 분류되며, 6.5%를 넘어가면 공복 혈당 수치와 관계없이 당뇨병으로 공식 진단됩니다.</li>
</ul>

<p>만약 공복 혈당이 98 mg/dL로 정상 커트라인에 걸쳐 있더라도 당화혈색소가 5.9%라면, 낮 시간대나 식후에 심한 혈당 롤러코스터(혈당 스파이크)를 겪고 있다는 결정적인 증거입니다. 검진 결과표를 보실 때는 반드시 두 숫자를 교차해서 읽으셔야 합니다.</p>

<div style="background:#f0f9ff; border:1.5px solid #bae6fd; border-radius:12px; padding:20px; margin:28px 0;">
  <strong style="color:#0369a1; font-size:1.05rem; display:block; margin-bottom:6px;">[수치 판독 가이드] 건강검진 혈압·혈당·간수치 종합 판독표</strong>
  <p style="font-size:0.92rem; color:#475569; margin:0 0 14px; line-height:1.5;">공복혈당뿐만 아니라 수축기 혈압, 간수치(AST·ALT), 총콜레스테롤 등 나의 종합 검진 결과가 정상 기준에 들어가는지 한 번에 점검해 보세요.</p>
  <a href="/checkup" style="display:inline-block; background:#0284c7; color:#fff; padding:10px 20px; border-radius:8px; font-weight:700; text-decoration:none; font-size:0.9rem;">건강검진 수치 정상 범위 &amp; 판독 가이드 바로가기 →</a>
</div>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>아침 공복 혈당이 왜 유독 높게 나올까? (인슐린 저항성과 간)</h2>
<p>밤새 아무것도 안 먹고 잤는데 아침 공복 혈당이 110을 훌쩍 넘는 현상에 많은 분들이 의아해하십니다. "먹은 게 없는데 어디서 당이 솟아난 걸까?" 답은 <strong>'간(Liver)'의 당 생성 과잉</strong>과 <strong>'인슐린 저항성'</strong>에 있습니다.</p>

<ol>
  <li><strong>간의 야간 당신생합성 (Gluconeogenesis):</strong> 간은 원래 수면 중에 뇌가 굶어 죽지 않도록 저장해 둔 글리코겐을 분해해 혈액 속으로 일정한 포도당을 공급합니다. 정상적인 몸이라면 췌장의 인슐린이 "이제 그만 내보내라"고 신호를 보내 멈추게 합니다.</li>
  <li><strong>인슐린 신호 차단:</strong> 그러나 간세포에 기름(지방간)이 끼고 인슐린 저항성이 생기면, 인슐린이 아무리 문을 두드려도 간이 신호를 무시하고 밤새 포도당을 뿜어냅니다. 그 결과 아침 기상 직후 공복 혈당이 치솟게 됩니다.</li>
  <li><strong>새벽 현상 (Dawn Phenomenon):</strong> 기상 2~3시간 전부터 몸을 깨우기 위해 코르티솔, 성장호르몬, 글루카곤 같은 각성 호르몬이 분비되는데, 이 호르몬들이 혈당을 끌어올립니다. 인슐린 감수성이 떨어진 사람일수록 이 새벽 혈당 상승 폭이 제어되지 않습니다.</li>
</ol>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>약 먹기 전 공복 혈당을 낮추는 4대 생활 교정법</h2>
<p>공복 혈당 100~125 mg/dL 구간은 아직 췌장의 베타세포가 완전히 파괴되지 않고 지쳐있는 상태입니다. 지금 당장 생활 습관을 바로잡으면 당뇨 진행을 60% 가까이 차단하고 정상 수치로 되돌릴 수 있습니다.</p>

<h3>1. 저녁 식사 후 야식 금지 (최소 12시간 공복 유지)</h3>
<p>밤 10시에 라면이나 과자를 먹고 잠들면 간은 밤새 야식을 분해하고 지방을 합성하느라 휴식 시간을 갖지 못합니다. 저녁 7시에 식사를 마쳤다면 다음 날 아침 7시까지 최소 12시간 동안은 물 외에 일체 간식을 끊어야 합니다. 공복 상태를 유지해야 간 내 지방이 연소되면서 간의 인슐린 감수성이 회복됩니다.</p>

<h3>2. 허벅지 대근육 단련 (인체 최대의 포도당 싱크대)</h3>
<p>우리 몸에서 음식으로 흡수된 포도당을 가장 많이 저장하고 소비하는 장기는 <strong>허벅지와 엉덩이 같은 하체 골격근(전체의 70% 이상)</strong>입니다. 근육량이 부족하면 포도당이 갈 곳을 잃고 혈관에 쌓입니다. 스쿼트, 런지, 계단 오르기 등 하체 근력 운동을 주 3회 병행하면 인슐린의 도움 없이도 근육의 포도당 수송체(GLUT4)가 활성화되어 공복 혈당이 빠르게 안정됩니다.</p>

<h3>3. 식사 순서 변경: 채소 먼저 먹는 거꾸로 식사법</h3>
<p>탄수화물(밥, 빵, 면)을 먼저 입에 넣으면 혈당이 수직 상승하며 인슐린이 폭발적으로 분비됩니다. 식사할 때 <strong>식이섬유(채소·해조류) → 단백질(고기·생선·두부) → 탄수화물(밥)</strong> 순서로 먹는 것만으로도 식후 혈당 피크를 30% 이상 억제할 수 있습니다. 자세한 식사 순서와 원리는 <a href="/health/blood-sugar-spike-prevention-diet/">혈당 스파이크 예방 식단 칼럼</a>을 참고해 보세요.</p>

<h3>4. 현재 체중의 5~7% 감량 (내장지방 제거)</h3>
<p>미국 국립보건원(NIH)의 유명한 대규모 임상 연구인 DPP(Diabetes Prevention Program)에 따르면, <strong>당뇨 전단계 성인이 체중의 5~7%만 감량해도 당뇨병 발생 위험이 58% 감소</strong>하는 것으로 증명되었습니다. 체중이 75kg인 사람이라면 3.5~5kg만 줄여도 복부 내장지방이 걷히며 인슐린 저항성이 획기적으로 개선됩니다. 나의 감량 칼로리 설계는 <a href="/calorie">하루 칼로리(TDEE) 계산기</a>를 활용해 보세요.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>에디터의 3줄 요약과 오늘부터 실천할 1가지</h2>
<ul>
  <li><strong>핵심 1:</strong> 공복 혈당 100~125 mg/dL은 안전지대가 아니라 췌장이 지쳐가는 '당뇨 전단계' 경고음입니다.</li>
  <li><strong>핵심 2:</strong> 건강검진 결과표에서 당화혈색소(HbA1c)가 5.7% 이상인지 반드시 함께 확인해야 합니다.</li>
  <li><strong>핵심 3:</strong> 저녁 8시 이후 야식을 완벽히 차단하고, 매일 20회 스쿼트로 허벅지 근육을 깨우세요.</li>
</ul>

<p>지금 당장 할 수 있는 가장 손쉬운 실천은 오늘 저녁 식사 후 부엌 찬장 문을 닫고, 아침 기상 전까지 12시간 동안 야식을 끊는 일입니다. 간이 쉴 수 있는 시간만 줘도 아침 혈당계 숫자는 달라지기 시작합니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>참고자료 및 공인 출처</h2>
<ul>
  <li>대한당뇨병학회 (KDA) – 2023 당뇨병 진료지침 제8판 (공복혈당장애 및 진단 기준)</li>
  <li>질병관리청 국가건강정보포털 – 당뇨병 전단계와 대사증후군 관리 수칙</li>
  <li>보건복지부 질병예방관리본부 – 한국인 만성질환 역학 및 심뇌혈관 질환 예방 가이드</li>
  <li>New England Journal of Medicine (NEJM) – Reduction in the Incidence of Type 2 Diabetes with Lifestyle Intervention (DPP Study)</li>
</ul>

<blockquote>
  <p><strong>[법적 및 의학적 고지]</strong><br>
  본 콘텐츠는 질병관리청 및 대한당뇨병학회의 학술 가이드라인을 토대로 작성된 건강 증진 정보이며, 의사의 전문적인 의학적 진단이나 처방을 대신할 수 없습니다. 공복 혈당이 126 mg/dL 이상이거나 당화혈색소가 6.5% 이상으로 확인된 경우, 지체 없이 내과 또는 내분비내과 전문의의 정밀 진료를 받으시기 바랍니다.</p>
</blockquote>

<div class="crp_related crp-text-only">
  <h3>함께 읽으면 좋은 건강 정보</h3>
  <ul>
    <li><a href="/health/blood-sugar-spike-prevention-diet/" class="crp_link"><span class="crp_title">식후 혈당 스파이크 증상과 낮추는 법, 거꾸로 식사법과 15분 걷기 효과</span></a></li>
    <li><a href="/health/liver-enzymes-ast-alt-guide/" class="crp_link"><span class="crp_title">간수치 AST ALT 정상 수치와 해석, 높은 이유와 낮추는 법</span></a></li>
    <li><a href="/health/blood-pressure-stages-hypertension-diet/" class="crp_link"><span class="crp_title">고혈압 전단계 수치 기준과 낮추는 법, DASH 식단과 칼륨·나트륨 관리 가이드</span></a></li>
  </ul>
  <div class="crp_clear"></div>
</div>
"""

# Assemble HTML
content = template

# Replace title
content = re.sub(r'<title>.*?</title>', f'<title>{title} | 건강노트</title>', content)
content = re.sub(r'<meta name="description" content=".*?"\s*/>', f'<meta name="description" content="{meta_desc}"/>', content)
content = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="https://healthfit100.com/health/{slug}/" />', content)

# Replace OG & Twitter
content = re.sub(r'<meta property="og:image" content=".*?" />', f'<meta property="og:image" content="https://healthfit100.com/health/{slug}/thumbnail.png" />', content)
content = re.sub(r'<meta name="twitter:image" content=".*?" />', f'<meta name="twitter:image" content="https://healthfit100.com/health/{slug}/thumbnail.png" />', content)
content = re.sub(r'<meta property="og:title" content=".*?" />', f'<meta property="og:title" content="{title}" />', content)
content = re.sub(r'<meta property="og:description" content=".*?" />', f'<meta property="og:description" content="{meta_desc}" />', content)
content = re.sub(r'<meta property="og:url" content=".*?" />', f'<meta property="og:url" content="https://healthfit100.com/health/{slug}/" />', content)
content = re.sub(r'<meta name="twitter:title" content=".*?" />', f'<meta name="twitter:title" content="{title}" />', content)
content = re.sub(r'<meta name="twitter:description" content=".*?" />', f'<meta name="twitter:description" content="{meta_desc}" />', content)

# Dates
content = re.sub(r'<meta property="og:updated_time" content=".*?" />', f'<meta property="og:updated_time" content="{published_iso}" />', content)
content = re.sub(r'<meta property="article:published_time" content=".*?" />', f'<meta property="article:published_time" content="{published_iso}" />', content)
content = re.sub(r'<meta property="article:modified_time" content=".*?" />', f'<meta property="article:modified_time" content="{modified_iso}" />', content)

# Article single header
content = re.sub(r'<h1 class="entry-title" itemprop="headline">.*?</h1>', f'<h1 class="entry-title" itemprop="headline">{title}</h1>', content)
content = re.sub(r'<span class="published" itemprop="datePublished">\s*.*?\s*</span>', f'<span class="published" itemprop="datePublished"> {display_date} </span>', content)

# Figure img
content = re.sub(r'<figure class="post-thumb-img-content".*?</figure>', f'''<figure class="post-thumb-img-content" style="margin:0 0 1.5em 0;border-radius:12px;overflow:hidden;text-align:center;box-shadow:0 4px 16px rgba(0,0,0,0.08);">
<img src="/health/{slug}/thumbnail.png" alt="{title}" width="1080" height="1350" loading="lazy" style="width:100%;max-width:540px;height:auto;margin:0 auto;display:block;border-radius:12px;">
</figure>''', content, flags=re.DOTALL)

# Replace entry-content
content = re.sub(r'<div class="entry-content clear"\s+itemprop="text"\s*>.*?</div><!-- \.entry-content \.clear -->', f'<div class="entry-content clear" itemprop="text">\n{body_html}\n</div><!-- .entry-content .clear -->', content, flags=re.DOTALL)

out_dir = REPO_DIR / "health" / slug
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "index.html"
out_file.write_text(content, encoding="utf-8")
print(f"Created article: {out_file}")

# Character count check
clean_text = re.sub(r'<[^>]+>', '', body_html)
clean_text_no_space = re.sub(r'\s+', '', clean_text)
print(f"Article character count (no spaces): {len(clean_text_no_space)} chars")

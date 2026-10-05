import os
import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# We can read the template from cholesterol-test-results-guide/index.html
template_path = REPO_DIR / "health" / "cholesterol-test-results-guide" / "index.html"
template = template_path.read_text(encoding="utf-8-sig")

articles = [
    {
        "slug": "vitamin-d-benefits-daily-intake-timing",
        "title": "비타민D 복용시간과 하루 권장량, 마그네슘과 함께 먹어야 하는 이유",
        "short_title": "비타민D 복용시간과 하루 권장량｜마그네슘 시너지",
        "meta_desc": "한국인 80%가 겪는 비타민D 결핍 기준(30 ng/mL), 지용성 흡수율을 높이는 점심 식후 복용법, 성인 1000~2000 IU 하루 권장량과 마그네슘 결합 이유를 정리했습니다.",
        "published_iso": "2026-10-03T09:00:00+09:00",
        "modified_iso": "2026-10-03T09:00:00+09:00",
        "display_date": "10월 3, 2026",
        "tags": ["비타민D", "비타민D 복용시간", "비타민D 하루 권장량", "마그네슘", "골다공증"],
        "img_url": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=800&h=450&fit=crop&q=80",
        "img_alt": "비타민D 영양제 복용시간과 하루 권장 섭취량",
        "body_html": """
<p>건강검진에서 혈액검사를 받고 “비타민D 수치가 너무 낮으니 꼭 챙겨 드세요”라는 말을 듣는 분들이 매우 많습니다. 실제로 질병관리청 통계에 따르면 대한민국 성인의 약 75~80%가 비타민D 결핍 또는 부족 상태에 놓여 있습니다.</p>
<p><strong>비타민D는 뼈 건강뿐 아니라 면역 체계와 만성 피로 관리의 핵심입니다. 하지만 지용성 비타민이기 때문에 공복에 물과 함께 삼키면 흡수율이 크게 떨어지며, 체내 활성화를 위해 마그네슘과의 균형을 맞추는 것이 중요합니다.</strong></p>

<h2>비타민D 혈중 농도 기준, 내 수치는 어디에 해당할까</h2>
<p>병원에서 혈액검사를 통해 확인하는 항목은 <strong>25(OH)D (25-하이드록시 비타민D)</strong> 농도입니다. 단위는 보통 ng/mL로 표기됩니다.</p>
<table>
<thead>
<tr>
<th>혈중 농도 (ng/mL)</th>
<th>분류</th>
<th>상태 설명 및 권고 사항</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>10 미만</strong></td>
<td>중증 결핍</td>
<td>구루병, 골연화증, 심한 면역 저하 위험. 고용량(주사 또는 4,000~5,000 IU) 처방 필요</td>
</tr>
<tr>
<td><strong>10 ~ 19</strong></td>
<td>결핍</td>
<td>한국인 대다수가 속하는 구간. 피로감, 근육통, 골다공증 위험 증가</td>
</tr>
<tr>
<td><strong>20 ~ 29</strong></td>
<td>부족</td>
<td>일반적인 권장치에 미치지 못함. 매일 1,000~2,000 IU 보충 권장</td>
</tr>
<tr>
<td><strong>30 ~ 100</strong></td>
<td><strong>적정 (정상)</strong></td>
<td>뼈 건강과 면역 기능이 가장 안정적으로 유지되는 이상적인 혈중 수치</td>
</tr>
<tr>
<td><strong>100 초과</strong></td>
<td>과다 / 중독 위험</td>
<td>고칼슘혈증, 신장결석, 메스꺼움 유발 가능. 복용 중단 후 재검 필요</td>
</tr>
</tbody>
</table>
<p>많은 전문가들이 권장하는 건강한 성인의 혈중 비타민D 목표치는 <strong>30~50 ng/mL</strong> 사이입니다. 자가 면역 질환이나 심한 피로를 겪는 분들은 40 ng/mL 이상 유지를 목표로 하기도 합니다.</p>

<h2>비타민D 복용시간, 아침 공복보다 ‘점심 식후’가 좋은 이유</h2>
<p>비타민제를 아침에 일어나자마자 물 한 컵과 함께 드시는 분들이 많습니다. 하지만 비타민D는 물에 녹는 수용성(비타민B, C)이 아니라 <strong>기름에 녹는 지용성(비타민A, D, E, K)</strong> 영양소입니다.</p>
<ul>
<li><strong>식사 중 지방과 함께 흡수:</strong> 비타민D는 소장에서 담즙산과 지방 성분과 섞여 미셀(micelle)을 형성해야 흡수됩니다. 지방이 없는 빈속에 먹으면 유효 성분의 상당량이 흡수되지 못하고 배출됩니다.</li>
<li><strong>점심 또는 기름진 식사 직후:</strong> 하루 중 가장 지방 섭취가 풍부한 식사(주로 점심 또는 저녁) 직후에 복용하는 것이 가장 흡수율이 높습니다. 임상 연구에 따르면 식사와 함께 복용했을 때 공복 대비 혈중 농도가 최대 30~50% 더 높게 상승했습니다.</li>
<li><strong>불면증 예방:</strong> 비타민D는 수면 유도 호르몬인 멜라토닌 분비와 상호작용합니다. 일부 민감한 분들은 늦은 밤에 복용할 경우 수면에 방해를 받을 수 있으므로, 아침 식후나 점심 식후 복용을 권장합니다.</li>
</ul>

<h2>하루 권장량: 1,000 IU vs 2,000 IU vs 5,000 IU</h2>
<p>보건복지부의 ‘한국인 영양소 섭취기준’에 따르면 성인의 비타민D 일일 충분섭취량은 400~800 IU(10~20㎍)로 설정되어 있습니다. 하지만 이 기준은 ‘골다공증이나 결핍증을 예방하기 위한 최소한의 선’에 가깝습니다.</p>
<ul>
<li><strong>혈중 농도 유지를 원하는 일반 성인:</strong> 매일 <strong>1,000 ~ 2,000 IU</strong> 복용이 가장 무난하고 안전합니다.</li>
<li><strong>검사상 20 ng/mL 미만 결핍 환자:</strong> 2~3개월간 매일 <strong>4,000 ~ 5,000 IU</strong>를 복용하여 혈중 수치를 30 ng/mL 이상으로 끌어올린 후, 유지 용량(1,000~2,000 IU)으로 줄이는 요법이 널리 쓰입니다.</li>
<li><strong>일일 상한섭취량:</strong> 한국 보건복지부 기준 성인 비타민D 상한섭취량은 <strong>4,000 IU</strong>입니다. 매일 5,000 IU 이상을 장기 복용할 때는 반드시 3~6개월마다 혈액검사를 받아야 합니다.</li>
</ul>

<h2>왜 마그네슘, 비타민K2와 함께 먹으라고 할까?</h2>
<p>비타민D 단일제만 먹었을 때 효과를 체감하지 못하거나 오히려 두통, 눈 떨림이 생기는 경우가 있습니다. 이는 비타민D의 대사 과정에 필수적인 <strong>보조 미네랄</strong>이 부족하기 때문입니다.</p>
<ol>
<li><strong>마그네슘과의 시너지:</strong> 우리가 섭취한 비타민D는 간과 신장을 거쳐 활성형 비타민D로 전환되어야 작용합니다. 이 전환 효소를 활성화하는 필수 물질이 바로 ‘마그네슘’입니다. 마그네슘이 부족하면 비타민D를 아무리 먹어도 몸에서 제대로 쓰이지 못합니다.</li>
<li><strong>비타민K2와의 칼슘 배분:</strong> 비타민D는 장에서 칼슘 흡수를 촉진합니다. 그런데 이 흡수된 칼슘이 뼈로 가지 못하고 혈관 벽에 달라붙으면 혈관 석회화나 신장 결석을 유발할 수 있습니다. 비타민K2는 혈액 속 칼슘을 뼈 속으로 운반해 넣는 ‘오스테오칼신’ 단백질을 활성화하여 동맥경화를 예방합니다.</li>
</ol>

<h2>비타민D 복용 시 주의할 점</h2>
<p>지용성 비타민은 몸 밖으로 소변을 통해 쉽게 배출되지 않고 간과 지방조직에 축적됩니다. 따라서 무분별한 초고용량 복용은 피해야 합니다. 고칼슘혈증이 생기면 구토, 갈증, 잦은 소변, 신장 결석 등의 증상이 나타날 수 있습니다.</p>
<p>또한 기존에 칼슘제나 종합비타민을 이미 드시고 있다면 영양성분표를 확인하여 하루 섭취 총합이 상한량을 넘지 않는지 확인하세요. 연령별 자세한 상한 기준은 <a href="/supplement">영양제 권장량 및 상한섭취량 조회기</a>에서 직접 확인하실 수 있습니다.</p>

<h2>참고자료</h2>
<ul>
<li>질병관리청 국가건강정보포털 – 비타민D 결핍증과 골다공증 가이드</li>
<li>보건복지부·한국영양학회 – 2020 한국인 영양소 섭취기준 (비타민D 및 미네랄)</li>
<li>The Journal of Clinical Endocrinology & Metabolism – Evaluation, Treatment, and Prevention of Vitamin D Deficiency</li>
</ul>
<blockquote><p>본 콘텐츠는 공신력 있는 보건 당국 및 학술 연구 자료를 바탕으로 작성된 건강 정보이며, 의사의 개별 진료나 처방을 대신할 수 없습니다. 수치 이상이나 기저질환이 있는 경우 주치의와 상담하십시오.</p></blockquote>
<div class="crp_related crp-text-only"><h3>함께 읽으면 좋은 정보</h3><ul><li><a href="/health/마그네슘-하루-권장량/" class="crp_link"><span class="crp_title">마그네슘 하루 권장량과 복용시간: 눈 밑 떨림과 수면 개선 팁</span></a></li><li><a href="/health/칼슘-하루-권장-섭취량/" class="crp_link"><span class="crp_title">칼슘 하루 권장 섭취량과 영양제 흡수율 높이는 법</span></a></li><li><a href="/health/멀티비타민-언제-먹어야-효과-좋을까/" class="crp_link"><span class="crp_title">멀티비타민 언제 먹어야 효과 좋을까? 식전 vs 식후 복용법</span></a></li></ul><div class="crp_clear"></div></div>
"""
    },
    {
        "slug": "blood-sugar-spike-prevention-diet",
        "title": "식후 혈당 스파이크 증상과 낮추는 법, 거꾸로 식사법과 15분 걷기 효과",
        "short_title": "식후 혈당 스파이크 증상과 낮추는 법｜거꾸로 식사법·15분 걷기",
        "meta_desc": "밥 먹고 쏟아지는 극심한 졸음의 원인 혈당 스파이크 기준(140 mg/dL), 식이섬유부터 먹는 거꾸로 식사법과 식후 15분 걷기가 인슐린에 미치는 과학적 효과를 정리했습니다.",
        "published_iso": "2026-10-04T09:00:00+09:00",
        "modified_iso": "2026-10-04T09:00:00+09:00",
        "display_date": "10월 4, 2026",
        "tags": ["혈당 스파이크", "식후 혈당 낮추는 법", "거꾸로 식사법", "당뇨 전단계", "공복혈당"],
        "img_url": "https://images.unsplash.com/photo-1505576399279-565b52d4ac71?w=800&h=450&fit=crop&q=80",
        "img_alt": "혈당 스파이크 예방을 위한 식이섬유와 건강한 식단 관리",
        "body_html": """
<p>점심을 배부르게 먹고 난 뒤 1시간쯤 지나면 머리가 멍해지거나 눈꺼풀을 들어올리기 힘들 만큼 쏟아지는 졸음을 겪어보신 적 있으신가요? 많은 분들이 단순한 춘곤증이나 피로 탓으로 돌리지만, 이는 혈액 속 포도당 농도가 요동치는 <strong>‘혈당 스파이크(Blood Sugar Spike)’</strong>의 대표적인 신호일 수 있습니다.</p>
<p><strong>건강검진에서 공복혈당 수치가 90대로 정상이어도 식후 혈당 스파이크는 얼마든지 발생할 수 있습니다. 췌장을 지치게 만들고 내장지방과 동맥경화를 부르는 혈당 스파이크의 메커니즘과, 일상에서 바로 실천할 수 있는 두 가지 핵심 예방법을 정리했습니다.</strong></p>

<h2>혈당 스파이크란 무엇이며 왜 위험할까?</h2>
<p>혈당 스파이크는 음식을 섭취한 뒤 1~2시간 사이에 혈당이 <strong>140 mg/dL 이상</strong>으로 급격하게 치솟았다가, 이를 처리하기 위해 췌장에서 인슐린이 과다 분비되면서 다시 곤두박질치는 현상을 말합니다.</p>
<ul>
<li><strong>급격한 저혈당 반응과 가짜 배고픔:</strong> 혈당이 급격히 떨어지면 뇌는 에너지가 고갈되었다고 착각하여 식사한 지 2시간도 채 안 되어 빵, 과자, 초콜릿 같은 단순당을 강하게 갈망하게 만듭니다.</li>
<li><strong>혈관 내피세포 손상과 활성산소:</strong> 롤러코스터처럼 요동치는 고혈당 상태는 혈관 내벽을 공격하여 활성산소를 뿜어내고, 미세 염증을 일으켜 혈관을 딱딱하게(동맥경화) 만듭니다.</li>
<li><strong>췌장 베타세포의 번아웃:</strong> 매 끼니마다 과도한 인슐린을 쥐어짜다 보면 결국 인슐린 저항성이 생기고, 췌장 기능이 고갈되어 실제 제2형 당뇨병으로 진행됩니다.</li>
</ul>

<h2>혈당 검사표 수치 기준</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>정상 범위</th>
<th>당뇨 전단계 (내당능 장애)</th>
<th>당뇨병 진단</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>공복 혈당 (mg/dL)</strong></td>
<td>100 미만</td>
<td>100 ~ 125</td>
<td>126 이상</td>
</tr>
<tr>
<td><strong>식후 2시간 혈당 (mg/dL)</strong></td>
<td><strong>140 미만</strong></td>
<td>140 ~ 199</td>
<td>200 이상</td>
</tr>
<tr>
<td><strong>당화혈색소 (HbA1c, %)</strong></td>
<td>5.7 미만</td>
<td>5.7 ~ 6.4</td>
<td>6.5 이상</td>
</tr>
</tbody>
</table>
<p>공복 혈당만 재는 일반 건강검진에서는 식후 혈당 스파이크를 놓치기 쉽습니다. 만약 식후 심한 졸음, 어지러움, 집중력 저하가 잦다면 연속혈당측정기(CGM)를 활용하거나 가정용 혈당계로 식후 1시간·2시간 혈당을 측정해 보는 것이 좋습니다.</p>

<h2>가장 확실한 식사 전략: ‘거꾸로 식사법 (채·단·탄)’</h2>
<p>먹는 음식의 총 칼로리가 같더라도 <strong>‘먹는 순서’</strong>만 바꾸면 식후 혈당 상승 폭을 30~40% 이상 완만하게 낮출 수 있습니다. 이를 영양학에서는 거꾸로 식사법이라고 부릅니다.</p>
<ol>
<li><strong>1단계: 채소·해조류 (식이섬유):</strong> 샐러드, 나물, 미역국, 양배추 등을 가장 먼저 꼭꼭 씹어 먹습니다. 수용성 식이섬유가 위벽에 그물망 같은 젤을 형성하여 이후 들어올 영양소의 소화 흡수를 물리적으로 지연시킵니다.</li>
<li><strong>2단계: 단백질·지방 (고기, 생선, 두부, 달걀):</strong> 단백질과 지방은 위장 배출 시간을 늦추는 호르몬(GLP-1) 분비를 촉진합니다. 포만감이 일찍 찾아와 탄수화물 과식을 막아줍니다.</li>
<li><strong>3단계: 탄수화물 (밥, 빵, 면):</strong> 마지막에 밥이나 빵을 먹습니다. 이미 식이섬유와 단백질이 장벽을 감싸고 있어 포도당이 혈액으로 급격히 흡수되지 않고 천천히 분해됩니다.</li>
</ol>

<h2>식후 15분의 마법: 식후 가벼운 걷기</h2>
<p>식사를 마친 뒤 소화를 시킨다며 소파나 침대에 바로 눕는 습관은 혈당을 최고조로 끌어올리는 지름길입니다.</p>
<ul>
<li><strong>골격근의 포도당 다이렉트 소비:</strong> 인체에서 포도당을 가장 많이 소비하는 곳은 허벅지와 엉덩이 같은 하체 대근육입니다. 식후 15~30분 이내에 가볍게 걷기 시작하면, 인슐린 도움 없이도 근육의 포도당 수송체(GLUT4)가 세포 표면으로 이동해 혈중 포도당을 직접 빨아들입니다.</li>
<li><strong>15분 걷기의 힘:</strong> 굳이 숨이 차는 격렬한 운동을 할 필요가 없습니다. 식후 15분 동안 동네를 산책하거나, 실내에서 제자리걸음, 뒤꿈치 들기(가자미근 운동), 가벼운 스쿼트를 20회 정도 해주는 것만으로도 혈당 피크 수치를 20~30 mg/dL 이상 뚝 떨어뜨릴 수 있습니다.</li>
</ul>

<h2>이런 음식은 혈당 스파이크의 주범입니다</h2>
<p>식이섬유가 제거된 <strong>정제 탄수화물과 액상과당</strong>은 혈관에 설탕물을 붓는 것과 같습니다. 식후 믹스커피, 바닐라라떼, 생과일주스, 탄산음료, 떡, 흰 식빵은 최소화해야 합니다. 하루에 필요한 적정 탄수화물 및 영양소 비율은 <a href="/calorie">하루 칼로리(TDEE) 계산기</a> 및 <a href="/protein">단백질 섭취량 계산기</a>에서 확인해 보세요.</p>

<h2>참고자료</h2>
<ul>
<li>대한당뇨병학회 – 당뇨병 진료지침 제8판</li>
<li>질병관리청 국가건강정보포털 – 당뇨병 전단계와 식후 혈당 관리</li>
<li>Diabetes Care – Food Order Impacts Postprandial Glucose and Insulin Levels in Prediabetes</li>
</ul>
<blockquote><p>본 콘텐츠는 일반적인 건강 증진을 목적으로 작성되었으며 의료적 진단이나 처방이 아닙니다. 당뇨 약물을 복용 중이신 환자는 식단 및 운동 변화 시 저혈당에 유의하고 담당 의사와 상의하세요.</p></blockquote>
<div class="crp_related crp-text-only"><h3>함께 읽으면 좋은 정보</h3><ul><li><a href="/health/fatty-liver-foods-diet/" class="crp_link"><span class="crp_title">지방간에 좋은 음식과 피해야 할 음식, 식단에서 먼저 바꿀 것</span></a></li><li><a href="/health/ldl-cholesterol-diet-saturated-fat/" class="crp_link"><span class="crp_title">LDL 콜레스테롤 낮추는 식단, 달걀보다 먼저 바꿀 지방</span></a></li><li><a href="/health/하루-물-섭취량/" class="crp_link"><span class="crp_title">하루 물 섭취량 계산법: 혈액 순환과 노폐물 배출 가이드</span></a></li></ul><div class="crp_clear"></div></div>
"""
    },
    {
        "slug": "blood-pressure-stages-hypertension-diet",
        "title": "고혈압 전단계 수치 기준과 낮추는 법, DASH 식단과 칼륨으로 나트륨 배출하기",
        "short_title": "고혈압 전단계 수치 기준과 낮추는 법｜DASH 식단·칼륨 음식",
        "meta_desc": "수축기 120~139 mmHg 고혈압 전단계 수치 기준과 약 복용 전 3개월 혈압 낮추는 생활요법, DASH 식단 및 칼륨이 풍부한 나트륨 배출 음식을 체계적으로 안내합니다.",
        "published_iso": "2026-10-05T09:00:00+09:00",
        "modified_iso": "2026-10-05T09:00:00+09:00",
        "display_date": "10월 5, 2026",
        "tags": ["고혈압 전단계", "혈압 정상수치", "고혈압 낮추는 방법", "DASH 식단", "나트륨 배출"],
        "img_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=450&fit=crop&q=80",
        "img_alt": "고혈압 전단계 수치 측정과 DASH 식단 및 생활습관 개선",
        "body_html": """
<p>건강검진표를 받아들었을 때 혈압 수치에 130/85 mmHg가 찍혀 있고 ‘고혈압 전단계(주의 혈압)’라는 붉은색 글씨를 보면 덜컥 겁이 납니다. 아직 약을 먹을 단계는 아니라고 하지만, 그렇다고 안심하고 방치해도 되는 상태는 결코 아닙니다.</p>
<p><strong>고혈압 전단계는 혈관에 탄력이 떨어지기 시작했다는 몸의 경고등입니다. 대한고혈압학회 지침에 따르면 이 단계에서 적극적으로 식단과 체중 관리를 시작하면 평생 혈압약을 먹지 않고도 정상 혈압으로 되돌릴 수 있는 ‘마지막 골든타임’입니다.</strong></p>

<h2>2026년 기준 혈압 분류표: 내 수치는 어디일까?</h2>
<p>혈압은 심장이 수축할 때 혈관에 가해지는 압력인 <strong>수축기 혈압(최고 혈압)</strong>과, 심장이 이완할 때의 <strong>이완기 혈압(최저 혈압)</strong>으로 나뉩니다. 단위는 mmHg입니다.</p>
<table>
<thead>
<tr>
<th>혈압 분류</th>
<th>수축기 혈압 (mmHg)</th>
<th></th>
<th>이완기 혈압 (mmHg)</th>
<th>대응 가이드</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>정상 혈압</strong></td>
<td><strong>120 미만</strong></td>
<td>그리고</td>
<td><strong>80 미만</strong></td>
<td>현재 건강한 생활습관 유지</td>
</tr>
<tr>
<td><strong>주의 혈압</strong></td>
<td>120 ~ 129</td>
<td>그리고</td>
<td>80 미만</td>
<td>염분 섭취 제한 및 유산소 운동 시작</td>
</tr>
<tr>
<td><strong>고혈압 전단계</strong></td>
<td><strong>130 ~ 139</strong></td>
<td>또는</td>
<td><strong>80 ~ 89</strong></td>
<td><strong>적극적인 비약물 요법(식단·체중감량) 필수</strong></td>
</tr>
<tr>
<td><strong>1기 고혈압</strong></td>
<td>140 ~ 159</td>
<td>또는</td>
<td>90 ~ 99</td>
<td>생활습관 개선 및 심혈관 위험도 평가 후 약물 치료 고려</td>
</tr>
<tr>
<td><strong>2기 고혈압</strong></td>
<td>160 이상</td>
<td>또는</td>
<td>100 이상</td>
<td>즉각적인 혈압 강하제 복용 및 정밀 검사</td>
</tr>
</tbody>
</table>
<p>수축기와 이완기 중 <strong>하나라도 더 높은 구간에 해당하면</strong> 그 단계로 판정합니다. 예를 들어 수축기가 125여도 이완기가 85라면 ‘고혈압 전단계’에 해당합니다.</p>

<h2>나트륨을 몰아내는 열쇠: ‘칼륨’과 나트륨-칼륨 펌프</h2>
<p>한국인은 찌개, 탕, 김치, 라면 등 국물 위주의 식문화로 인해 하루 평균 나트륨 섭취량이 세계보건기구(WHO) 권장량(2,000mg)의 약 1.5~2배에 달합니다.</p>
<ul>
<li><strong>나트륨이 혈압을 올리는 원리:</strong> 혈액 속에 나트륨 농도가 높아지면 삼투압 현상으로 인해 세포 안의 수분을 혈관 속으로 끌어당깁니다. 혈액량이 불어나면서 혈관벽을 강하게 밀어내어 혈압이 상승합니다.</li>
<li><strong>칼륨의 나트륨 배출 효과:</strong> 세포 안팎의 미네랄 균형을 맞추는 ‘나트륨-칼륨 펌프’ 원리에 의해, 체내에 칼륨이 충분히 들어오면 신장에서 나트륨을 소변으로 밀어내어 체외로 배출시킵니다. 이를 통해 혈액량이 줄어들고 혈관의 긴장이 완화됩니다.</li>
</ul>

<h3>칼륨이 풍부한 대표 식재료</h3>
<ul>
<li><strong>시금치·근대·아욱:</strong> 짙은 녹색 잎채소는 칼륨과 마그네슘이 모두 풍부하여 혈관 확장을 돕습니다.</li>
<li><strong>바나나·토마토·아보카도:</strong> 대표적인 고칼륨 과채류로 아침 식사나 간식으로 나트륨 배출을 돕기에 적합합니다.</li>
<li><strong>감자·고구마:</strong> 밥 대신 섭취할 수 있는 복합 탄수화물이자 풍부한 칼륨 공급원입니다.</li>
<li><em>※ 주의: 만성 콩팥병(신부전) 환자는 신장의 칼륨 배출 기능이 떨어져 고칼륨혈증(부정맥 위험)이 발생할 수 있으므로 임의로 고칼륨 식단을 하시면 안 됩니다.</em></li>
</ul>

<h2>혈압을 11 mmHg 낮추는 ‘DASH 식단’의 핵심</h2>
<p>미국 국립보건원(NIH)에서 고혈압 치료를 위해 개발한 <strong>DASH(Dietary Approaches to Stop Hypertension) 식단</strong>은 약물에 버금가는 혈압 강하 효과가 입증된 식사법입니다.</p>
<ol>
<li><strong>흰쌀밥 대신 통곡물:</strong> 현미, 귀리, 보리 등 통곡물로 밥을 지어 식이섬유 섭취를 늘립니다.</li>
<li><strong>국물은 건더기만:</strong> 찌개나 라면 국물에 녹아 있는 나트륨이 전체의 60% 이상입니다. 국물을 남기는 것만으로도 나트륨 섭취를 절반으로 줄일 수 있습니다.</li>
<li><strong>저지방 유제품과 견과류:</strong> 칼슘이 풍부한 저지방 우유·요거트와 마그네슘이 풍부한 아몬드·호두를 매일 한 줌씩 섭취합니다.</li>
<li><strong>가공육과 붉은 고기 줄이기:</strong> 베이컨, 햄, 소시지 등 가공육은 나트륨과 포화지방 함량이 매우 높아 혈관 탄력을 떨어뜨립니다.</li>
</ol>

<h2>혈압을 낮추는 생활 습관 3가지</h2>
<ol>
<li><strong>체중 1kg 감량 시 혈압 1 mmHg 감소:</strong> 과체중인 경우 체중 감량은 가장 강력한 혈압 강하제입니다. <a href="/bmi">BMI 계산기</a>로 자신의 비만도를 확인하고 표준 체중을 목표로 감량해 보세요.</li>
<li><strong>빠르게 걷기 하루 30분:</strong> 주 5회 이상 숨이 약간 찰 정도의 유산소 운동(빠르게 걷기, 자전거, 수영)은 혈관 내피세포 기능을 회복시켜 수축기 혈압을 5~8 mmHg 낮춥니다.</li>
<li><strong>올바른 가정 혈압 측정:</strong> 병원에만 가면 긴장해서 혈압이 오르는 ‘백의 고혈압’이 많습니다. 아침 기상 후 소변을 보고 1시간 이내, 식사 전, 등받이 의자에 편안히 5분간 앉은 뒤 심장 높이에서 측정한 혈압을 기록하세요.</li>
</ol>

<h2>참고자료</h2>
<ul>
<li>대한고혈압학회 – 2022 고혈압 진료지침 개정안</li>
<li>질병관리청 국가건강정보포털 – 고혈압 전단계와 비약물적 생활요법</li>
<li>National Institutes of Health (NIH) – DASH Eating Plan and Blood Pressure Reduction</li>
</ul>
<blockquote><p>본 정보는 일반적인 건강 증진을 위해 공신력 있는 의학 지침을 정리한 자료입니다. 개인의 심혈관 질환 위험인자(당뇨, 흡연, 고지혈증)에 따라 치료 기준이 달라지므로 반드시 의사와 상담하시기 바랍니다.</p></blockquote>
<div class="crp_related crp-text-only"><h3>함께 읽으면 좋은 정보</h3><ul><li><a href="/health/cholesterol-test-results-guide/" class="crp_link"><span class="crp_title">콜레스테롤 검사표 읽는 법, 총콜레스테롤보다 먼저 볼 숫자</span></a></li><li><a href="/health/ldl-cholesterol-diet-saturated-fat/" class="crp_link"><span class="crp_title">LDL 콜레스테롤 낮추는 식단, 달걀보다 먼저 바꿀 지방</span></a></li><li><a href="/health/하루-카페인-권장량/" class="crp_link"><span class="crp_title">하루 카페인 권장량과 혈압·심장에 미치는 영향</span></a></li></ul><div class="crp_clear"></div></div>
"""
    }
]

# Generate each article
for art in articles:
    art_dir = REPO_DIR / "health" / art["slug"]
    art_dir.mkdir(parents=True, exist_ok=True)
    art_file = art_dir / "index.html"
    
    # We will build HTML using cholesterol-test-results-guide as template
    content = template
    
    # 1. Update Title & Meta
    content = re.sub(r"<title>.*?</title>", f"<title>{art['title']} | 건강노트</title>", content)
    content = re.sub(r'<meta name="description" content=".*?"/>', f'<meta name="description" content="{art["meta_desc"]}"/>', content)
    content = re.sub(r'<meta property="og:title" content=".*?" />', f'<meta property="og:title" content="{art["title"]}" />', content)
    content = re.sub(r'<meta property="og:description" content=".*?" />', f'<meta property="og:description" content="{art["meta_desc"]}" />', content)
    content = re.sub(r'<meta property="og:url" content=".*?" />', f'<meta property="og:url" content="https://healthfit100.com/health/{art["slug"]}/" />', content)
    content = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="https://healthfit100.com/health/{art["slug"]}/" />', content)
    content = re.sub(r'<meta name="twitter:title" content=".*?" />', f'<meta name="twitter:title" content="{art["title"]}" />', content)
    content = re.sub(r'<meta name="twitter:description" content=".*?" />', f'<meta name="twitter:description" content="{art["meta_desc"]}" />', content)
    content = re.sub(r'<meta property="article:published_time" content=".*?" />', f'<meta property="article:published_time" content="{art["published_iso"]}" />', content)
    content = re.sub(r'<meta property="article:modified_time" content=".*?" />', f'<meta property="article:modified_time" content="{art["modified_iso"]}" />', content)
    content = re.sub(r'<meta property="og:updated_time" content=".*?" />', f'<meta property="og:updated_time" content="{art["modified_iso"]}" />', content)
    
    # 2. Schema JSON
    # Simple replacement of URLs, title, desc, dates
    content = re.sub(r'https://healthfit100.com/health/cholesterol-test-results-guide/', f'https://healthfit100.com/health/{art["slug"]}/', content)
    content = re.sub(r'2026-08-07T09:00:00\+09:00', art["published_iso"], content)
    content = re.sub(r'2026-08-08T17:32:54\+09:00', art["modified_iso"], content)
    
    # 3. Entry Title & Date in body
    content = re.sub(r'<h1 class="entry-title" itemprop="headline">.*?</h1>', f'<h1 class="entry-title" itemprop="headline">{art["title"]}</h1>', content)
    content = re.sub(r'<span class="published" itemprop="datePublished">.*?</span>', f'<span class="published" itemprop="datePublished"> {art["display_date"]} </span>', content)
    
    # 4. Insert image figure before <header class="entry-header "> if not present
    fig_html = f'''<figure class="post-thumb-img-content" style="margin:0 0 1.5em 0;border-radius:8px;overflow:hidden;text-align:center;">
<img src="{art['img_url']}" alt="{art['img_alt']}" width="800" height="450" loading="lazy" style="width:100%;height:auto;display:block;object-fit:cover;">
<figcaption style="font-size:12px;color:#888888;margin-top:6px;text-align:center;">사진 출처: Unsplash</figcaption>
</figure>'''
    
    # If there's an existing figure or we replace header
    if '<header class="entry-header ">' in content:
        content = content.replace('<header class="entry-header ">', f'{fig_html}\n<header class="entry-header ">', 1)
        
    # 5. Replace entry-content
    # Find start of entry-content and end
    start_tag = '<div class="entry-content clear"\n\titemprop="text"\t>'
    if start_tag not in content:
        start_tag = '<div class="entry-content clear" itemprop="text">'
    if start_tag not in content:
        # regex find
        m = re.search(r'<div class="entry-content clear"[^>]*>', content)
        if m:
            start_tag = m.group(0)

    end_tag = '</div><!-- .entry-content .clear -->'
    
    parts = content.split(start_tag)
    before_body = parts[0] + start_tag
    after_body = end_tag + parts[1].split(end_tag)[1]
    
    full_art_html = before_body + "\n" + art["body_html"] + "\n" + after_body
    
    art_file.write_text(full_art_html, encoding="utf-8")
    print(f"Created article: {art_file}")

print("All 3 articles created successfully!")

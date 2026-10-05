import os
import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Read template from cholesterol-test-results-guide
template_path = REPO_DIR / "health" / "cholesterol-test-results-guide" / "index.html"
template = template_path.read_text(encoding="utf-8-sig")

# 2. Define the 2 new articles
new_articles = [
    {
        "slug": "liver-enzymes-ast-alt-guide",
        "title": "간수치 AST ALT 정상 수치와 해석, 높은 이유와 낮추는 법",
        "short_title": "간수치 AST ALT 정상 수치와 해석｜높은 이유·낮추는 법",
        "meta_desc": "건강검진 간수치 AST(GOT)·ALT(GPT) 정상 범위(40 IU/L 이하)와 수치가 높아지는 주요 원인(비알코올성 지방간, 음주, 약물·즙), 식단과 생활습관으로 낮추는 법을 정리했습니다.",
        "published_iso": "2026-10-05T09:00:00+09:00",
        "modified_iso": "2026-10-05T09:00:00+09:00",
        "display_date": "10월 5, 2026",
        "tags": ["간수치", "AST", "ALT", "간수치 낮추는 법", "지방간", "간기능 검사"],
        "img_url": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=800&h=450&fit=crop&q=80",
        "img_alt": "간기능 검사 AST ALT 수치 해석과 간 건강 관리",
        "body_html": """
<p>건강검진 결과지에서 ‘AST(GOT)’와 ‘ALT(GPT)’라는 알파벳 옆에 빨간색 글씨로 ‘주의’ 또는 ‘질환의심’이 표시되면 덜컥 겁이 납니다. 술을 거의 마시지 않는 분들도 간수치가 높게 나와 당황하는 경우가 매우 흔합니다.</p>
<p><strong>간은 ‘침묵의 장기’로 불리며 신경세포가 없어 세포가 파괴되어도 통증을 느끼지 못합니다. AST와 ALT는 간세포가 손상될 때 혈액 속으로 흘러나오는 효소로, 간이 보내는 가장 첫 번째 SOS 신호입니다. 두 수치의 차이점과 정상 범위, 일상에서 수치를 정상으로 되돌리는 검증된 방법을 정리했습니다.</strong></p>

<h2>AST와 ALT, 무엇이 다른가요?</h2>
<p>많은 분들이 두 수치를 비슷하게 생각하지만, 체내 분포 위치와 임상적 의미에 분명한 차이가 있습니다.</p>
<ul>
<li><strong>AST (아스파르테이트 아미노전이효소, 구 GOT):</strong> 간세포뿐 아니라 심장, 콩팥, 골격근, 뇌 등 여러 장기에도 널리 분포합니다. 따라서 심한 근력 운동 후 근육통이 심하거나 심장 질환이 있을 때도 AST 수치가 단독으로 상승할 수 있습니다.</li>
<li><strong>ALT (알라닌 아미노전이효소, 구 GPT):</strong> 주로 <strong>‘간세포’</strong> 내부에 집중되어 존재합니다. 따라서 ALT가 상승했다는 것은 다른 장기보다 간세포가 직접적으로 손상되었음을 나타내는 훨씬 특이도 높은 지표입니다.</li>
</ul>

<h2>간수치 정상 범위와 수치별 분류 기준</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>일반 참고 기준 (IU/L)</th>
<th>대한간학회 권장 이상적 기준</th>
<th>임상적 의미</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>정상</strong></td>
<td><strong>0 ~ 40 이하</strong></td>
<td>남성 30~35 미만 / 여성 25 미만</td>
<td>간세포 손상이 없는 안정적인 상태</td>
</tr>
<tr>
<td><strong>경도 상승 (경계)</strong></td>
<td>41 ~ 100</td>
<td>-</td>
<td>비알코올성 지방간, 경미한 음주, 과로, 복용 약물(한약, 즙) 영향 의심</td>
</tr>
<tr>
<td><strong>중등도 상승</strong></td>
<td>101 ~ 300</td>
<td>-</td>
<td>만성 간염 활동기, 알코올성 간염, 지방간염 진행</td>
</tr>
<tr>
<td><strong>고도 상승 (위험)</strong></td>
<td>300 이상 (때로 1,000 이상)</td>
<td>-</td>
<td>급성 바이러스성 간염, 독성 간염(약물 중독), 허혈성 간 손상 즉각 진료 필요</td>
</tr>
</tbody>
</table>
<p>수치가 40을 살짝 넘은 45~60 수준이라면 당장 간경화나 간암을 걱정하기보다는 최근의 음주, 체중 증가, 복용한 건강기능식품 등을 먼저 점검하는 것이 합리적입니다.</p>

<h2>술을 안 마시는데 간수치가 왜 높을까? 4대 원인</h2>
<ol>
<li><strong>비알코올성 지방간질환 (NAFLD):</strong> 현대인 간수치 상승의 가장 흔한 원인입니다. 밥, 빵, 면, 떡 등 정제 탄수화물과 액상과당을 과다 섭취하면 간에 중성지방이 끼고, 이 지방이 염증을 일으켜 간세포를 파괴합니다.</li>
<li><strong>농축액과 건강즙 (독성 간염):</strong> 칡즙, 헛개즙, 양파즙, 마늘즙 등 농축된 형태의 건강즙이나 성분을 알 수 없는 한약재를 장기 복용하면, 이를 해독하는 간에 심한 과부하가 걸려 간수치가 급상승할 수 있습니다.</li>
<li><strong>진통소염제 및 복용 약물:</strong> 아세트아미노펜(타이레놀 등) 계열의 해열진통제를 술과 함께 먹거나, 고지혈증약(스타틴), 일부 항생제 복용 시 일시적으로 간수치가 오를 수 있습니다.</li>
<li><strong>검사 직전 고강도 웨이트 트레이닝:</strong> 검사 전날 무거운 무게로 스쿼트나 데드리프트 등 격렬한 운동을 한 경우, 근육 파괴로 인해 혈중 AST 수치가 100 이상으로 튈 수 있습니다.</li>
</ol>

<h2>간수치 낮추는 4가지 확실한 생활요법</h2>
<ul>
<li><strong>체중의 5~10% 감량:</strong> 의학적으로 입증된 가장 강력한 간 치료법입니다. 체중을 5%만 줄여도 간 내 지방량이 현저히 줄어들며, 10%를 줄이면 간 염증이 정상화됩니다. <a href="/bmi">BMI 계산기</a>로 목표 체중을 설정해 보세요.</li>
<li><strong>액상과당과 정제 탄수화물 끊기:</strong> 간은 당류를 지방으로 전환하는 공장입니다. 탄산음료, 과일주스, 달달한 커피믹스를 물로 바꾸는 것만으로도 4주 만에 ALT 수치가 떨어집니다.</li>
<li><strong>모든 즙과 영양제 2주간 중단해보기:</strong> 간수치가 원인 모르게 높다면 평소 먹던 종합비타민, 영양제, 건강즙을 2~4주간 모두 중단하고 피검사를 다시 해보세요. 상당수가 정상으로 회복됩니다.</li>
<li><strong>완전한 금주:</strong> 간이 손상된 상태에서 알코올 섭취는 불난 집에 기름을 붓는 격입니다. 최소 한 달간 술자리를 완전히 피해야 합니다.</li>
</ul>

<h2>참고자료</h2>
<ul>
<li>대한간학회 – 비알코올성 지방간질환 진료지침 개정안</li>
<li>질병관리청 국가건강정보포털 – 간기능 검사와 간수치 해석</li>
<li>The American Journal of Gastroenterology – ACG Clinical Guideline: Evaluation of Abnormal Liver Chemistries</li>
</ul>
<blockquote><p>본 정보는 일반적인 건강 상식 제공을 목적으로 하며 전문의의 진료를 대신할 수 없습니다. 간수치가 지속적으로 높거나 황달, 극심한 피로가 동반되는 경우 소화기내과 전문의의 정밀 초음파 및 혈액검사를 받으시기 바랍니다.</p></blockquote>
<div class="crp_related crp-text-only"><h3>함께 읽으면 좋은 정보</h3><ul><li><a href="/health/fatty-liver-foods-diet/" class="crp_link"><span class="crp_title">지방간에 좋은 음식과 피해야 할 음식, 식단에서 먼저 바꿀 것</span></a></li><li><a href="/health/cholesterol-test-results-guide/" class="crp_link"><span class="crp_title">콜레스테롤 검사표 읽는 법, 총콜레스테롤보다 먼저 볼 숫자</span></a></li><li><a href="/health/소주-주량-계산/" class="crp_link"><span class="crp_title">소주 주량 계산과 알코올 분해 시간 가이드</span></a></li></ul><div class="crp_clear"></div></div>
"""
    },
    {
        "slug": "fasting-cardio-fat-loss-timing",
        "title": "공복 유산소 운동 vs 식후 운동 효과 비교, 체지방 감량과 근손실 방지 가이드",
        "short_title": "공복 유산소 vs 식후 운동 비교｜체지방 감량·근손실",
        "meta_desc": "아침 공복 유산소 운동의 체지방 연소 과학적 원리와 근손실 예방 심박수, 식후 근력 운동과의 칼로리 소모 비교, 목표별 최적의 운동 시간대를 안내합니다.",
        "published_iso": "2026-10-05T14:00:00+09:00",
        "modified_iso": "2026-10-05T14:00:00+09:00",
        "display_date": "10월 5, 2026",
        "tags": ["공복 유산소", "공복 운동 효과", "근손실", "체지방 감량", "운동 타이밍"],
        "img_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=800&h=450&fit=crop&q=80",
        "img_alt": "공복 유산소 운동과 식후 운동 효과 비교 및 근손실 방지",
        "body_html": """
<p>다이어트를 시작하면 가장 먼저 듣는 조언 중 하나가 “아침 공복에 유산소 운동을 뛰면 뱃살이 훨씬 빨리 빠진다”는 말입니다. 반면에 “공복에 뛰면 근육이 다 녹아내린다(근손실)”며 극구 반대하는 의견도 만만치 않습니다.</p>
<p><strong>공복 유산소 운동은 실제로 체지방 산화율을 높이는 강력한 무기이지만, 강도와 시간을 잘못 설정하면 귀중한 골격근을 잃을 위험이 있습니다. 운동 생리학 연구 데이터를 바탕으로 공복 운동과 식후 운동의 장단점, 그리고 목표별 최적의 실천 가이드를 정리했습니다.</strong></p>

<h2>공복 유산소 운동, 왜 지방이 더 잘 탈까?</h2>
<p>수면을 취하는 8~10시간 동안 우리는 아무 음식도 먹지 않습니다. 기상 직후 몸 안에서는 다음과 같은 생리적 변화가 일어납니다.</p>
<ul>
<li><strong>인슐린 수치의 바닥:</strong> 인슐린은 혈당을 낮추는 호르몬이지만 동시에 체지방 분해를 억제하는 성질이 있습니다. 밤새 공복 상태에서는 혈중 인슐린 농도가 가장 낮아 지방 분해 효소(HSL)의 활동이 극대화됩니다.</li>
<li><strong>간 글리코겐 고갈:</strong> 간에 저장된 탄수화물(글리코겐)이 수면 중 상당량 소모되어, 몸은 주 에너지원으로 체내 축적된 지방산을 끌어다 쓰게 됩니다. 연구에 따르면 식후 운동 대비 공복 유산소 시 지방 산화율이 약 <strong>20~30%</strong> 높게 나타납니다.</li>
</ul>

<h2>공복 유산소 운동 vs 식후 운동 비교표</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>아침 공복 유산소 운동</th>
<th>식후 운동 (식사 후 1.5~2시간)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>주요 에너지원</strong></td>
<td><strong>체지방 (지방산 산화 비중 ↑)</strong></td>
<td>섭취한 탄수화물 (혈당 및 글리코겐)</td>
</tr>
<tr>
<td><strong>장점</strong></td>
<td>단기 체지방 컷팅 효과 극대화, 하루 대사 활성화</td>
<td>최대 근력 발휘 가능, 고강도 지속 시간 ↑</td>
</tr>
<tr>
<td><strong>단점 및 위험</strong></td>
<td>근손실 위험, 저혈당 쇼크, 어지러움</td>
<td>소화 불량 가능성 (식사 직후 운동 시)</td>
</tr>
<tr>
<td><strong>추천 운동 종류</strong></td>
<td><strong>빠르게 걷기, 경사로 트레드밀, 실내 자전거</strong></td>
<td><strong>웨이트 트레이닝 (스쿼트, 벤치프레스 등 고중량)</strong></td>
</tr>
<tr>
<td><strong>적정 운동 시간</strong></td>
<td><strong>30분 ~ 45분 이내</strong></td>
<td>50분 ~ 90분</td>
</tr>
</tbody>
</table>

<h2>공복 유산소 시 '근손실' 막는 3대 수칙</h2>
<ol>
<li><strong>심박수 60~70%의 중저강도 유지:</strong> 숨이 턱 끝까지 차오르는 전력 질주나 고강도 인터벌은 공복에 금물입니다. 에너지가 부족해 체내 코르티솔 호르몬이 급증하며 근육 단백질을 쪼개어 쓰기 시작합니다. 옆 사람과 가볍게 대화할 수 있는 정도(시속 5.5~6.2km 빠르게 걷기)가 가장 지방 연소 효율이 높습니다.</li>
<li><strong>운동 시간은 최대 45분을 넘기지 말 것:</strong> 45분을 넘어가면 지방 연소 속도보다 당신생 작용(근육 단백질 분해) 속도가 더 빨라집니다. 30분 내외가 가장 안전합니다.</li>
<li><strong>운동 직전 미온수 300ml 필수 섭취:</strong> 밤새 탈수된 상태에서 땀을 흘리면 혈액 점도가 높아져 심혈관에 큰 부담을 줍니다. 반드시 기상 직후 물 한 잔을 마시고 운동을 시작하세요. <a href="/water">물 섭취량 계산기</a>를 참고하세요.</li>
</ol>

<h2>내 목표에 맞는 운동 시간표 선택하기</h2>
<ul>
<li><strong>체지방 감량 및 다이어트가 최우선인 경우:</strong><br>
➜ 기상 직후 미온수 1잔 ➜ 30~40분 경사로 빠르게 걷기 ➜ 운동 후 30분 이내 달걀, 그릭요거트 등 단백질 식사. <a href="/calorie">하루 칼로리 계산기</a>로 감량 칼로리를 체크하세요.</li>
<li><strong>근육량 증가 및 탄탄한 몸매가 목표인 경우:</strong><br>
➜ 식사 후 1.5~2시간 뒤 탄수화물이 충전된 상태에서 50분 근력 운동 ➜ 마무리 유산소 20분 ➜ 단백질 보충. <a href="/protein">단백질 계산기</a>로 권장량을 확인하세요.</li>
<li><em>※ 주의: 당뇨 환자는 공복 운동 시 치명적인 저혈당 쇼크가 올 수 있으므로 식후 30분~1시간 뒤 운동을 시작해야 합니다.</em></li>
</ul>

<h2>참고자료</h2>
<ul>
<li>British Journal of Nutrition – Breakfast and exercise timing affect postprandial metabolism and energy intake</li>
<li>Journal of Functional Morphology and Kinesiology – Exercise and Fasting: Physiological Mechanisms and Health Impacts</li>
<li>질병관리청 국가건강정보포털 – 비만과 신체활동 가이드</li>
</ul>
<blockquote><p>본 콘텐츠는 건강 증진을 목적으로 한 운동 생리학 정보이며, 심혈관 질환이나 당뇨병 등 만성질환자는 운동 시작 전 주치의와 상담하여 안전한 운동 강도를 설정하시기 바랍니다.</p></blockquote>
<div class="crp_related crp-text-only"><h3>함께 읽으면 좋은 정보</h3><ul><li><a href="/health/운동-소모-칼로리-계산/" class="crp_link"><span class="crp_title">운동 소모 칼로리 계산과 체지방 1kg 감량 기준</span></a></li><li><a href="/health/근육-유지와-다이어트를-위해-단백질-섭취의-중요성/" class="crp_link"><span class="crp_title">근육 유지와 다이어트를 위한 단백질 섭취의 중요성</span></a></li><li><a href="/health/blood-sugar-spike-prevention-diet/" class="crp_link"><span class="crp_title">식후 혈당 스파이크 증상과 낮추는 법, 거꾸로 식사법과 15분 걷기</span></a></li></ul><div class="crp_clear"></div></div>
"""
    }
]

# Write the 2 new articles
for art in new_articles:
    art_dir = REPO_DIR / "health" / art["slug"]
    art_dir.mkdir(parents=True, exist_ok=True)
    art_file = art_dir / "index.html"
    
    content = template
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
    
    content = re.sub(r'https://healthfit100.com/health/cholesterol-test-results-guide/', f'https://healthfit100.com/health/{art["slug"]}/', content)
    content = re.sub(r'2026-08-07T09:00:00\+09:00', art["published_iso"], content)
    content = re.sub(r'2026-08-08T17:32:54\+09:00', art["modified_iso"], content)
    
    content = re.sub(r'<h1 class="entry-title" itemprop="headline">.*?</h1>', f'<h1 class="entry-title" itemprop="headline">{art["title"]}</h1>', content)
    content = re.sub(r'<span class="published" itemprop="datePublished">.*?</span>', f'<span class="published" itemprop="datePublished"> {art["display_date"]} </span>', content)
    
    fig_html = f'''<figure class="post-thumb-img-content" style="margin:0 0 1.5em 0;border-radius:8px;overflow:hidden;text-align:center;">
<img src="{art['img_url']}" alt="{art['img_alt']}" width="800" height="450" loading="lazy" style="width:100%;height:auto;display:block;object-fit:cover;">
<figcaption style="font-size:12px;color:#888888;margin-top:6px;text-align:center;">사진 출처: Unsplash</figcaption>
</figure>'''
    
    if '<header class="entry-header ">' in content:
        content = content.replace('<header class="entry-header ">', f'{fig_html}\n<header class="entry-header ">', 1)
        
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
    
    full_art_html = before_body + "\n" + art["body_html"] + "\n" + after_body
    art_file.write_text(full_art_html, encoding="utf-8")
    print(f"Created: {art_file}")

# 3. Update existing vitamin-d article date to 10월 1일
vitd_path = REPO_DIR / "health" / "vitamin-d-benefits-daily-intake-timing" / "index.html"
if vitd_path.exists():
    vc = vitd_path.read_text(encoding="utf-8-sig")
    vc = vc.replace("2026-10-03", "2026-10-01")
    vc = vc.replace("10월 3, 2026", "10월 1, 2026")
    vitd_path.write_text(vc, encoding="utf-8")
    print("Updated vitamin-d date to 10월 1일")

# 4. Update blog.html
blog_path = REPO_DIR / "blog.html"
blog_c = blog_path.read_text(encoding="utf-8-sig")

blog_entries_2 = """
<article class="post-406 post type-post status-publish format-standard hentry category-health ast-grid-common-col ast-full-width ast-article-post remove-featured-img-padding" id="post-406" itemtype="https://schema.org/CreativeWork" itemscope="itemscope">
		<div class="ast-post-format- ast-no-thumb blog-layout-4 ast-article-inner">
	<div class="post-content ast-grid-common-col">
		<span class="ast-blog-single-element ast-taxonomy-container cat-links default"><a href="/blog" rel="category tag">건강,영양</a></span><h2 class="entry-title ast-blog-single-element" itemprop="headline"><a href="https://healthfit100.com/health/fasting-cardio-fat-loss-timing" rel="bookmark">공복 유산소 운동 vs 식후 운동 효과 비교, 체지방 감량과 근손실 방지 가이드</a></h2>
		<header class="entry-header ast-blog-single-element ast-blog-meta-container">
			<div class="entry-meta"><span class="posted-by vcard author" itemtype="https://schema.org/Person" itemscope="itemscope" itemprop="author"><a title="건강노트의 모든 글 보기" href="https://healthfit100.com/about" rel="author" class="url fn n" itemprop="url"><span class="author-name" itemprop="name">건강노트</span></a></span> / <span class="posted-on"><span class="published" itemprop="datePublished"> 10월 5, 2026 </span></span></div>
		</header>
		<div class="ast-excerpt-container ast-blog-single-element"><p>아침 공복 유산소 운동의 체지방 연소 과학적 원리와 근손실 예방 심박수, 식후 근력 운동과의 칼로리 소모 비교, 목표별 최적의 운동 시간대를 안내합니다.</p></div>
		<div class="entry-content clear" itemprop="text"></div>
	</div>
</div>
	</article>
<article class="post-404 post type-post status-publish format-standard hentry category-health ast-grid-common-col ast-full-width ast-article-post remove-featured-img-padding" id="post-404" itemtype="https://schema.org/CreativeWork" itemscope="itemscope">
		<div class="ast-post-format- ast-no-thumb blog-layout-4 ast-article-inner">
	<div class="post-content ast-grid-common-col">
		<span class="ast-blog-single-element ast-taxonomy-container cat-links default"><a href="/blog" rel="category tag">건강,영양</a></span><h2 class="entry-title ast-blog-single-element" itemprop="headline"><a href="https://healthfit100.com/health/liver-enzymes-ast-alt-guide" rel="bookmark">간수치 AST ALT 정상 수치와 해석, 높은 이유와 낮추는 법</a></h2>
		<header class="entry-header ast-blog-single-element ast-blog-meta-container">
			<div class="entry-meta"><span class="posted-by vcard author" itemtype="https://schema.org/Person" itemscope="itemscope" itemprop="author"><a title="건강노트의 모든 글 보기" href="https://healthfit100.com/about" rel="author" class="url fn n" itemprop="url"><span class="author-name" itemprop="name">건강노트</span></a></span> / <span class="posted-on"><span class="published" itemprop="datePublished"> 10월 5, 2026 </span></span></div>
		</header>
		<div class="ast-excerpt-container ast-blog-single-element"><p>건강검진 간수치 AST(GOT)·ALT(GPT) 정상 범위(40 IU/L 이하)와 수치가 높아지는 주요 원인(비알코올성 지방간, 음주, 약물·즙), 식단과 생활습관으로 낮추는 법을 정리했습니다.</p></div>
		<div class="entry-content clear" itemprop="text"></div>
	</div>
</div>
	</article>
"""

# replace vitamin-d date in blog.html as well
blog_c = blog_c.replace("10월 3, 2026 </span></span></div>\n\t\t</header>\n\t\t<div class=\"ast-excerpt-container ast-blog-single-element\"><p>한국인 80%가 겪는 비타민D", "10월 1, 2026 </span></span></div>\n\t\t</header>\n\t\t<div class=\"ast-excerpt-container ast-blog-single-element\"><p>한국인 80%가 겪는 비타민D")
if '<div class="ast-row">' in blog_c:
    blog_c = blog_c.replace('<div class="ast-row">', f'<div class="ast-row">{blog_entries_2}', 1)
    blog_path.write_text(blog_c, encoding="utf-8")
    print("Updated blog.html with 2 new posts")

# 5. Update index.html: Add October Special Banner + 2 new cards + Fact-check policy section
index_path = REPO_DIR / "index.html"
index_c = index_path.read_text(encoding="utf-8-sig")

october_banner = """
      <!-- 10월 특별 기획 큐레이션 -->
      <div style="background: linear-gradient(135deg, #1e3a8a, #0284c7); border-radius: 18px; padding: 28px 32px; color: #fff; margin-bottom: 40px; box-shadow: 0 10px 25px rgba(2,132,199,0.18);">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
          <span style="background:rgba(255,255,255,0.2); padding:4px 12px; border-radius:999px; font-size:0.8rem; font-weight:700; letter-spacing:0.5px;">🍂 10월 테마 큐레이션</span>
          <span style="font-size:0.85rem; opacity:0.9;">환절기 건강 관리</span>
        </div>
        <h2 style="margin:0 0 10px; font-size:1.6rem; font-weight:800; color:#fff; border:none; padding:0;">10월 환절기 혈관·혈당·간수치 집중 관리 가이드</h2>
        <p style="margin:0 0 20px; font-size:0.95rem; opacity:0.9; line-height:1.6; max-width:680px;">
          일교차가 10도 이상 벌어지는 가을철에는 혈관 수축으로 인한 혈압 급상승과 면역력 저하, 식욕 증가로 인한 혈당 스파이크에 각별히 유의해야 합니다. 공신력 있는 의학 학회 지침을 바탕으로 엄선한 이달의 추천 가이드입니다.
        </p>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px;">
          <a href="/health/blood-pressure-stages-hypertension-diet/" style="background:rgba(255,255,255,0.15); border-radius:12px; padding:14px 16px; text-decoration:none; color:#fff; transition:background 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
            <div style="font-size:0.8rem; opacity:0.8;">심혈관 관리</div>
            <strong style="font-size:0.95rem; display:block; margin-top:2px;">고혈압 전단계 낮추는 법 →</strong>
          </a>
          <a href="/health/blood-sugar-spike-prevention-diet/" style="background:rgba(255,255,255,0.15); border-radius:12px; padding:14px 16px; text-decoration:none; color:#fff; transition:background 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
            <div style="font-size:0.8rem; opacity:0.8;">식후 대사</div>
            <strong style="font-size:0.95rem; display:block; margin-top:2px;">혈당 스파이크 거꾸로 식사법 →</strong>
          </a>
          <a href="/health/liver-enzymes-ast-alt-guide/" style="background:rgba(255,255,255,0.15); border-radius:12px; padding:14px 16px; text-decoration:none; color:#fff; transition:background 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
            <div style="font-size:0.8rem; opacity:0.8;">건강검진표</div>
            <strong style="font-size:0.95rem; display:block; margin-top:2px;">간수치 AST·ALT 해석 가이드 →</strong>
          </a>
          <a href="/health/vitamin-d-benefits-daily-intake-timing/" style="background:rgba(255,255,255,0.15); border-radius:12px; padding:14px 16px; text-decoration:none; color:#fff; transition:background 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
            <div style="font-size:0.8rem; opacity:0.8;">면역 영양소</div>
            <strong style="font-size:0.95rem; display:block; margin-top:2px;">비타민D 복용시간 & 권장량 →</strong>
          </a>
        </div>
      </div>
"""

home_cards_2 = """
        <!-- New Post: Liver AST ALT -->
        <article class="custom-card-list-item">
          <a href="/health/liver-enzymes-ast-alt-guide/" class="custom-card-thumb-link" aria-label="간수치 AST ALT 정상 수치와 해석">
            <img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=400&h=260&fit=crop&q=80" alt="간기능 검사 AST ALT 수치와 낮추는 법" loading="lazy">
          </a>
          <div class="custom-card-body">
            <div class="custom-card-meta">
              <span class="custom-card-category">간 건강·검진</span>
              <span>5분 읽기 · 대한간학회 지침 기반</span>
            </div>
            <h3 class="custom-card-title">
              <a href="/health/liver-enzymes-ast-alt-guide/">간수치 AST ALT 정상 수치와 해석, 높은 이유와 낮추는 법</a>
            </h3>
            <p class="custom-card-excerpt">
              건강검진표에서 가장 흔하게 지적받는 간수치 AST(GOT)와 ALT(GPT)의 차이점과 정상 범위(40 IU/L 이하), 비알코올성 지방간과 과도한 즙 복용으로 인한 간수치 상승을 5% 체중 감량으로 낮추는 방법을 체계적으로 안내합니다.
            </p>
          </div>
        </article>

        <!-- New Post: Fasting Cardio -->
        <article class="custom-card-list-item">
          <a href="/health/fasting-cardio-fat-loss-timing/" class="custom-card-thumb-link" aria-label="공복 유산소 운동 vs 식후 운동 효과 비교">
            <img src="https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=400&h=260&fit=crop&q=80" alt="공복 유산소 운동과 식후 운동 비교" loading="lazy">
          </a>
          <div class="custom-card-body">
            <div class="custom-card-meta">
              <span class="custom-card-category">운동·다이어트</span>
              <span>5분 읽기 · 운동 생리학 연구 분석</span>
            </div>
            <h3 class="custom-card-title">
              <a href="/health/fasting-cardio-fat-loss-timing/">공복 유산소 운동 vs 식후 운동 효과 비교, 체지방 감량과 근손실 방지 가이드</a>
            </h3>
            <p class="custom-card-excerpt">
              아침 공복에 유산소 운동을 할 때 지방산 산화율이 20~30% 증가하는 생리학적 원리와 근손실(단백질 분해)을 막는 심박수 60~70% 중저강도 유지 수칙, 개인의 목표에 맞는 최적의 운동 타이밍을 비교 정리했습니다.
            </p>
          </div>
        </article>
"""

# Insert banner above '<h2 class="section-title">✍️ 최신 & 추천 건강 칼럼</h2>'
banner_marker = '<h2 class="section-title">✍️ 최신 & 추천 건강 칼럼</h2>'
if banner_marker in index_c:
    index_c = index_c.replace(banner_marker, f'{october_banner}\n{banner_marker}', 1)

# Insert new cards into post list
card_marker = '<div style="display:flex;flex-direction:column;gap:18px;margin-bottom:55px;">'
if card_marker in index_c:
    index_c = index_c.replace(card_marker, f'{card_marker}\n{home_cards_2}', 1)

# Add Editorial Fact-check Policy box near bottom of index.html
policy_box = """
      <!-- 건강노트 3대 콘텐츠 검증 및 편집 원칙 (E-E-A-T) -->
      <section style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:18px; padding:32px; margin-bottom:50px;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
          <span style="font-size:1.5rem;">🛡️</span>
          <h2 style="margin:0; font-size:1.35rem; font-weight:800; color:#0f172a;">건강노트의 3대 콘텐츠 검증 및 작성 원칙</h2>
        </div>
        <p style="color:#64748b; font-size:0.93rem; margin:0 0 22px; line-height:1.6;">
          건강노트는 인터넷상에 무분별하게 퍼져 있는 불확실한 건강 정보와 상업적 광고를 배제하고, 독자에게 신뢰할 수 있는 정확한 건강 지식을 전달하기 위해 아래의 엄격한 편집 원칙을 준수합니다.
        </p>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:20px;">
          <div style="background:#fff; border:1px solid #edf2f7; border-radius:12px; padding:20px;">
            <div style="font-weight:700; color:#0284c7; margin-bottom:6px;">1. 공인된 1차 의학 출처 인용</div>
            <p style="margin:0; font-size:0.88rem; color:#475569; line-height:1.6;">
              보건복지부, 질병관리청(KDCA), 대한당뇨병학회, 대한고혈압학회, 한국지질·동맥경화학회 등 국가 공공기관 및 전문 의학 학회의 최신 공식 지침과 학술 논문만을 1차 근거로 사용합니다.
            </p>
          </div>
          <div style="background:#fff; border:1px solid #edf2f7; border-radius:12px; padding:20px;">
            <div style="font-weight:700; color:#0284c7; margin-bottom:6px;">2. 상업적 제품 광고 배제</div>
            <p style="margin:0; font-size:0.88rem; color:#475569; line-height:1.6;">
              특정 제약사나 영양제 브랜드의 협찬·유료 광고성 리뷰를 일절 작성하지 않으며, 특정 상품을 강요하지 않고 성분 자체의 과학적 기전과 일일 섭취 기준치에 집중합니다.
            </p>
          </div>
          <div style="background:#fff; border:1px solid #edf2f7; border-radius:12px; padding:20px;">
            <div style="font-weight:700; color:#0284c7; margin-bottom:6px;">3. 주기적 팩트체크와 갱신</div>
            <p style="margin:0; font-size:0.88rem; color:#475569; line-height:1.6;">
              매년 개정되는 한국인 영양소 섭취기준 및 보건 정책 변화에 맞춰 기존에 발행된 글들의 수치와 기준을 정기적으로 재검토하고 최신 정보로 업데이트합니다.
            </p>
          </div>
        </div>
      </section>
"""

editor_principle_marker = '<h2 class="section-title">🌿 에디터의 3대 건강 관리 원칙</h2>'
if editor_principle_marker in index_c:
    index_c = index_c.replace(editor_principle_marker, f'{policy_box}\n{editor_principle_marker}', 1)

index_path.write_text(index_c, encoding="utf-8")
print("Updated index.html with October banner, cards, and policy box")

# 6. Update about.html with Editorial Policy as well
about_path = REPO_DIR / "about.html"
about_c = about_path.read_text(encoding="utf-8-sig")
if "<h2>건강노트의 3대 가치</h2>" in about_c:
    about_policy = """
        <h2>건강노트의 3대 정보 검증 원칙 (Editorial Policy)</h2>
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:14px; padding:24px; margin-bottom:30px;">
          <ul style="margin:0; padding-left:20px; line-height:1.8; color:#334155;">
            <li><strong>공식 보건 당국 및 전문 학회 1차 근거 기반:</strong> 질병관리청(KDCA), 보건복지부, 대한당뇨병학회, 대한고혈압학회 등의 공식 진료 가이드라인을 철저히 확인하여 글을 작성합니다.</li>
            <li><strong>특정 상업 제품 배제 및 중립성 유지:</strong> 광고성 대가나 특정 건강식품 브랜드의 협찬을 일절 배제하며 객관적인 성분과 영양 가치만을 다룹니다.</li>
            <li><strong>지속적인 데이터 업데이트:</strong> 매년 변경되는 섭취 기준 및 의학 연구에 발맞추어 주기적으로 콘텐츠의 수치를 검증하고 수정합니다.</li>
          </ul>
        </div>
"""
    about_c = about_c.replace("<h2>건강노트의 3대 가치</h2>", f'{about_policy}\n<h2>건강노트의 3대 가치</h2>', 1)
    about_path.write_text(about_c, encoding="utf-8")
    print("Updated about.html with Editorial Policy")

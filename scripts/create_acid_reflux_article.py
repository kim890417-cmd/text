import os
import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Base template from fasting-blood-sugar-normal-range-prediabetes
template_path = REPO_DIR / "health" / "fasting-blood-sugar-normal-range-prediabetes" / "index.html"
template = template_path.read_text(encoding="utf-8")

slug = "acid-reflux-gerd-symptoms-diet-foods"
title = "역류성 식도염 증상과 좋은 음식 피해야 할 음식, 목 이물감 없애는 식후 습관"
meta_desc = "가슴 쓰림과 목 이물감, 신트림을 유발하는 역류성 식도염(GERD)의 원인과 하부식도괄약근 보호 원리, 양배추·바나나 등 위벽을 살리는 식단과 식후 3시간 생활수칙을 정리했습니다."
published_iso = "2026-10-11T09:00:00+09:00"
modified_iso = "2026-10-11T09:00:00+09:00"
display_date = "10월 11, 2026"
post_id = "411"

body_html = """
<p>식사 후 가슴 한가운데가 타는 듯이 쓰라리거나, 목구멍에 가시가 걸린 것처럼 답답한 이물감 때문에 헛기침을 해보신 적 있으신가요? 많은 분들이 단순한 감기나 일시적인 소화불량으로 넘기기 쉽지만, 이는 위산과 소화 효소가 식도를 타고 거꾸로 넘어와 점막을 태우는 <strong>'역류성 식도염(위식도역류질환, GERD)'</strong>의 전형적인 신호입니다.</p>

<p>저 역시 과거 방송 제작(PD) 시절, 며칠 밤을 새우며 편집실에서 쏟아지는 잠을 쫓겠다고 빈속에 차가운 아메리카노를 서너 잔씩 들이붓고, 자정이 넘은 시간에 배달 피자나 야식을 급하게 먹은 뒤 곧바로 소파에 곯아떨어지던 최악의 습관을 몇 년간 반복했습니다. (지금 돌아보면 몸을 스스로 망치는 자해나 다름없었죠.) 결국 목에 무언가 꽉 막힌 느낌과 밤마다 터져 나오는 마른기침으로 물 한 모금 삼키기 힘들어 내시경 검사를 받았고, 식도 하부가 붉게 헐어있는 중증 역류성 식도염 진단을 받았습니다. 약을 먹어도 습관을 바꾸지 않으면 몇 달 만에 재발하는 고통을 뼈저리게 겪었습니다.</p>

<p>대학에서 식품학을 공부하며 위장 생리학과 소화기 운동 메커니즘을 다시 깊이 파고들었을 때 해답을 찾을 수 있었습니다. 위장과 식도를 연결하는 조임근인 <strong>'하부식도괄약근(LES)'의 압력을 떨어뜨리는 음식을 식판에서 걷어내고, 식후 3시간 중력의 법칙을 지키는 것</strong>이 평생 위산 역류의 악순환에서 벗어나는 유일한 의학적 돌파구입니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>역류성 식도염의 대표 증상과 자가진단 기준</h2>
<p><strong>역류성 식도염은 위 속의 강산성 내용물이 식도로 역류하여 점막을 손상시키는 질환으로, 가슴 쓰림과 산 역류, 목 이물감 및 만성 기침이 대표적인 핵심 증상입니다.</strong></p>

<p>위 점막은 pH 1.5~2.0에 달하는 강력한 염산(위산)을 견딜 수 있는 두꺼운 점액 방어벽을 가지고 있습니다. 반면 식도는 보호막이 없는 얇은 편평상피세포로 이루어져 있어, 강산에 단 몇 분만 노출되어도 세포가 타들어가며 미세한 궤양과 염증이 발생합니다.</p>

<table>
  <thead>
    <tr>
      <th>구분</th>
      <th>대표적인 주요 증상</th>
      <th>생리학적 원인 및 특징</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>전형적 증상</strong></td>
      <td><strong>가슴 쓰림 (Heartburn)</strong></td>
      <td>명치끝에서 목구멍 쪽으로 불길이 치밀어 오르는 듯한 작열감</td>
    </tr>
    <tr>
      <td><strong>전형적 증상</strong></td>
      <td><strong>위산 역류 (Acid Regurgitation)</strong></td>
      <td>트림할 때 시큼하고 쓴맛이 나는 액체가 입안까지 넘어옴</td>
    </tr>
    <tr>
      <td><strong>비전형적 증상</strong></td>
      <td><strong>인후두 이물감 (목 이물감)</strong></td>
      <td>목에 솜뭉치나 가래가 걸린 듯 뱉어지지도 삼켜지지도 않는 느낌</td>
    </tr>
    <tr>
      <td><strong>비전형적 증상</strong></td>
      <td><strong>만성 마른기침 &amp; 쉰 목소리</strong></td>
      <td>역류한 위산 미립자가 성대와 기도를 자극해 3주 이상 지속되는 기침</td>
    </tr>
    <tr>
      <td><strong>경고 증상</strong></td>
      <td><strong>연하곤란 (음식 걸림 현상)</strong></td>
      <td>식도 점막이 반복적으로 손상되어 좁아진 상태 (즉시 전문의 내시경 필요)</td>
    </tr>
  </tbody>
</table>

<p>대한소화기기능성질환·운동학회 통계에 따르면 한국인 10명 중 1명 이상이 위식도역류질환을 앓고 있습니다. 만약 이를 방치하여 식도 점막 손상이 만성화되면 식도 점막 세포가 장 점막처럼 변하는 '바렛 식도(Barrett's Esophagus)'로 진행될 수 있으며, 이는 식도암의 전단계 위험 인자로 꼽힙니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>식도 괄약근을 살리는 5대 위벽 보호 식품</h2>
<p>역류성 식도염을 관리할 때는 위산 분비를 자극하지 않으면서 손상된 식도 점막을 물리적으로 코팅하고 소화 부담을 줄여주는 음식을 선택해야 합니다.</p>

<h3>1. 양배추 (비타민 U / S-메틸메티오닌)</h3>
<p>양배추의 핵심 유효 성분인 비타민 U(S-Methylmethionine)는 위장 점막 세포의 단백질 합성을 촉진하여 헐어버린 식도벽과 위벽의 상처를 재생하는 탁월한 치유 작용을 합니다. 단, 생양배추를 너무 차갑게 많이 먹으면 가스가 차서 복압을 올릴 수 있으므로 살짝 찌거나 삶아서 섭취하는 것이 가장 이상적입니다.</p>

<h3>2. 바나나 (천연 알칼리 완충 작용)</h3>
<p>바나나는 pH 5.6 안팎의 약알칼리성 식품으로, 위산을 중화시켜 가슴 쓰림을 즉각적으로 가라앉히는 천연 완충제 역할을 합니다. 풍부한 수용성 식이섬유인 펙틴(Pectin)은 위벽을 부드럽게 감싸 소화관 점막의 자극을 줄여줍니다.</p>

<h3>3. 마 (뮤신 성분의 점막 보호막)</h3>
<p>마를 잘랐을 때 나오는 끈적끈적한 액체는 당단백질의 일종인 <strong>뮤신(Mucin)</strong>입니다. 뮤신은 인체 소화관 점액과 매우 유사한 구조를 가지고 있어, 위산이 식도 점막에 직접 닿지 않도록 그물망 형태의 강력한 보호 코팅층을 형성합니다.</p>

<h3>4. 브로콜리 (설포라판과 위염 억제)</h3>
<p>브로콜리는 항산화 물질인 설포라판(Sulforaphane)이 풍부하여 위장 내 염증을 유발하는 헬리코박터균의 증식을 억제하고 소화기 점막의 만성 염증을 가라앉히는 데 도움을 줍니다. 부드럽게 데쳐서 식사 첫머리에 섭취하면 소화 속도를 조절해 줍니다.</p>

<h3>5. 감자 (알칼리성 전분의 위산 흡착)</h3>
<p>생감자를 갈아 가라앉힌 전분 앙금이나 찐 감자는 위산 과다 분비를 진정시키는 대표적인 알칼리성 식품입니다. 산성화된 위장 환경을 중화시켜 식도로 치밀어 오르는 작열감을 빠르게 완화시킵니다.</p>

<div style="background:#f0fdf4; border:1.5px solid #bbf7d0; border-radius:12px; padding:20px; margin:28px 0;">
  <strong style="color:#166534; font-size:1.05rem; display:block; margin-bottom:6px;">[수분과 위산 관리] 하루 물 섭취량과 올바른 마시는 타이밍</strong>
  <p style="font-size:0.92rem; color:#475569; margin:0 0 14px; line-height:1.5;">식사 직전이나 식사 도중에 물을 벌컥벌컥 마시면 위액이 희석되어 소화가 지연되고 위 용적이 늘어나 역류가 심해집니다. 나의 적정 물 섭취량과 안전한 복용 타이밍을 확인해 보세요.</p>
  <a href="/water" style="display:inline-block; background:#16a34a; color:#fff; padding:10px 20px; border-radius:8px; font-weight:700; text-decoration:none; font-size:0.9rem;">하루 물 권장 섭취량 계산기 바로가기 →</a>
</div>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>이것만은 절대 금지: 식도 괄약근을 열어젖히는 5대 악마 식품</h2>
<p>역류성 식도염 치료의 핵심은 좋은 음식을 먹는 것보다 <strong>조임근을 느슨하게 만드는 음식을 완벽히 차단하는 것</strong>입니다. 아무리 양배추즙을 마셔도 아래 식품을 끊지 못하면 밑 빠진 독에 물 붓기입니다.</p>

<ul>
  <li><strong>1. 커피 및 고함량 카페인 (메틸크산틴):</strong> 카페인 성분은 하부식도괄약근의 평활근을 직접 이완시켜 문을 헐겁게 열어버립니다. 빈속의 모닝커피는 식도염 환자에게 독약입니다. 나의 하루 안전 카페인 한도는 <a href="/caffeine">카페인 안전 섭취량 계산기</a>에서 확인하실 수 있습니다.</li>
  <li><strong>2. 초콜릿 (테오브로민과 지방):</strong> 초콜릿 속 테오브로민은 식도 조임근을 마비시키듯 느슨하게 풀고, 고농도 지방 성분이 위장 배출 시간을 2배 이상 늦춥니다.</li>
  <li><strong>3. 기름진 튀김 및 삼겹살:</strong> 지방질이 많은 고기류는 소화하는 데 4~5시간 이상 걸리며, 위산 분비를 촉진하는 호르몬을 대량 방출시켜 위 내부 압력을 폭발적으로 끌어올립니다.</li>
  <li><strong>4. 감귤류·토마토 등 산도가 강한 과일:</strong> 오렌지, 자몽, 레몬, 토마토소스는 자체 산도(pH 3 이하)가 높아 이미 헐어버린 식도 점막에 닿는 순간 극심한 통증과 염증을 유발합니다.</li>
  <li><strong>5. 박하 및 페퍼민트:</strong> 상쾌한 느낌 때문에 소화에 좋을 것이라 착각하기 쉽지만, 박하의 멘톨 성분은 식도 괄약근 긴장도를 직접적으로 떨어뜨리는 대표적인 금기 성분입니다.</li>
</ul>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>재발 없는 위장을 만드는 3대 식후 생활 습관</h2>
<p>역류성 식도염은 약물로 위산 분비를 억제(PPI 제제)하면 일시적으로 호전되지만, 약을 끊으면 80% 이상이 재발합니다. 기계적인 중력과 복압을 다스리는 생활 습관이 뒷받침되어야 완치됩니다.</p>

<h3>1. 식후 3시간 눕기 절대 금지 (중력의 법칙)</h3>
<p>음식이 위장에서 십이지장으로 완전히 내려가는 데는 최소 2~3시간이 걸립니다. 식사 후 졸리다고 소파나 침대에 누워버리면, 중력의 도움을 받지 못해 위 속의 죽 같은 음식물이 식도로 바로 쏟아져 들어옵니다. 저녁 식사는 취침 최소 3시간 전에 끝마쳐야 합니다.</p>

<h3>2. 수면 시 '왼쪽'으로 눕는 자세 유지</h3>
<p>인간의 위장은 신체 왼쪽으로 볼록하게 굽어진 주머니 형태를 띠고 있습니다. 오른쪽으로 누워 자면 위 내용물이 위식도 접합부보다 위쪽에 위치하게 되어 자는 내내 위산이 역류합니다. 반면 <strong>왼쪽으로 누워 자면 위식도 접합부가 위 내용물보다 높은 위치에 자리잡아</strong> 구조적으로 역류가 차단됩니다. 베개 높이를 15cm 정도 완만하게 높여 상체를 살짝 세우는 것도 큰 도움이 됩니다.</p>

<h3>3. 복압을 올리는 복부 압박 차단</h3>
<p>꽉 끼는 벨트, 보정 속옷, 단추를 조이는 바지는 복부 내부 압력을 상승시켜 위장을 쥐어짜듯 위로 밀어 올립니다. 과식이나 폭식을 피하고 밥을 천천히 20분 이상 꼭꼭 씹어 먹는 습관도 위의 팽창을 막아 복압 상승을 방지합니다. 식사 순서를 채소부터 먹는 <a href="/health/blood-sugar-spike-prevention-diet/">거꾸로 식사법</a>을 병행하면 위장 부담을 크게 덜 수 있습니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>에디터의 3줄 요약과 오늘부터 실천할 1가지</h2>
<ul>
  <li><strong>핵심 1:</strong> 목 이물감과 가슴 쓰림은 식도 괄약근(LES)이 느슨해져 위산이 역류하는 명백한 경고 신호입니다.</li>
  <li><strong>핵심 2:</strong> 양배추, 바나나로 점막을 보호하고 커피·초콜릿·기름진 야식을 식탁에서 완전히 끊어내세요.</li>
  <li><strong>핵심 3:</strong> 저녁 식사 후 최소 3시간 동안 눕지 말고, 수면 시에는 반드시 왼쪽으로 누우세요.</li>
</ul>

<p>지금 당장 할 수 있는 가장 확실한 행동은 오늘 저녁 식사를 마친 뒤 소파에 비스듬히 눕는 대신, 편안한 옷으로 갈아입고 거실을 천천히 10분간 서성이는 일입니다. 중력을 아군으로 만드는 순간, 타는 듯한 가슴 쓰림은 멈추기 시작합니다.</p>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #e2e8f0;">

<h2>참고자료 및 공인 출처</h2>
<ul>
  <li>대한소화기기능성질환·운동학회 – 2020 위식도역류질환 서울 가이드라인 (진단 및 생활요법 지침)</li>
  <li>질병관리청 국가건강정보포털 – 위식도역류질환의 증상, 합병증 및 예방 수칙</li>
  <li>American College of Gastroenterology (ACG) – Guidelines for the Diagnosis and Management of Gastroesophageal Reflux Disease (Am J Gastroenterol)</li>
  <li>The American Journal of Clinical Nutrition – Diet and Lifestyle Factors in Gastroesophageal Reflux Disease</li>
</ul>

<blockquote>
  <p><strong>[법적 및 의학적 고지]</strong><br>
  본 콘텐츠는 질병관리청 및 대한소화기기능성질환학회의 학술 지침을 바탕으로 작성된 일반 건강 정보이며, 의사의 전문적인 진단이나 처방을 대신할 수 없습니다. 음식물이 목에 걸려 넘어가지 않거나 피를 토하는 증상(토혈), 체중 감소를 동반한 연하곤란이 있다면 지체 없이 소화기내과 전문의의 정밀 위내시경 검사를 받으시기 바랍니다.</p>
</blockquote>

<div class="crp_related crp-text-only">
  <h3>함께 읽으면 좋은 건강 정보</h3>
  <ul>
    <li><a href="/health/caffeine-daily-intake-limit-side-effects/" class="crp_link"><span class="crp_title">하루 카페인 권장량 400mg, 임산부·청소년 기준과 부작용</span></a></li>
    <li><a href="/health/daily-water-intake-calculator-benefits/" class="crp_link"><span class="crp_title">하루 물 섭취량, 2리터가 모두에게 정답은 아닌 이유</span></a></li>
    <li><a href="/health/blood-sugar-spike-prevention-diet/" class="crp_link"><span class="crp_title">식후 혈당 스파이크 증상과 낮추는 법, 거꾸로 식사법과 15분 걷기 효과</span></a></li>
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

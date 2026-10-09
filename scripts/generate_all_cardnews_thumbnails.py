import os
import glob
import re
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# -------------------------------------------------------------
# Configuration & Fonts
# -------------------------------------------------------------
FONT_DIR = r"C:\Users\sadase\Desktop\블로그 설정\fonts"
F_BLACKHAN = os.path.join(FONT_DIR, "BlackHanSans-Regular.ttf")
F_PRETEND = os.path.join(FONT_DIR, "Pretendard-Bold.ttf")

if not os.path.exists(F_BLACKHAN):
    F_BLACKHAN = r"C:\Windows\Fonts\malgunbd.ttf"
if not os.path.exists(F_PRETEND):
    F_PRETEND = r"C:\Windows\Fonts\malgunbd.ttf"

CACHE_DIR = "images/thumbnails/cache"
os.makedirs(CACHE_DIR, exist_ok=True)

# -------------------------------------------------------------
# Unsplash Fallback Library
# -------------------------------------------------------------
TOPIC_IMAGES = {
    'diet': 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=1080&q=80',
    'workout': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=1080&q=80',
    'nutrition': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=1080&q=80',
    'medical': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=1080&q=80',
    'vitamins': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=1080&q=80',
    'sleep': 'https://images.unsplash.com/photo-1541480601022-2308c0f02487?w=1080&q=80',
    'water': 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=1080&q=80',
    'coffee': 'https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=1080&q=80',
    'alcohol': 'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=1080&q=80',
    'eye': 'https://images.unsplash.com/photo-1508847154043-be5407fcaa5a?w=1080&q=80',
    'blood': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1080&q=80',
    'weight': 'https://images.unsplash.com/photo-1576678927484-cc907957088c?w=1080&q=80',
    'protein': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1080&q=80',
    'pregnancy': 'https://images.unsplash.com/photo-1491013516836-7db643ee125a?w=1080&q=80',
    'default': 'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=1080&q=80'
}

def download_or_load_image(img_url_or_path: str, cache_name: str) -> Image.Image:
    if not img_url_or_path:
        img_url_or_path = TOPIC_IMAGES['default']

    if img_url_or_path.startswith('http'):
        # ensure high resolution
        if 'unsplash.com' in img_url_or_path:
            base_url = img_url_or_path.split('?')[0]
            clean_url = f"{base_url}?w=1080&q=85"
        else:
            clean_url = img_url_or_path

        cache_file = os.path.join(CACHE_DIR, f"{cache_name}.jpg")
        if not os.path.exists(cache_file):
            try:
                req = urllib.request.Request(clean_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as resp, open(cache_file, 'wb') as f:
                    f.write(resp.read())
            except Exception as e:
                print(f"Failed to fetch {clean_url}: {e}, falling back to default")
                # Fallback
                req = urllib.request.Request(TOPIC_IMAGES['default'], headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as resp, open(cache_file, 'wb') as f:
                    f.write(resp.read())

        return Image.open(cache_file).convert("RGBA")
    elif os.path.exists(img_url_or_path):
        return Image.open(img_url_or_path).convert("RGBA")
    else:
        # fallback blank
        return Image.new("RGBA", (1080, 1350), (15, 23, 42, 255))

# -------------------------------------------------------------
# 1. Card-News Thumbnail Renderer (4:5 Ratio, 1080x1350)
# -------------------------------------------------------------
def render_cardnews_4_5(
    img_src: str,
    cache_id: str,
    badge_text: str,
    title_lines: list,
    point_text: str,
    sub_lines: list,
    badge_color: tuple,
    point_color: tuple,
    output_path: str
):
    W, H = 1080, 1350
    canvas = Image.new("RGBA", (W, H), (15, 23, 42, 255))

    # 1. Load Background & Cover Crop
    raw = download_or_load_image(img_src, cache_id)
    aspect = raw.width / raw.height
    target_h = H
    target_w = int(target_h * aspect)
    if target_w < W:
        target_w = W
        target_h = int(target_w / aspect)
    scaled = raw.resize((target_w, target_h), Image.Resampling.LANCZOS)
    left = (target_w - W) // 2
    top = (target_h - H) // 2
    cropped = scaled.crop((left, top, left + W, top + H))
    canvas.paste(cropped, (0, 0))

    # 2. Dark Vignette & Gradient Mask
    mask = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    m_draw = ImageDraw.Draw(mask)
    for y in range(H):
        if y < 240:
            a = 55
        elif y < 520:
            ratio = (y - 240) / 280.0
            a = int(55 + (185 - 55) * ratio)
        else:
            ratio = (y - 520) / (H - 520)
            a = int(185 + (248 - 185) * ratio)
        m_draw.line([(0, y), (W, y)], fill=(10, 15, 28, a))

    canvas = Image.alpha_composite(canvas, mask)
    draw = ImageDraw.Draw(canvas)

    # 3. Fonts
    font_brand = ImageFont.truetype(F_PRETEND, 26)
    font_badge = ImageFont.truetype(F_PRETEND, 34)
    # dynamically size title font based on length
    max_len = max(len(l) for l in title_lines) if title_lines else 6
    title_size = 112 if max_len <= 7 else (98 if max_len <= 10 else 86)
    font_title = ImageFont.truetype(F_BLACKHAN, title_size)
    font_point = ImageFont.truetype(F_PRETEND, 48)
    font_sub = ImageFont.truetype(F_PRETEND, 36)

    # 4. Top Brand Watermark
    draw.text((70, 70), "건강노트 HealthFit", fill=(255, 255, 255, 220), font=font_brand)

    # 5. Pill Badge
    badge_str = f" {badge_text} "
    bbox = draw.textbbox((0, 0), badge_str, font=font_badge)
    bw = bbox[2] - bbox[0] + 28
    bh = bbox[3] - bbox[1] + 16
    by = 380
    draw.rounded_rectangle((70, by, 70 + bw, by + bh), radius=12, fill=badge_color)
    draw.text((84, by + 8), badge_str, fill=(255, 255, 255), font=font_badge)

    # 6. Main Headline (1~2 Lines)
    ty = by + bh + 36
    line_height = int(title_size * 1.18)
    for line in title_lines[:2]:
        for ox, oy in [(-3,-3), (3,-3), (-3,3), (3,3), (0,4), (4,0)]:
            draw.text((70 + ox, ty + oy), line, font=font_title, fill=(0, 0, 0, 240))
        draw.text((70, ty), line, font=font_title, fill=(255, 255, 255))
        ty += line_height

    # 7. Point Bullet Copy
    py = ty + 16
    draw.text((72, py + 2), point_text, font=font_point, fill=(0, 0, 0, 220))
    draw.text((70, py), point_text, font=font_point, fill=point_color)

    # 8. Divider Line
    dy = py + 70
    draw.line([(70, dy), (70 + 480, dy)], fill=badge_color, width=4)

    # 9. Sub Lines
    sy = dy + 32
    if sub_lines:
        draw.text((70, sy), sub_lines[0], font=font_sub, fill=(226, 232, 240))
        if len(sub_lines) > 1:
            draw.text((70, sy + 48), sub_lines[1], font=font_sub, fill=(148, 163, 184))

    # 10. Outer Frame & Corners
    draw.rounded_rectangle((30, 30, W - 30, H - 30), radius=20, outline=(255, 255, 255, 45), width=2)

    # Contrast & Color Enhancement
    rgb = canvas.convert("RGB")
    rgb = ImageEnhance.Contrast(rgb).enhance(1.08)
    rgb = ImageEnhance.Color(rgb).enhance(1.05)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    rgb.save(output_path, "PNG", optimize=True)

# -------------------------------------------------------------
# 2. Horizontal Card Banner Renderer for index.html (16:9, 640x360)
# -------------------------------------------------------------
def render_tool_banner(
    img_src: str,
    cache_id: str,
    badge_text: str,
    title_text: str,
    sub_text: str,
    badge_color: tuple,
    output_path: str
):
    W, H = 640, 360
    canvas = Image.new("RGBA", (W, H), (15, 23, 42, 255))

    raw = download_or_load_image(img_src, cache_id)
    aspect = raw.width / raw.height
    target_h = H
    target_w = int(target_h * aspect)
    if target_w < W:
        target_w = W
        target_h = int(target_w / aspect)
    scaled = raw.resize((target_w, target_h), Image.Resampling.LANCZOS)
    left = (target_w - W) // 2
    top = (target_h - H) // 2
    cropped = scaled.crop((left, top, left + W, top + H))
    canvas.paste(cropped, (0, 0))

    # Dark gradient overlay from top to bottom
    mask = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    m_draw = ImageDraw.Draw(mask)
    for y in range(H):
        val = int(80 + (y / H) * 145)
        m_draw.line([(0, y), (W, y)], fill=(10, 15, 28, val))

    canvas = Image.alpha_composite(canvas, mask)
    draw = ImageDraw.Draw(canvas)

    font_b = ImageFont.truetype(F_PRETEND, 20)
    font_t = ImageFont.truetype(F_BLACKHAN, 40)
    font_s = ImageFont.truetype(F_PRETEND, 22)

    # Badge
    bbox = draw.textbbox((0, 0), badge_text, font=font_b)
    bw, bh = bbox[2] - bbox[0] + 20, bbox[3] - bbox[1] + 10
    by = 45
    draw.rounded_rectangle((40, by, 40 + bw, by + bh), radius=8, fill=badge_color)
    draw.text((50, by + 5), badge_text, fill=(255, 255, 255), font=font_b)

    # Title
    ty = by + bh + 22
    for ox, oy in [(-2,-2), (2,-2), (-2,2), (2,2), (0,2)]:
        draw.text((40 + ox, ty + oy), title_text, font=font_t, fill=(0, 0, 0, 240))
    draw.text((40, ty), title_text, font=font_t, fill=(255, 255, 255))

    # Sub
    sy = ty + 56
    draw.text((41, sy + 1), sub_text, font=font_s, fill=(0, 0, 0, 180))
    draw.text((40, sy), sub_text, font=font_s, fill=(226, 232, 240))

    # Subtle inner border
    draw.rounded_rectangle((12, 12, W - 12, H - 12), radius=12, outline=(255, 255, 255, 40), width=1)

    rgb = canvas.convert("RGB")
    rgb = ImageEnhance.Contrast(rgb).enhance(1.05)
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    rgb.save(output_path, "JPEG", quality=92, optimize=True)

# -------------------------------------------------------------
# 3. Complete Article & Tool Metadata Definitions
# -------------------------------------------------------------

# Theme color presets
BLUE = (2, 132, 199)       # #0284c7 Sky Blue
EMERALD = (16, 185, 129)   # #10b981 Mint/Emerald
AMBER = (217, 119, 6)      # #d97706 Warm Amber
ROSE = (225, 29, 72)       # #e11d48 Vivid Rose
PURPLE = (139, 92, 246)    # #8b5cf6 Violet
GOLD_YELLOW = (255, 225, 70)
SKY_ACCENT = (56, 189, 248)

ARTICLES_MAP = [
    {
        'slug': 'blood-pressure-stages-hypertension-diet',
        'badge': '혈관·혈압 관리',
        'titles': ['고혈압 전단계', '수치 기준 & 낮추는 법'],
        'point': '✓ 수축기 120~139 단계별 DASH 식단',
        'sub': ['칼륨 나트륨 배출 음식 & 3개월 관리법', '건강노트 순환기계 팩트체크'],
        'badge_color': ROSE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1080&q=80'
    },
    {
        'slug': 'blood-sugar-spike-prevention-diet',
        'badge': '혈당·대사 케어',
        'titles': ['식후 혈당 스파이크', '증상 & 거꾸로 식사법'],
        'point': '✓ 140mg/dL 급상승 예방 15분 걷기',
        'sub': ['식이섬유 우선 식사 순서와 인슐린 안정', '건강노트 대사 건강 가이드'],
        'badge_color': AMBER, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1505576399279-565b52d4ac71?w=1080&q=80'
    },
    {
        'slug': 'bmi-계산법',
        'badge': '체성분 정밀진단',
        'titles': ['BMI 계산법', '한국인 성인 비만 기준'],
        'point': '✓ 23부터 비만전단계 & 허리둘레 기준',
        'sub': ['키·체중 기반 체질량지수 4단계 분석', '건강노트 체형 진단 가이드'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1576678927484-cc907957088c?w=1080&q=80'
    },
    {
        'slug': 'body-fat-loss-calorie-deficit-calculator',
        'badge': '다이어트 팩트체크',
        'titles': ['체지방 1kg', '태우는 현실 공식'],
        'point': '✓ 하루 500kcal 적자의 과학적 진실',
        'sub': ['기초대사량(BMR) & 활동대사량(TDEE) 계산법', '체지방 연소와 근손실 방지 식단 가이드'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=1080&q=80'
    },
    {
        'slug': 'cholesterol-test-results-guide',
        'badge': '검진 수치 판독',
        'titles': ['콜레스테롤 검사표', '읽는 법 완벽 가이드'],
        'point': '✓ LDL · HDL · 중성지방 정상 수치',
        'sub': ['공복 채혈 기준과 비HDL 계산 공식', '건강노트 검진표 종합 판독'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=1080&q=80'
    },
    {
        'slug': 'fasting-cardio-fat-loss-timing',
        'badge': '운동 생리학',
        'titles': ['공복 유산소 vs 식후', '체지방 감량 효과 비교'],
        'point': '✓ 지방 연소 효율 & 근손실 방지 심박수',
        'sub': ['아침 공복과 식후 웨이트 최적 타이밍', '건강노트 운동 피트니스 가이드'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=1080&q=80'
    },
    {
        'slug': 'fatty-liver-foods-diet',
        'badge': '간 건강 케어',
        'titles': ['지방간 좋은 음식', '& 피해야 할 음식 기준'],
        'point': '✓ 액상과당 차단 & 지중해식 식단 가이드',
        'sub': ['비알코올성 지방간 식단과 체중 감량 원칙', '건강노트 내과 팩트체크'],
        'badge_color': AMBER, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=1080&q=80'
    },
    {
        'slug': 'iron-anemia-side-effects',
        'badge': '영양·빈혈 가이드',
        'titles': ['철분제 효능 & 복용법', '빈혈 증상과 부작용'],
        'point': '✓ 페리틴 검사 & 비타민C 병용 흡수율',
        'sub': ['위장장애·변비 줄이는 복용 타이밍', '건강노트 영양소 연구팀'],
        'badge_color': ROSE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=1080&q=80'
    },
    {
        'slug': 'ldl-cholesterol-diet-saturated-fat',
        'badge': '지질 대사 관리',
        'titles': ['LDL 콜레스테롤 식단', '달걀보다 포화지방 줄이기'],
        'point': '✓ 혈중 LDL을 올리는 진짜 주범 차단',
        'sub': ['가공육·버터 제한과 수용성 식이섬유 섭취', '건강노트 영양학 리서치'],
        'badge_color': ROSE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=1080&q=80'
    },
    {
        'slug': 'liver-enzymes-ast-alt-guide',
        'badge': '간수치 팩트체크',
        'titles': ['간수치 AST · ALT', '정상 범위 & 낮추는 법'],
        'point': '✓ 40 IU/L 기준 위험 신호 판독법',
        'sub': ['음주·약물·건강즙 부작용과 생활 회복법', '건강노트 검진 리포트'],
        'badge_color': AMBER, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=1080&q=80'
    },
    {
        'slug': 'lutein-benefits-evidence',
        'badge': '안과 영양 정보',
        'titles': ['루테인 효능 팩트', '10~20mg 권장 섭취량'],
        'point': '✓ 황반색소 밀도 유지 & 눈 피로 진실',
        'sub': ['식약처 인정 기능성과 AREDS2 임상 근거', '건강노트 눈 건강 가이드'],
        'badge_color': EMERALD, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1508847154043-be5407fcaa5a?w=1080&q=80'
    },
    {
        'slug': 'lutein-timing-with-meals',
        'badge': '영양제 복용법',
        'titles': ['루테인 복용시간', '식후 흡수율 2배 비결'],
        'point': '✓ 지용성 성분 식사 직후 섭취 원칙',
        'sub': ['공복 섭취 시 흡수율 저하와 상호작용', '건강노트 영양제 타이밍'],
        'badge_color': EMERALD, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1508847154043-be5407fcaa5a?w=1080&q=80'
    },
    {
        'slug': 'melatonin-overseas-purchase-korea',
        'badge': '의약품 규정 안내',
        'titles': ['멜라토닌 해외직구', '국내 통관 & 전문약 규정'],
        'point': '✓ 국내 전문의약품 분류와 반입 기준',
        'sub': ['통관 금지 성분 확인과 안전한 처방 가이드', '건강노트 약학 법령 정보'],
        'badge_color': PURPLE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1541480601022-2308c0f02487?w=1080&q=80'
    },
    {
        'slug': 'melatonin-timing-sleep-rhythm',
        'badge': '수면 생체리듬',
        'titles': ['멜라토닌 복용시간', '생체시계 맞춤 가이드'],
        'point': '✓ 취침 1~2시간 전 황금 타이밍',
        'sub': ['빛 노출 차단과 멜라토닌 분비 촉진 원리', '건강노트 수면 클리닉'],
        'badge_color': PURPLE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1541480601022-2308c0f02487?w=1080&q=80'
    },
    {
        'slug': 'sleep-foods-melatonin',
        'badge': '숙면 식단 솔루션',
        'titles': ['잠 잘 오는 음식', '멜라토닌 & 트립토판'],
        'point': '✓ 바나나·체리·따뜻한 우유의 과학',
        'sub': ['야식 피하고 뇌 수면 호르몬 깨우는 식단', '건강노트 숙면 큐레이션'],
        'badge_color': PURPLE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1541480601022-2308c0f02487?w=1080&q=80'
    },
    {
        'slug': 'tdee계산하는법',
        'badge': '다이어트 에너지',
        'titles': ['TDEE 계산법', '활동계수와 실전 칼로리'],
        'point': '✓ 내 일상에 딱 맞는 소비 칼로리 산출',
        'sub': ['주 3회 운동 vs 좌식 생활 활동량 보정법', '건강노트 칼로리 계산 공식'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=1080&q=80'
    },
    {
        'slug': 'vitamin-d-benefits-daily-intake-timing',
        'badge': '영양제 골든타임',
        'titles': ['비타민D 복용시간', '마그네슘 함께 먹는 이유'],
        'point': '✓ 흡수율 2배 높이는 점심 식후 복용',
        'sub': ['한국인 80% 결핍 기준 & 일일 2,000 IU', '건강노트 보충제 가이드'],
        'badge_color': EMERALD, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=1080&q=80'
    },
    {
        'slug': 'zinc-benefits-daily-intake',
        'badge': '면역·미네랄 케어',
        'titles': ['아연 효능 & 권장량', '공복 복용 주의사항'],
        'point': '✓ 성인 하루 8~10mg 최적 섭취선',
        'sub': ['속쓰림 없는 식후 섭취와 구리 상호작용', '건강노트 영양소 연구팀'],
        'badge_color': EMERALD, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=1080&q=80'
    },
    {
        'slug': '근육-유지와-다이어트를-위해-단백질-섭취의-중요성',
        'badge': '단백질 권장량',
        'titles': ['단백질 하루 섭취량', '체중 1kg당 몇 g일까?'],
        'point': '✓ 일반 성인 0.8g vs 운동인 1.6~2.0g',
        'sub': ['근육 합성 극대화 식사별 분할 섭취법', '건강노트 단백질 계산 공식'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1080&q=80'
    },
    {
        'slug': '기초대사량-계산법',
        'badge': '기초대사량 BMR',
        'titles': ['기초대사량 계산법', '남녀 평균보다 내 수치'],
        'point': '✓ 해리스-베네딕트 공식과 인바디 해석',
        'sub': ['굶는 다이어트가 기초대사량 망치는 이유', '건강노트 대사량 가이드'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=1080&q=80'
    },
    {
        'slug': '눈-뻑뻑함과-계단-어지러움-루테인과-철분제-낭비-없',
        'badge': '피로 자가진단',
        'titles': ['눈 뻑뻑함 & 어지러움', '루테인 · 철분 낭비 없는 법'],
        'point': '✓ 단순 피로와 결핍 증상 정확한 구분',
        'sub': ['인공눈물 바른 사용법과 페리틴 혈액 검사', '건강노트 생활 증상 케어'],
        'badge_color': EMERALD, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1508847154043-be5407fcaa5a?w=1080&q=80'
    },
    {
        'slug': '다이어트를-하는-분들이-매일-아침-오르는-체중계의',
        'badge': '복부비만 진단',
        'titles': ['허리둘레 재는 법', '남 90cm · 여 85cm 기준'],
        'point': '✓ 갈비뼈 아래와 골반 위 정중앙 측정',
        'sub': ['바지 인치와 다른 진짜 내장지방 기준', '건강노트 체형 진단'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1535914254981-b5012eebbd15?w=1080&q=80'
    },
    {
        'slug': '마그네슘-하루-권장량',
        'badge': '신경·근육 미네랄',
        'titles': ['마그네슘 권장량', '복용시간 & 상한 부작용'],
        'point': '✓ 킬레이트·산화 마그네슘 흡수율 차이',
        'sub': ['저녁 복용과 숙면, 설사 없는 상한선 350mg', '건강노트 보충제 분석'],
        'badge_color': EMERALD, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1498557850523-fd3d118b962e?w=1080&q=80'
    },
    {
        'slug': '멀티비타민-언제-먹어야-효과-좋을까',
        'badge': '종합영양제 팁',
        'titles': ['멀티비타민 복용시간', '아침 vs 저녁 언제 먹을까?'],
        'point': '✓ 수용성 B군 활력 아침 식후 추천',
        'sub': ['위장장애 없는 식사 직후 복용 원칙', '건강노트 영양제 복용 가이드'],
        'badge_color': EMERALD, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1516997121675-4c2d1684aa3e?w=1080&q=80'
    },
    {
        'slug': '생리주기-계산법',
        'badge': '여성 헬스케어',
        'titles': ['배란일 계산법 & 가임기', '생리주기 오차 잡는 법'],
        'point': '✓ 다음 생리 예정일 기준 14일 전 공식',
        'sub': ['불규칙 주기 보정과 기초체온 관찰법', '건강노트 여성 주기 가이드'],
        'badge_color': ROSE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?w=1080&q=80'
    },
    {
        'slug': '서브웨이-칼로리',
        'badge': '다이어트 외식',
        'titles': ['서브웨이 칼로리', '빵 · 소스 다이어트 조합'],
        'point': '✓ 위트 빵 + 로스트치킨 + 올리브오일',
        'sub': ['소스 하나로 200kcal 차이나는 칼로리표', '건강노트 식단 큐레이션'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1509722747041-616f39b57569?w=1080&q=80'
    },
    {
        'slug': '소주-주량-계산',
        'badge': '숙취 해독 과학',
        'titles': ['술 깨는 시간 계산', '위드마크 공식과 간 해독'],
        'point': '✓ 소주 1병 완전 분해 4~6시간 소요',
        'sub': ['커피·사우나로 빨라지지 않는 알코올 대사', '건강노트 숙취 해소 가이드'],
        'badge_color': AMBER, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1080&q=80'
    },
    {
        'slug': '스타벅스-칼로리',
        'badge': '카페 음료 분석',
        'titles': ['스타벅스 칼로리', '다이어트 저당 음료 순서'],
        'point': '✓ 아메리카노 10kcal vs 프라푸치노 400kcal',
        'sub': ['시럽 펌프당 당류와 라이트 밀크 옵션', '건강노트 음료 칼로리표'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1080&q=80'
    },
    {
        'slug': '여자-적정-체중',
        'badge': '건강 체중 기준',
        'titles': ['여자 적정 체중', '미용 체중보다 건강 범위'],
        'point': '✓ BMI 18.5~22.9 한국 성인 표준 지표',
        'sub': ['체지방률과 근육량을 함께 보는 건강 지수', '건강노트 체중 가이드'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=1080&q=80'
    },
    {
        'slug': '영양제-상한섭취량',
        'badge': '영양제 안전성',
        'titles': ['영양제 상한섭취량', '중복 복용 전 확인할 숫자'],
        'point': '✓ 비타민A · 아연 · 셀레늄 과다 경고',
        'sub': ['종합비타민 + 단일제 합산 계산 원칙', '건강노트 영양제 안전 체크'],
        'badge_color': ROSE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1587854680352-936b22b91030?w=1080&q=80'
    },
    {
        'slug': '오메가3',
        'badge': '혈행·오메가3',
        'titles': ['오메가3 고르는 법', 'rTG vs 순도 팩트체크'],
        'point': '✓ EPA + DHA 순수 합 1,000mg 확인법',
        'sub': ['산패도(IFOS)와 식후 복용으로 흡수율 극대화', '건강노트 보충제 연구팀'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1519682577862-22b62b24e493?w=1080&q=80'
    },
    {
        'slug': '와인칼로리',
        'badge': '알코올 열량',
        'titles': ['와인 칼로리 계산', '당도보다 알코올 도수!'],
        'point': '✓ 레드와인 1잔(150mL) 125kcal의 진실',
        'sub': ['달지 않아도 도수 높으면 칼로리 폭탄', '건강노트 주류 열량 분석'],
        'badge_color': ROSE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=1080&q=80'
    },
    {
        'slug': '운동-소모-칼로리-계산',
        'badge': '소비 칼로리 MET',
        'titles': ['운동 소모 칼로리', 'MET 공식 & 스마트워치 오차'],
        'point': '✓ 걷기 · 러닝 · 수영 종목별 정확한 계산',
        'sub': ['체중과 시간 반영한 신체활동 에너지 소비량', '건강노트 운동역학 계산'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1080&q=80'
    },
    {
        'slug': '임산부-엽산-권장량',
        'badge': '임신 영양 관리',
        'titles': ['임산부 엽산 권장량', '400μg vs 620μg DFE'],
        'point': '✓ 임신 전 3개월부터 태아 신경관 결손 예방',
        'sub': ['활성형 엽산(5-MTHF) 선택 기준 안내', '건강노트 임신 건강 가이드'],
        'badge_color': ROSE, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1476703993599-0035a21b17a9?w=1080&q=80'
    },
    {
        'slug': '임산부-체중증가',
        'badge': '임신 체중 기준',
        'titles': ['임신 체중 증가 범위', '임신 전 BMI별 권장량'],
        'point': '✓ 정상 체중 기준 11.5~16kg 건강 증가',
        'sub': ['임신성 당뇨와 고혈압 예방 주수별 체중 관리', '건강노트 모자보건 가이드'],
        'badge_color': ROSE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1491013516836-7db643ee125a?w=1080&q=80'
    },
    {
        'slug': '칼슘-하루-권장-섭취량',
        'badge': '골밀도·칼슘 케어',
        'titles': ['칼슘 하루 권장량', '500mg 분할 & 복용법'],
        'point': '✓ 1회 500mg 이하 분할 흡수율 극대화',
        'sub': ['비타민D·마그네슘 상호작용과 위장 편한 성분', '건강노트 뼈 건강 연구팀'],
        'badge_color': EMERALD, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1563636619-e9143da7973b?w=1080&q=80'
    },
    {
        'slug': '하루-물-섭취량',
        'badge': '수분 밸런스',
        'titles': ['하루 물 섭취량', '2리터가 정답이 아닌 이유'],
        'point': '✓ 체중 × 30~35mL 내 몸 맞춤 수분량',
        'sub': ['식사 수분 포함과 과다 수분중독 예방법', '건강노트 수분 건강 가이드'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=1080&q=80'
    },
    {
        'slug': '하루-카페인-권장량',
        'badge': '카페인 안전 가이드',
        'titles': ['하루 카페인 권장량', '성인 400mg 안전 한도'],
        'point': '✓ 커피 3~4잔 기준 임산부·청소년 한도',
        'sub': ['심장 두근거림 없는 섭취 시간과 배출 시간', '건강노트 카페인 분석'],
        'badge_color': AMBER, 'point_color': GOLD_YELLOW,
        'img': 'https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=1080&q=80'
    },
    {
        'slug': '헬스장-트레이너나',
        'badge': '영양소 황금비율',
        'titles': ['탄단지 비율 계산법', '2025 한국인 영양 기준'],
        'point': '✓ 탄수화물 5: 단백질 3: 지방 2 최적화',
        'sub': ['다이어트 감량기와 유지기 맞춤 영양 설계', '건강노트 영양학 가이드'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1080&q=80'
    }
]

TOOLS_MAP = [
    {
        'id': 'routine',
        'file': 'routine.html',
        'badge': '시그니처 플래너',
        'titles': ['영양제 시간표', '& 상극 궁합 플래너'],
        'point': '✓ 4단계 복용 타이밍 & 충돌 자동 분석',
        'sub': ['먹는 영양제 1초 맞춤 시간표 처방', '건강노트 1:1 스마트 솔루션'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': TOPIC_IMAGES['vitamins']
    },
    {
        'id': 'checkup',
        'file': 'checkup.html',
        'badge': '검진 종합 판독',
        'titles': ['건강검진 수치', '신호등 판독 리포트'],
        'point': '✓ 혈압 · 혈당 · 간수치 · 콜레스테롤',
        'sub': ['정상 · 주의 · 위험 신호등 즉시 판독', '한국인 표준 검진 해석 가이드'],
        'badge_color': AMBER, 'point_color': GOLD_YELLOW,
        'img': TOPIC_IMAGES['medical']
    },
    {
        'id': 'quiz',
        'file': 'quiz.html',
        'badge': '셀프 케어 진단',
        'titles': ['30초 맞춤 건강', '생활습관 자가진단'],
        'point': '✓ 내 몸 1순위 케어 솔루션 처방',
        'sub': ['영양 · 수면 · 활력 4문항 간편 체크', '개인 맞춤 건강 처방전'],
        'badge_color': PURPLE, 'point_color': SKY_ACCENT,
        'img': TOPIC_IMAGES['default']
    },
    {
        'id': 'bmi',
        'file': 'bmi.html',
        'badge': '체성분 정밀 진단',
        'titles': ['BMI 비만도 계산기', '& 한국인 표준체중'],
        'point': '✓ 아시아 비만학회 기준 비만 4단계',
        'sub': ['키 · 체중 기반 최적 적정 체중 산출', '건강 체형 관리 솔루션'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': TOPIC_IMAGES['weight']
    },
    {
        'id': 'calorie',
        'file': 'calorie.html',
        'badge': '다이어트 계산기',
        'titles': ['하루 칼로리 계산기', '기초대사량 & TDEE'],
        'point': '✓ 감량 · 유지 · 증량 목표 칼로리',
        'sub': ['미플린-지어 공식 기반 정밀 대사량 산출', '체계적인 일일 섭취 목표 가이드'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': TOPIC_IMAGES['diet']
    },
    {
        'id': 'protein',
        'file': 'protein.html',
        'badge': '영양 섭취 계산',
        'titles': ['하루 단백질 권장량', '목표별 정밀 계산기'],
        'point': '✓ 체중 1kg당 최적 단백질(g) 산출',
        'sub': ['근육 합성 & 체중 감량 맞춤 권장량', '식품별 단백질 환산 안내'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': TOPIC_IMAGES['protein']
    },
    {
        'id': 'exercise',
        'file': 'exercise.html',
        'badge': '운동 소모 계산',
        'titles': ['운동별 소모 칼로리', 'METs 정밀 계산기'],
        'point': '✓ 걷기 · 러닝 · 수영 · 웨이트 소비량',
        'sub': ['체중과 운동 시간 기반 소비 칼로리', '체지방 연소 시간 가이드'],
        'badge_color': BLUE, 'point_color': GOLD_YELLOW,
        'img': TOPIC_IMAGES['workout']
    },
    {
        'id': 'water',
        'file': 'water.html',
        'badge': '수분 건강 계산',
        'titles': ['하루 물 권장 섭취량', '& 잔 수 맞춤 계산기'],
        'point': '✓ 체중 × 30~35mL 최적 수분량',
        'sub': ['운동량 반영 일일 수분 권장량 산출', '수분 부족 예방 가이드'],
        'badge_color': BLUE, 'point_color': SKY_ACCENT,
        'img': TOPIC_IMAGES['water']
    },
    {
        'id': 'caffeine',
        'file': 'caffeine.html',
        'badge': '카페인 안전 한도',
        'titles': ['하루 카페인 안전량', '& 커피 음료 계산기'],
        'point': '✓ 성인 400mg 대비 섭취율 측정',
        'sub': ['커피 · 에너지음료 속 카페인 총량', '부작용 없는 일일 안전선'],
        'badge_color': AMBER, 'point_color': GOLD_YELLOW,
        'img': TOPIC_IMAGES['coffee']
    },
    {
        'id': 'alcohol',
        'file': 'alcohol.html',
        'badge': '간 건강 계산',
        'titles': ['알코올 분해시간', '위드마크 숙취 계산기'],
        'point': '✓ 소주 · 맥주 완전 해독 소요 시간',
        'sub': ['체중과 음주량 기반 알코올 분해 추정', '숙취 예방 및 음주 가이드'],
        'badge_color': AMBER, 'point_color': SKY_ACCENT,
        'img': TOPIC_IMAGES['alcohol']
    },
    {
        'id': 'supplement',
        'file': 'supplement.html',
        'badge': '영양제 안전 분석',
        'titles': ['영양제 상한 섭취량', '& 과다복용 체크기'],
        'point': '✓ 비타민 · 미네랄 중복 복용 위험 차단',
        'sub': ['식약처 1일 권장량 및 상한선 조회', '안전한 성분 배합 체크'],
        'badge_color': EMERALD, 'point_color': GOLD_YELLOW,
        'img': TOPIC_IMAGES['vitamins']
    }
]

# -------------------------------------------------------------
# 4. Helper for Updating OpenGraph tags
# -------------------------------------------------------------
def inject_og_image(file_path: str, og_url: str):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'property="og:image"' in content or 'property=\'og:image\'' in content:
        content = re.sub(
            r'<meta\s+property=[\'"]og:image[\'"][^>]*>',
            f'<meta property="og:image" content="{og_url}" />',
            content
        )
    else:
        og_tag = f'\n  <meta property="og:image" content="{og_url}" />\n  <meta name="twitter:card" content="summary_large_image" />\n  <meta name="twitter:image" content="{og_url}" />'
        if '<meta property="og:type"' in content:
            content = re.sub(r'(<meta property="og:type"[^>]*>)', r'\1' + og_tag, content, count=1)
        elif '<head>' in content:
            content = content.replace('<head>', '<head>' + og_tag, 1)
        elif '<head ' in content:
            content = re.sub(r'(<head[^>]*>)', r'\1' + og_tag, content, count=1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# -------------------------------------------------------------
# 5. Main Execution
# -------------------------------------------------------------
def run():
    print("=== 1. Generating Article Card-News Thumbnails (4:5) ===")
    for item in ARTICLES_MAP:
        slug = item['slug']
        article_dir = os.path.join("health", slug)
        out_path = os.path.join(article_dir, "thumbnail.png")
        print(f"Generating article thumb: {slug}...")
        render_cardnews_4_5(
            img_src=item['img'],
            cache_id=slug,
            badge_text=item['badge'],
            title_lines=item['titles'],
            point_text=item['point'],
            sub_lines=item['sub'],
            badge_color=item['badge_color'],
            point_color=item['point_color'],
            output_path=out_path
        )
        html_path = os.path.join(article_dir, "index.html")
        inject_og_image(html_path, f"https://healthfit100.com/health/{slug}/thumbnail.png")

    print("\n=== 2. Generating Tool Thumbnails (4:5 Card-News & 16:9 Banner) ===")
    for tool in TOOLS_MAP:
        tid = tool['id']
        tfile = tool['file']
        card_out = f"images/thumbnails/tool_{tid}.png"
        banner_out = f"images/thumbnails/banner_{tid}.jpg"

        print(f"Generating tool thumbs: {tid}...")
        # 4:5 Card-news for OpenGraph & Pinterest / Threads
        render_cardnews_4_5(
            img_src=tool['img'],
            cache_id=f"tool_{tid}",
            badge_text=tool['badge'],
            title_lines=tool['titles'],
            point_text=tool['point'],
            sub_lines=tool['sub'],
            badge_color=tool['badge_color'],
            point_color=tool['point_color'],
            output_path=card_out
        )

        # 16:9 Banner for index.html card header
        render_tool_banner(
            img_src=tool['img'],
            cache_id=f"tool_{tid}",
            badge_text=tool['badge'],
            title_text=" ".join(tool['titles']),
            sub_text=tool['point'],
            badge_color=tool['badge_color'],
            output_path=banner_out
        )

        # Inject OG into tool html
        inject_og_image(tfile, f"https://healthfit100.com/{card_out}")

    # Generate default site OG
    print("Generating default site OG...")
    render_cardnews_4_5(
        img_src=TOPIC_IMAGES['default'],
        cache_id="og_default",
        badge_text="스마트 헬스케어",
        title_lines=["건강노트 HealthFit", "전문 건강정보 & 도구"],
        point_text="✓ 11종 무료 건강 분석 & 의학 팩트체크",
        sub_lines=["근거 기반 건강 블로그 & 1:1 맞춤 계산기", "healthfit100.com"],
        badge_color=BLUE,
        point_color=GOLD_YELLOW,
        output_path="images/thumbnails/og_default.png"
    )
    inject_og_image("index.html", "https://healthfit100.com/images/thumbnails/og_default.png")

    print("\nAll thumbnails generated and OG images updated successfully!")

if __name__ == '__main__':
    run()

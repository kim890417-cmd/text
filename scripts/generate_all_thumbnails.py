import os
import glob
import re
from PIL import Image, ImageDraw, ImageFont

def create_gradient(width, height, start_color, end_color):
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_rounded_rect(draw, coords, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(coords, radius=radius, fill=fill, outline=outline, width=width)

THEMES = {
    'blue': {
        'bg_start': (15, 23, 42),
        'bg_end': (30, 58, 138),
        'accent': (56, 189, 248),
        'badge_bg': (14, 116, 144),
        'badge_fg': (224, 242, 254),
    },
    'emerald': {
        'bg_start': (15, 23, 42),
        'bg_end': (6, 78, 59),
        'accent': (52, 211, 153),
        'badge_bg': (4, 120, 87),
        'badge_fg': (209, 250, 229),
    },
    'teal': {
        'bg_start': (15, 23, 42),
        'bg_end': (19, 78, 74),
        'accent': (45, 212, 191),
        'badge_bg': (15, 118, 110),
        'badge_fg': (204, 251, 241),
    },
    'indigo': {
        'bg_start': (15, 23, 42),
        'bg_end': (49, 46, 129),
        'accent': (129, 140, 248),
        'badge_bg': (67, 56, 202),
        'badge_fg': (224, 231, 255),
    },
    'violet': {
        'bg_start': (15, 23, 42),
        'bg_end': (76, 29, 149),
        'accent': (192, 132, 252),
        'badge_bg': (109, 40, 217),
        'badge_fg': (243, 232, 255),
    }
}

def generate_thumbnail(title: str, subtitle: str, category: str, output_path: str, theme: str = 'blue'):
    width, height = 1200, 630
    t = THEMES.get(theme, THEMES['blue'])

    img = create_gradient(width, height, t['bg_start'], t['bg_end'])
    draw = ImageDraw.Draw(img)

    # Outer border
    draw_rounded_rect(draw, (30, 30, width - 30, height - 30), radius=24, outline=(255, 255, 255, 40), width=2)
    # Inner card
    draw_rounded_rect(draw, (50, 50, width - 50, height - 50), radius=20, fill=(15, 23, 42, 180), outline=(255, 255, 255, 20), width=1)
    # Accent top bar
    draw_rounded_rect(draw, (75, 52, 220, 56), radius=2, fill=t['accent'])

    font_brand = ImageFont.truetype(r'C:\Windows\Fonts\malgunbd.ttf', 20)
    font_cat = ImageFont.truetype(r'C:\Windows\Fonts\malgunbd.ttf', 22)
    font_title = ImageFont.truetype(r'C:\Windows\Fonts\malgunbd.ttf', 44)
    font_sub = ImageFont.truetype(r'C:\Windows\Fonts\malgun.ttf', 24)
    font_footer = ImageFont.truetype(r'C:\Windows\Fonts\malgun.ttf', 18)

    # Top Brand
    draw.text((75, 80), "건강노트", fill=(255, 255, 255), font=font_brand)
    draw.text((165, 82), "HealthFit", fill=t['accent'], font=font_brand)

    # Category Pill
    cat_text = f"  {category}  "
    cat_bbox = draw.textbbox((0, 0), cat_text, font=font_cat)
    cat_w = cat_bbox[2] - cat_bbox[0]
    cat_x = width - 75 - cat_w - 20
    draw_rounded_rect(draw, (cat_x, 74, cat_x + cat_w + 20, 114), radius=12, fill=t['badge_bg'])
    draw.text((cat_x + 10, 80), cat_text, fill=t['badge_fg'], font=font_cat)

    draw.line((75, 130, width - 75, 130), fill=(255, 255, 255, 30), width=1)

    # Clean title
    clean_title = title.split('|')[0].strip()
    words = clean_title.split()
    lines = []
    curr_line = ""
    for w in words:
        test = f"{curr_line} {w}".strip()
        bbox = draw.textbbox((0, 0), test, font=font_title)
        if bbox[2] - bbox[0] > (width - 160):
            if curr_line:
                lines.append(curr_line)
            curr_line = w
        else:
            curr_line = test
    if curr_line:
        lines.append(curr_line)

    if len(lines) > 2:
        lines = lines[:2]
        if not lines[1].endswith('...'):
            lines[1] += '...'

    title_y = 175
    for line in lines:
        draw.text((75, title_y), line, fill=(255, 255, 255), font=font_title)
        title_y += 62

    # Clean subtitle
    clean_sub = subtitle.split('.')[0].strip() if subtitle else ""
    if len(clean_sub) > 75:
        clean_sub = clean_sub[:72] + "..."
    sub_words = clean_sub.split()
    sub_lines = []
    curr_sub = ""
    for w in sub_words:
        test = f"{curr_sub} {w}".strip()
        bbox = draw.textbbox((0, 0), test, font=font_sub)
        if bbox[2] - bbox[0] > (width - 160):
            if curr_sub:
                sub_lines.append(curr_sub)
            curr_sub = w
        else:
            curr_sub = test
    if curr_sub:
        sub_lines.append(curr_sub)

    sub_y = max(title_y + 20, 360)
    for sline in sub_lines[:2]:
        draw.text((75, sub_y), sline, fill=(203, 213, 225), font=font_sub)
        sub_y += 36

    # Footer
    footer_y = height - 95
    draw.line((75, footer_y - 15, width - 75, footer_y - 15), fill=(255, 255, 255, 30), width=1)
    draw.text((75, footer_y), "✓ 의학·생리학 근거 기반 가이드", fill=t['accent'], font=font_footer)
    draw.text((360, footer_y), "✓ 맞춤 분석 & 무료 도구", fill=(148, 163, 184), font=font_footer)
    draw.text((width - 75 - 160, footer_y), "healthfit100.com", fill=(148, 163, 184), font=font_footer)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    img.save(output_path, "PNG", optimize=True)

def inject_og_image(file_path: str, og_url: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if og:image exists
    if 'property="og:image"' in content or 'property=\'og:image\'' in content:
        # replace
        content = re.sub(
            r'<meta\s+property=[\'"]og:image[\'"][^>]*>',
            f'<meta property="og:image" content="{og_url}" />',
            content
        )
    else:
        # inject after og:type or <head>
        og_tag = f'\n  <meta property="og:image" content="{og_url}" />\n  <meta name="twitter:card" content="summary_large_image" />\n  <meta name="twitter:image" content="{og_url}" />'
        if '<meta property="og:type"' in content:
            content = re.sub(r'(<meta property="og:type"[^>]*>)', r'\1' + og_tag, content, count=1)
        elif '<head>' in content:
            content = content.replace('<head>', '<head>' + og_tag, 1)
        elif '<head ' in content:
            content = re.sub(r'(<head[^>]*>)', r'\1' + og_tag, content, count=1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def process_tools():
    tools = [
        ('routine.html', '내 영양제 복용 시간표 & 상극 궁합 플래너', '영양제 복용 시간표와 흡수를 방해하는 상극 조합을 1초 만에 분석', '시그니처 플래너', 'teal', 'images/thumbnails/tool_routine.png'),
        ('calorie.html', '하루 칼로리 계산기 | 기초대사량(BMR) & 필요 칼로리(TDEE)', '기초대사량과 활동대사량, 체중 감량 목표 맞춤 칼로리 무료 계산', '다이어트 계산기', 'indigo', 'images/thumbnails/tool_calorie.png'),
        ('protein.html', '하루 단백질 권장 섭취량 계산기', '체중과 운동 강도에 따른 근육 유지 및 다이어트 단백질 권장량', '영양 섭취 계산기', 'emerald', 'images/thumbnails/tool_protein.png'),
        ('bmi.html', 'BMI 비만도 계산기 | 체질량지수 분석', '한국인 기준 비만도 단계와 건강 체중 범위를 즉시 확인', '건강 진단 계산기', 'blue', 'images/thumbnails/tool_bmi.png'),
        ('exercise.html', '운동별 소모 칼로리 계산기', '체중과 운동 종목, 운동 시간에 따른 정확한 에너지 소모량 계산', '운동 소모 계산기', 'violet', 'images/thumbnails/tool_exercise.png'),
        ('water.html', '하루 물 권장 섭취량 계산기', '체중과 활동량 기준 수분 부족 예방을 위한 하루 최적 섭취량', '수분 건강 계산기', 'teal', 'images/thumbnails/tool_water.png'),
        ('caffeine.html', '하루 카페인 권장량 & 안전 섭취 계산기', '커피, 에너지음료 속 카페인 함량과 부작용 없는 일일 안전 한도', '영양 섭취 가이드', 'blue', 'images/thumbnails/tool_caffeine.png'),
        ('alcohol.html', '소주·맥주 주량 및 숙취 알코올 분해 계산기', '체중과 음주량에 따른 체내 알코올 분해 소요 시간 및 간 건강 분석', '생활 건강 계산기', 'indigo', 'images/thumbnails/tool_alcohol.png'),
        ('supplement.html', '영양제 상한 섭취량 및 과다복용 체크', '비타민과 미네랄 성분 중복 및 상한선 초과 위험을 예방하는 안전 체크', '영양제 안전 분석', 'emerald', 'images/thumbnails/tool_supplement.png'),
        ('checkup.html', '건강검진 수치 정상 범위 & 판독 가이드', '혈압, 공복혈당, 간수치(AST·ALT), 콜레스테롤 정상 기준 종합 안내', '검진 수치 가이드', 'blue', 'images/thumbnails/tool_checkup.png'),
        ('quiz.html', '건강 상식 퀴즈 & 나의 생활습관 자가진단', '잘못 알고 있던 영양·수면·운동 상식을 바로잡는 인터랙티브 퀴즈', '건강 자가 진단', 'violet', 'images/thumbnails/tool_quiz.png'),
        ('index.html', '건강노트 | 영양제·식단·건강 정보와 무료 건강 계산기', '직접 검증한 건강 정보와 11종 무료 건강 계산기를 한곳에서', '스마트 헬스케어', 'teal', 'images/thumbnails/og_default.png'),
    ]

    for fname, title, sub, cat, theme, outpath in tools:
        if os.path.exists(fname):
            generate_thumbnail(title, sub, cat, outpath, theme)
            og_url = f"https://healthfit100.com/{outpath}"
            inject_og_image(fname, og_url)
            print(f"Tool {fname} -> {og_url}")

def process_articles():
    article_files = glob.glob('health/*/index.html')
    print(f"\nProcessing {len(article_files)} articles...")

    for afile in article_files:
        with open(afile, 'r', encoding='utf-8') as f:
            content = f.read()

        folder = os.path.dirname(afile)
        thumb_path = os.path.join(folder, 'thumbnail.png')

        # extract title
        tm = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = tm.group(1).split('|')[0].strip() if tm else "건강 칼럼 가이드"

        # extract description
        dm = re.search(r'<meta\s+name=[\'"]description[\'"]\s+content=[\'"](.*?)[\'"]', content, re.IGNORECASE)
        sub = dm.group(1) if dm else ""

        # pick theme & category based on title
        if any(k in title for k in ['칼로리', '체지방', '다이어트', '유산소', '운동', 'TDEE', '기초대사량', '체중']):
            theme = 'indigo'
            category = '다이어트·운동'
        elif any(k in title for k in ['비타민', '오메가', '마그네슘', '루테인', '철분', '영양제', '엽산', '칼슘', '아연']):
            theme = 'emerald'
            category = '영양·보충제'
        elif any(k in title for k in ['혈압', '혈당', '간수치', '콜레스테롤', '지방간', '수면', '멜라토닌']):
            theme = 'teal'
            category = '질환·검진'
        else:
            theme = 'blue'
            category = '건강 매거진'

        generate_thumbnail(title, sub, category, thumb_path, theme)
        og_url = f"https://healthfit100.com/{thumb_path.replace(os.sep, '/')}"
        inject_og_image(afile, og_url)

if __name__ == '__main__':
    process_tools()
    process_articles()
    print("\nAll thumbnails generated and OG images injected successfully!")

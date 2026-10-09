import os
from PIL import Image, ImageDraw, ImageFont

def create_gradient(width, height, start_color, end_color):
    """Creates a vertical gradient image."""
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

def generate_thumbnail(
    title: str,
    subtitle: str,
    category: str,
    output_path: str,
    theme: str = 'blue'
):
    width, height = 1200, 630

    # Color themes
    themes = {
        'blue': {
            'bg_start': (15, 23, 42),      # slate-900
            'bg_end': (30, 58, 138),       # blue-900
            'accent': (56, 189, 248),      # sky-400
            'badge_bg': (14, 116, 144),    # cyan-700
            'badge_fg': (224, 242, 254),   # sky-100
        },
        'emerald': {
            'bg_start': (15, 23, 42),
            'bg_end': (6, 78, 59),         # emerald-900
            'accent': (52, 211, 153),      # emerald-400
            'badge_bg': (4, 120, 87),      # emerald-700
            'badge_fg': (209, 250, 229),   # emerald-100
        },
        'teal': {
            'bg_start': (15, 23, 42),
            'bg_end': (19, 78, 74),        # teal-900
            'accent': (45, 212, 191),      # teal-400
            'badge_bg': (15, 118, 110),    # teal-700
            'badge_fg': (204, 251, 241),   # teal-100
        },
        'indigo': {
            'bg_start': (15, 23, 42),
            'bg_end': (49, 46, 129),       # indigo-900
            'accent': (129, 140, 248),     # indigo-400
            'badge_bg': (67, 56, 202),     # indigo-700
            'badge_fg': (224, 231, 255),   # indigo-100
        }
    }
    t = themes.get(theme, themes['blue'])

    # 1. Base Gradient
    img = create_gradient(width, height, t['bg_start'], t['bg_end'])
    draw = ImageDraw.Draw(img)

    # 2. Outer decorative border
    draw_rounded_rect(draw, (30, 30, width - 30, height - 30), radius=24, outline=(255, 255, 255, 40), width=2)

    # 3. Inner card surface
    inner_coords = (50, 50, width - 50, height - 50)
    # subtle glow on inner card
    draw_rounded_rect(draw, inner_coords, radius=20, fill=(15, 23, 42, 180), outline=(255, 255, 255, 20), width=1)

    # Accent decorative top bar
    draw_rounded_rect(draw, (75, 52, 220, 56), radius=2, fill=t['accent'])

    # Fonts
    font_brand = ImageFont.truetype(r'C:\Windows\Fonts\malgunbd.ttf', 20)
    font_cat = ImageFont.truetype(r'C:\Windows\Fonts\malgunbd.ttf', 22)
    font_title = ImageFont.truetype(r'C:\Windows\Fonts\malgunbd.ttf', 48)
    font_sub = ImageFont.truetype(r'C:\Windows\Fonts\malgun.ttf', 26)
    font_footer = ImageFont.truetype(r'C:\Windows\Fonts\malgun.ttf', 18)

    # 4. Top Badges
    # Brand: 건강노트 HealthFit
    draw.text((75, 80), "건강노트", fill=(255, 255, 255), font=font_brand)
    draw.text((165, 82), "HealthFit", fill=t['accent'], font=font_brand)

    # Category Pill
    cat_text = f"  {category}  "
    cat_bbox = draw.textbbox((0, 0), cat_text, font=font_cat)
    cat_w = cat_bbox[2] - cat_bbox[0]
    cat_x = width - 75 - cat_w - 20
    draw_rounded_rect(draw, (cat_x, 74, cat_x + cat_w + 20, 114), radius=12, fill=t['badge_bg'])
    draw.text((cat_x + 10, 80), cat_text, fill=t['badge_fg'], font=font_cat)

    # Divider line
    draw.line((75, 130, width - 75, 130), fill=(255, 255, 255, 30), width=1)

    # 5. Title Wrapping
    # Wrap title if long
    words = title.split()
    lines = []
    curr_line = ""
    for w in words:
        test_line = f"{curr_line} {w}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=font_title)
        if bbox[2] - bbox[0] > (width - 160):
            if curr_line:
                lines.append(curr_line)
            curr_line = w
        else:
            curr_line = test_line
    if curr_line:
        lines.append(curr_line)

    if len(lines) > 3:
        lines = lines[:2] + [lines[2] + "..."]

    # Draw Title
    title_y = 175
    line_spacing = 64
    for line in lines:
        draw.text((75, title_y), line, fill=(255, 255, 255), font=font_title)
        title_y += line_spacing

    # 6. Subtitle
    sub_y = max(title_y + 20, 370)
    sub_words = subtitle.split()
    sub_lines = []
    curr_sub = ""
    for w in sub_words:
        test_line = f"{curr_sub} {w}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=font_sub)
        if bbox[2] - bbox[0] > (width - 160):
            if curr_sub:
                sub_lines.append(curr_sub)
            curr_sub = w
        else:
            curr_sub = test_line
    if curr_sub:
        sub_lines.append(curr_sub)

    for sline in sub_lines[:2]:
        draw.text((75, sub_y), sline, fill=(203, 213, 225), font=font_sub)
        sub_y += 38

    # 7. Bottom Bar & Features
    footer_y = height - 95
    draw.line((75, footer_y - 15, width - 75, footer_y - 15), fill=(255, 255, 255, 30), width=1)

    # Feature checkmark
    draw.text((75, footer_y), "✓ 전문 건강 데이터 기반", fill=t['accent'], font=font_footer)
    draw.text((320, footer_y), "✓ 무료 즉시 분석 도구", fill=(148, 163, 184), font=font_footer)

    # Domain
    domain_text = "healthfit100.com"
    draw.text((width - 75 - 160, footer_y), domain_text, fill=(148, 163, 184), font=font_footer)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    # Test routine
    generate_thumbnail(
        title="내 영양제 복용 시간표 & 상극 궁합 플래너",
        subtitle="내가 먹는 영양제 선택 시 최적의 복용 시간과 흡수를 방해하는 상극 조합을 1초 만에 분석",
        category="시그니처 플래너",
        output_path="images/thumbnails/tool_routine.png",
        theme="teal"
    )

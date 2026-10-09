import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_DIR = r"C:\Users\sadase\Desktop\블로그 설정\fonts"
F_BLACKHAN = os.path.join(FONT_DIR, "BlackHanSans-Regular.ttf")
F_PRETEND = os.path.join(FONT_DIR, "Pretendard-Bold.ttf")

if not os.path.exists(F_BLACKHAN):
    F_BLACKHAN = r"C:\Windows\Fonts\malgunbd.ttf"
if not os.path.exists(F_PRETEND):
    F_PRETEND = r"C:\Windows\Fonts\malgunbd.ttf"

def draw_text_with_stroke(draw, pos, text, font, fill_color, stroke_color, stroke_width):
    x, y = pos
    if stroke_width > 0:
        for dx in range(-stroke_width, stroke_width + 1):
            for dy in range(-stroke_width, stroke_width + 1):
                if dx * dx + dy * dy <= stroke_width * stroke_width:
                    draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    draw.text((x, y), text, font=font, fill=fill_color)

def create_wave_mask(width, height, split_x):
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    points = [(0, 0)]
    steps = 120
    for i in range(steps + 1):
        y = (height * i) / steps
        # gentle organic S-curve bulging out in the middle
        offset = math.sin((i / steps) * math.pi) * 95 + math.sin((i / steps) * math.pi * 2) * 30
        x = split_x + offset
        points.append((x, y))
        
    points.append((0, height))
    draw.polygon(points, fill=255)
    return mask

def render_master_cardnews(
    bg_path: str,
    output_path: str,
    badge_text: str,
    badge_bg: tuple,
    line1_text: str,
    line2_text: str,
    line2_color: tuple,
    sub_lines: list,
    footer_text: str,
    theme_top: tuple,
    theme_bot: tuple,
    split_x: int = 440
):
    W, H = 1080, 1350
    
    # 1. Base Photo
    raw = Image.open(bg_path).convert("RGBA")
    scale = H / raw.height
    new_w = int(raw.width * scale)
    scaled = raw.resize((new_w, H), Image.Resampling.LANCZOS)
    
    photo = Image.new("RGBA", (W, H), (15, 23, 42, 255))
    offset_x = W - new_w
    photo.paste(scaled, (offset_x, 0))
    
    # 2. Panel Mask & Shadow
    mask = create_wave_mask(W, H, split_x)
    shadow_mask = mask.filter(ImageFilter.GaussianBlur(20))
    s_layer = Image.new("RGBA", (W, H), (0, 0, 0, 155))
    photo.paste(s_layer, (0, 0), shadow_mask)
    
    # 3. Left Panel with Theme Gradient
    panel_img = Image.new("RGBA", (W, H), theme_top)
    p_draw = ImageDraw.Draw(panel_img)
    for y in range(H):
        ratio = y / H
        r = int(theme_top[0] * (1 - ratio) + theme_bot[0] * ratio)
        g = int(theme_top[1] * (1 - ratio) + theme_bot[1] * ratio)
        b = int(theme_top[2] * (1 - ratio) + theme_bot[2] * ratio)
        p_draw.line([(0, y), (W, y)], fill=(r, g, b, 255))
        
    # Decorative Dot Patterns
    dot_color = (255, 255, 255, 25)
    for row in range(6):
        for col in range(6):
            cx = split_x - 120 + col * 20
            cy = 80 + row * 20
            p_draw.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill=dot_color)
            
    for row in range(5):
        for col in range(5):
            cx = 70 + col * 20
            cy = 1180 + row * 20
            p_draw.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill=dot_color)
            
    # Composite panel onto photo
    canvas = Image.composite(panel_img, photo, mask)
    draw = ImageDraw.Draw(canvas)
    
    # 4. Fonts
    font_badge = ImageFont.truetype(F_PRETEND, 34)
    # Adapt main font size if text is long
    max_char = max(len(line1_text), len(line2_text))
    main_size = 130 if max_char <= 5 else (116 if max_char <= 7 else 102)
    font_main = ImageFont.truetype(F_BLACKHAN, main_size)
    font_sub = ImageFont.truetype(F_PRETEND, 48)
    font_footer = ImageFont.truetype(F_PRETEND, 32)
    
    # 5. Badge
    bx, by = 75, 175
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw = bbox[2] - bbox[0] + 36
    bh = bbox[3] - bbox[1] + 20
    draw.rounded_rectangle((bx, by, bx + bw, by + bh), radius=12, fill=badge_bg)
    draw.text((bx + 18, by + 10), badge_text, fill=(255, 255, 255), font=font_badge)
    
    # 6. Main Titles
    ty = by + bh + 45
    line_gap = int(main_size * 1.16)
    
    def render_title_line(y_pos, text, fill_col):
        if "·" in text:
            parts = text.split("·")
            t1 = parts[0]
            t2 = parts[1]
            bb1 = draw.textbbox((0, 0), t1, font=font_main)
            w1 = bb1[2] - bb1[0]
            draw_text_with_stroke(draw, (75, y_pos), t1, font_main, fill_col, (4, 10, 24), 6)
            
            # draw dot
            dot_x = 75 + w1 + 18
            dot_y = y_pos + (bb1[3] - bb1[1]) // 2 + 10
            r = 7
            draw.ellipse((dot_x - r - 2, dot_y - r - 2, dot_x + r + 2, dot_y + r + 2), fill=(4, 10, 24))
            draw.ellipse((dot_x - r, dot_y - r, dot_x + r, dot_y + r), fill=fill_col)
            
            draw_text_with_stroke(draw, (dot_x + 18, y_pos), t2, font_main, fill_col, (4, 10, 24), 6)
        else:
            draw_text_with_stroke(draw, (75, y_pos), text, font_main, fill_col, (4, 10, 24), 6)

    render_title_line(ty, line1_text, (255, 255, 255))
    render_title_line(ty + line_gap, line2_text, line2_color)
    
    # 7. Subtitles
    sy = ty + line_gap * 2 + 35
    for sline in sub_lines:
        draw_text_with_stroke(draw, (75, sy), sline, font_sub, (255, 255, 255), (0, 0, 0), 3)
        sy += 68
        
    # 8. Divider & Footer
    draw.line([(75, sy + 30), (280, sy + 30)], fill=line2_color, width=5)
    draw.text((75, sy + 58), footer_text, fill=(190, 215, 245), font=font_footer)
    
    # Save optimized PNG
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    canvas.convert("RGB").save(output_path, "PNG", optimize=True)
    print(f"Generated: {output_path}")

def generate_all():
    base_brain = r"C:\Users\sadase\.gemini\antigravity\brain\63192880-4f85-4647-986b-28fea0ed278d"
    
    tasks = [
        # 1. 체지방 1kg 빼는 칼로리
        {
            "bg": os.path.join(base_brain, "body_fat_loss_1791555042741.jpg"),
            "out": "health/body-fat-loss-calorie-deficit-calculator/thumbnail.png",
            "badge": "다이어트 정석",
            "badge_bg": (28, 78, 160),
            "line1": "체지방",
            "line2": "1kg 감량",
            "line2_color": (255, 215, 0),
            "subs": ["하루 500kcal 적자", "현실적인 감량 공식"],
            "footer": "BMR & TDEE 계산 가이드",
            "theme_top": (11, 35, 75),
            "theme_bot": (7, 20, 48),
            "split_x": 440
        },
        # 2. 공복 유산소 운동 vs 식후 운동
        {
            "bg": os.path.join(base_brain, "fasting_cardio_photo_1791555084596.jpg"),
            "out": "health/fasting-cardio-fat-loss-timing/thumbnail.png",
            "badge": "운동 생리학",
            "badge_bg": (14, 90, 111),
            "line1": "공복 유산소",
            "line2": "운동 타이밍",
            "line2_color": (255, 215, 0),
            "subs": ["체지방 감량 효과와", "근손실 방지 가이드"],
            "footer": "식후 운동 vs 공복 비교",
            "theme_top": (11, 48, 66),
            "theme_bot": (6, 26, 38),
            "split_x": 450
        },
        # 3. 간수치 AST ALT
        {
            "bg": os.path.join(base_brain, "liver_enzymes_photo_1791555105338.jpg"),
            "out": "health/liver-enzymes-ast-alt-guide/thumbnail.png",
            "badge": "검진 수치 판독",
            "badge_bg": (27, 94, 57),
            "line1": "간수치",
            "line2": "AST·ALT",
            "line2_color": (214, 245, 93), # Lime Yellow
            "subs": ["정상 수치 기준과", "원인별 간질환 관리"],
            "footer": "밀크씨슬 & 생활습관 가이드",
            "theme_top": (18, 52, 36),
            "theme_bot": (9, 28, 18),
            "split_x": 440
        },
        # 4. 고혈압 전단계 DASH 식단
        {
            "bg": os.path.join(base_brain, "blood_pressure_photo_1791555123727.jpg"),
            "out": "health/blood-pressure-stages-hypertension-diet/thumbnail.png",
            "badge": "혈관 건강 관리",
            "badge_bg": (122, 26, 43),
            "line1": "고혈압 전단계",
            "line2": "DASH 식단",
            "line2_color": (245, 199, 84), # Warm Gold
            "subs": ["수축기 130 이상 기준", "칼륨·나트륨 감량법"],
            "footer": "혈압 낮추는 식습관 가이드",
            "theme_top": (54, 16, 28),
            "theme_bot": (28, 7, 14),
            "split_x": 450
        },
        # 5. 혈당 스파이크 거꾸로 식사법
        {
            "bg": os.path.join(base_brain, "blood_sugar_photo_1791555146534.jpg"),
            "out": "health/blood-sugar-spike-prevention-diet/thumbnail.png",
            "badge": "혈당 관리 솔루션",
            "badge_bg": (146, 64, 14),
            "line1": "식후 혈당",
            "line2": "스파이크",
            "line2_color": (255, 229, 0), # Vivid Yellow
            "subs": ["채소 먼저 거꾸로 식사", "식후 15분 걷기 효과"],
            "footer": "식후 140mg/dL 안정 가이드",
            "theme_top": (66, 29, 10),
            "theme_bot": (36, 15, 4),
            "split_x": 440
        },
        # 6. 비타민D 복용시간
        {
            "bg": os.path.join(base_brain, "vitamin_d_photo_1791555166009.jpg"),
            "out": "health/vitamin-d-benefits-daily-intake-timing/thumbnail.png",
            "badge": "영양제 흡수율",
            "badge_bg": (28, 56, 95),
            "line1": "비타민D",
            "line2": "복용시간",
            "line2_color": (245, 199, 84), # Vivid Gold
            "subs": ["하루 2000IU 권장량", "마그네슘 필수 시너지"],
            "footer": "식후 흡수 골든타임 가이드",
            "theme_top": (15, 34, 64),
            "theme_bot": (8, 19, 36),
            "split_x": 440
        },
        # 7. 신규 글: 공복 혈당 정상 수치와 당뇨 전단계 관리 가이드
        {
            "bg": os.path.join(base_brain, "fasting_sugar_photo_1791555185031.jpg"),
            "out": "health/fasting-blood-sugar-normal-range-prediabetes/thumbnail.png",
            "badge": "국가건강검진 기준",
            "badge_bg": (13, 56, 104),
            "line1": "공복 혈당",
            "line2": "정상 수치",
            "line2_color": (255, 229, 0), # Vivid Yellow
            "subs": ["100~125mg/dL 전단계", "당화혈색소 5.7% 관리법"],
            "footer": "인슐린 저항성 개선 솔루션",
            "theme_top": (17, 36, 78),
            "theme_bot": (10, 21, 48),
            "split_x": 440
        }
    ]
    
    for t in tasks:
        render_master_cardnews(
            bg_path=t["bg"],
            output_path=t["out"],
            badge_text=t["badge"],
            badge_bg=t["badge_bg"],
            line1_text=t["line1"],
            line2_text=t["line2"],
            line2_color=t["line2_color"],
            sub_lines=t["subs"],
            footer_text=t["footer"],
            theme_top=t["theme_top"],
            theme_bot=t["theme_bot"],
            split_x=t["split_x"]
        )

if __name__ == '__main__':
    generate_all()

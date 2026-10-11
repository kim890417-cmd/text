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
        offset = math.sin((i / steps) * math.pi) * 95 + math.sin((i / steps) * math.pi * 2) * 30
        x = split_x + offset
        points.append((x, y))
        
    points.append((0, height))
    draw.polygon(points, fill=255)
    return mask

def render():
    W, H = 1080, 1350
    bg_path = r"C:\Users\sadase\.gemini\antigravity\brain\63192880-4f85-4647-986b-28fea0ed278d\acid_reflux_photo_1791704186855.jpg"
    out_path = r"health\acid-reflux-gerd-symptoms-diet-foods\thumbnail.png"
    
    # 1. Base Photo
    raw = Image.open(bg_path).convert("RGBA")
    scale = H / raw.height
    new_w = int(raw.width * scale)
    scaled = raw.resize((new_w, H), Image.Resampling.LANCZOS)
    
    photo = Image.new("RGBA", (W, H), (15, 23, 42, 255))
    offset_x = W - new_w
    photo.paste(scaled, (offset_x, 0))
    
    # 2. Panel Mask & Shadow
    split_x = 440
    mask = create_wave_mask(W, H, split_x)
    shadow_mask = mask.filter(ImageFilter.GaussianBlur(20))
    s_layer = Image.new("RGBA", (W, H), (0, 0, 0, 155))
    photo.paste(s_layer, (0, 0), shadow_mask)
    
    # 3. Left Panel with Theme Gradient (Deep Calming Sage / Forest Slate)
    theme_top = (20, 52, 40)
    theme_bot = (10, 28, 20)
    panel_img = Image.new("RGBA", (W, H), theme_top)
    p_draw = ImageDraw.Draw(panel_img)
    for y in range(H):
        ratio = y / H
        r = int(theme_top[0] * (1 - ratio) + theme_bot[0] * ratio)
        g = int(theme_top[1] * (1 - ratio) + theme_bot[1] * ratio)
        b = int(theme_top[2] * (1 - ratio) + theme_bot[2] * ratio)
        p_draw.line([(0, y), (W, y)], fill=(r, g, b, 255))
        
    # Dot Pattern
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
            
    canvas = Image.composite(panel_img, photo, mask)
    draw = ImageDraw.Draw(canvas)
    
    # 4. Fonts
    font_badge = ImageFont.truetype(F_PRETEND, 34)
    font_main = ImageFont.truetype(F_BLACKHAN, 116)
    font_sub = ImageFont.truetype(F_PRETEND, 48)
    font_footer = ImageFont.truetype(F_PRETEND, 32)
    
    # 5. Badge
    bx, by = 75, 175
    badge_text = "위식도 역류 관리"
    badge_bg = (30, 95, 68)
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw = bbox[2] - bbox[0] + 36
    bh = bbox[3] - bbox[1] + 20
    draw.rounded_rectangle((bx, by, bx + bw, by + bh), radius=12, fill=badge_bg)
    draw.text((bx + 18, by + 10), badge_text, fill=(255, 255, 255), font=font_badge)
    
    # 6. Main Titles
    ty = by + bh + 45
    line_gap = int(116 * 1.16)
    draw_text_with_stroke(draw, (75, ty), "역류성 식도염", font_main, (255, 255, 255), (4, 10, 24), 6)
    draw_text_with_stroke(draw, (75, ty + line_gap), "식단 & 습관", font_main, (255, 229, 0), (4, 10, 24), 7)
    
    # 7. Subtitles
    sy = ty + line_gap * 2 + 35
    sub_lines = ["좋은 음식 vs 나쁜 음식", "식후 3시간 눕기 금지"]
    for sline in sub_lines:
        draw_text_with_stroke(draw, (75, sy), sline, font_sub, (255, 255, 255), (0, 0, 0), 3)
        sy += 68
        
    # 8. Divider & Footer
    draw.line([(75, sy + 30), (280, sy + 30)], fill=(255, 229, 0), width=5)
    draw.text((75, sy + 58), "목 이물감 & 위산 역류 개선", fill=(190, 225, 210), font=font_footer)
    
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    canvas.convert("RGB").save(out_path, "PNG", optimize=True)
    print("Thumbnail generated:", out_path)

if __name__ == '__main__':
    render()

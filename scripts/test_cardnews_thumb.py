import urllib.request
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_cardnews_thumbnail(
    bg_img_url_or_path: str,
    badge_text: str,
    title_lines: list,
    point_text: str,
    output_path: str,
    accent_color=(56, 189, 248) # sky-400
):
    W, H = 800, 1000  # 4:5 세로형 카드뉴스 표준 해상도

    # 1. 배경 이미지 로드 및 800x1000 커버 크롭
    if bg_img_url_or_path.startswith('http'):
        temp_cache = "images/thumbnails/temp_bg.jpg"
        os.makedirs(os.path.dirname(temp_cache), exist_ok=True)
        req = urllib.request.Request(bg_img_url_or_path, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(temp_cache, 'wb') as f:
            f.write(resp.read())
        raw_img = Image.open(temp_cache).convert("RGBA")
    elif os.path.exists(bg_img_url_or_path):
        raw_img = Image.open(bg_img_url_or_path).convert("RGBA")
    else:
        # fallback gradient
        raw_img = Image.new("RGBA", (W, H), (15, 23, 42, 255))

    # Resize & cover crop to W, H
    img_aspect = raw_img.width / raw_img.height
    canvas_aspect = W / H
    if img_aspect > canvas_aspect:
        new_h = H
        new_w = int(H * img_aspect)
    else:
        new_w = W
        new_h = int(W / img_aspect)
    scaled_bg = raw_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - W) // 2
    top = (new_h - H) // 2
    bg_cropped = scaled_bg.crop((left, top, left + W, top + H))

    canvas = bg_cropped.copy()

    # 2. 다크 그라데이션 마스크 (하단 텍스트 가독성 확보)
    gradient = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(gradient)
    for y in range(H):
        if y < 350:
            alpha = int(40 * (y / 350))
        elif y < 600:
            ratio = (y - 350) / 250
            alpha = int(40 + (180 - 40) * ratio)
        else:
            ratio = (y - 600) / 400
            alpha = int(180 + (245 - 180) * ratio)
        g_draw.line([(0, y), (W, y)], fill=(10, 15, 28, alpha))
    
    canvas = Image.alpha_composite(canvas, gradient)
    draw = ImageDraw.Draw(canvas)

    # 3. 폰트
    font_badge = ImageFont.truetype(r'C:\Windows\Fonts\malgunbd.ttf', 24)
    font_title = ImageFont.truetype(r'C:\Windows\Fonts\malgunbd.ttf', 52)
    font_point = ImageFont.truetype(r'C:\Windows\Fonts\malgunbd.ttf', 28)
    font_logo = ImageFont.truetype(r'C:\Windows\Fonts\malgun.ttf', 20)

    # 4. 상단 브랜드 워터마크
    draw.text((45, 45), "건강노트 HealthFit", fill=(255, 255, 255, 200), font=font_logo)

    # 5. 카테고리 뱃지
    badge_str = f" {badge_text} "
    bbox = draw.textbbox((0, 0), badge_str, font=font_badge)
    bw = bbox[2] - bbox[0] + 20
    bh = bbox[3] - bbox[1] + 16
    by = 560
    draw.rounded_rectangle((45, by, 45 + bw, by + bh), radius=8, fill=accent_color)
    draw.text((55, by + 8), badge_str, fill=(10, 15, 28), font=font_badge)

    # 6. 메인 타이틀 (1~2줄, 글자 조금)
    ty = by + bh + 24
    for line in title_lines[:2]:
        # 그림자 효과
        draw.text((47, ty + 2), line, fill=(0, 0, 0, 180), font=font_title)
        draw.text((45, ty), line, fill=(255, 255, 255), font=font_title)
        ty += 68

    # 7. 핵심 포인트 (1줄 요약)
    py = ty + 15
    draw.text((47, py + 1), point_text, fill=(0, 0, 0, 150), font=font_point)
    draw.text((45, py), point_text, fill=(226, 232, 240), font=font_point)

    # 8. 테두리 미세 라인
    draw.rounded_rectangle((20, 20, W - 20, H - 20), radius=16, outline=(255, 255, 255, 30), width=2)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    canvas.convert("RGB").save(output_path, "JPEG", quality=90, optimize=True)
    print(f"Generated cardnews thumbnail: {output_path}")

if __name__ == '__main__':
    # Test sample
    create_cardnews_thumbnail(
        bg_img_url_or_path="https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=800&q=80",
        badge_text="다이어트 꿀팁",
        title_lines=["체지방 1kg", "태우는 현실 공식"],
        point_text="✓ 하루 500kcal 적자의 과학",
        output_path="images/thumbnails/test_cardnews_45.jpg"
    )

import os
import re
import shutil
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")
HEALTH_DIR = REPO_DIR / "health"

MAPPING = {
    "bmi-계산법": "bmi-calculator-korean-standard",
    "tdee계산하는법": "tdee-calculator-daily-energy-expenditure",
    "근육-유지와-다이어트를-위해-단백질-섭취의-중요성": "protein-intake-muscle-maintenance-diet",
    "기초대사량-계산법": "bmr-basal-metabolic-rate-formula",
    "눈-뻑뻑함과-계단-어지러움-루테인과-철분제-낭비-없": "dry-eyes-fatigue-lutein-iron-benefits",
    "다이어트를-하는-분들이-매일-아침-오르는-체중계의": "weight-scale-fluctuation-morning-truth",
    "마그네슘-하루-권장량": "magnesium-daily-recommended-intake-timing",
    "멀티비타민-언제-먹어야-효과-좋을까": "multivitamin-best-time-to-take",
    "생리주기-계산법": "menstrual-cycle-calculator-ovulation",
    "서브웨이-칼로리": "subway-sandwich-low-calorie-diet-menu",
    "소주-주량-계산": "soju-alcohol-breakdown-hangover-time",
    "스타벅스-칼로리": "starbucks-drink-low-calorie-diet-guide",
    "여자-적정-체중": "female-ideal-healthy-weight-standard",
    "영양제-상한섭취량": "supplement-upper-intake-limit-overdose",
    "오메가3": "omega3-supplement-benefits-rtg-intake",
    "와인칼로리": "wine-calories-sugar-hangover-guide",
    "운동-소모-칼로리-계산": "exercise-calories-burned-met-calculator",
    "임산부-엽산-권장량": "pregnancy-folic-acid-dosage-timing",
    "임산부-체중증가": "pregnancy-weight-gain-guidelines-bmi",
    "칼슘-하루-권장-섭취량": "calcium-daily-recommended-intake-timing",
    "하루-물-섭취량": "daily-water-intake-calculator-benefits",
    "하루-카페인-권장량": "caffeine-daily-intake-limit-side-effects",
    "헬스장-트레이너나": "gym-trainer-diet-carbohydrate-truth"
}

print(f"Total mappings: {len(MAPPING)}")

# 1. Migrate folders and contents
for kor, eng in MAPPING.items():
    kor_path = HEALTH_DIR / kor
    eng_path = HEALTH_DIR / eng
    
    if not kor_path.exists():
        print(f"Warning: {kor_path} does not exist!")
        continue
        
    eng_path.mkdir(parents=True, exist_ok=True)
    
    # Read old index.html
    old_index_file = kor_path / "index.html"
    old_html = old_index_file.read_text(encoding="utf-8", errors="ignore")
    
    # Update new HTML with new slug
    new_html = old_html
    new_html = new_html.replace(f"/health/{kor}/", f"/health/{eng}/")
    new_html = new_html.replace(f"/health/{kor}", f"/health/{eng}/")
    
    # Write to new destination
    new_index_file = eng_path / "index.html"
    new_index_file.write_text(new_html, encoding="utf-8")
    
    # Copy thumbnail.png
    old_thumb = kor_path / "thumbnail.png"
    if old_thumb.exists():
        new_thumb = eng_path / "thumbnail.png"
        shutil.copy2(old_thumb, new_thumb)
        
    # Write Redirect HTML to old Korean folder so zero broken links or 404s!
    redirect_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>페이지 이동 중... | 건강노트</title>
  <meta http-equiv="refresh" content="0; url=https://healthfit100.com/health/{eng}/">
  <link rel="canonical" href="https://healthfit100.com/health/{eng}/">
  <meta name="robots" content="noindex, follow">
  <script>
    window.location.replace("https://healthfit100.com/health/{eng}/");
  </script>
</head>
<body style="font-family:-apple-system,BlinkMacSystemFont,sans-serif; text-align:center; padding:60px 20px; color:#334155;">
  <h2>새로운 주소로 안전하게 이동합니다</h2>
  <p style="color:#64748b;">잠시만 기다려 주시면 공식 페이지로 자동 연결됩니다.</p>
  <p><a href="https://healthfit100.com/health/{eng}/" style="color:#0284c7; font-weight:600;">직접 이동하기 →</a></p>
</body>
</html>
"""
    old_index_file.write_text(redirect_html, encoding="utf-8")
    print(f"Migrated: {kor} -> {eng} (Redirect installed)")

# 2. Update all references in blog.html, index.html, other html files
all_html_files = list(REPO_DIR.glob("*.html")) + list(HEALTH_DIR.glob("**/*.html"))

for hf in all_html_files:
    # Skip the redirect files themselves
    if hf.parent.name in MAPPING:
        continue
    content = hf.read_text(encoding="utf-8", errors="ignore")
    modified = False
    for kor, eng in MAPPING.items():
        if f"/health/{kor}/" in content or f"/health/{kor}" in content:
            content = content.replace(f"/health/{kor}/", f"/health/{eng}/")
            content = content.replace(f"/health/{kor}", f"/health/{eng}/")
            modified = True
        # Also check urlencoded forms
        import urllib.parse
        enc_kor = urllib.parse.quote(kor)
        if f"/health/{enc_kor}/" in content or f"/health/{enc_kor}" in content:
            content = content.replace(f"/health/{enc_kor}/", f"/health/{eng}/")
            content = content.replace(f"/health/{enc_kor}", f"/health/{eng}/")
            modified = True
            
    if modified:
        hf.write_text(content, encoding="utf-8")
        print(f"Updated references in: {hf.relative_to(REPO_DIR)}")

# 3. Update sitemap.xml
sitemap_file = REPO_DIR / "sitemap.xml"
if sitemap_file.exists():
    s_content = sitemap_file.read_text(encoding="utf-8")
    for kor, eng in MAPPING.items():
        import urllib.parse
        enc_kor = urllib.parse.quote(kor)
        s_content = s_content.replace(f"/health/{enc_kor}/", f"/health/{eng}/")
        s_content = s_content.replace(f"/health/{enc_kor}", f"/health/{eng}/")
        s_content = s_content.replace(f"/health/{kor}/", f"/health/{eng}/")
        s_content = s_content.replace(f"/health/{kor}", f"/health/{eng}/")
    sitemap_file.write_text(s_content, encoding="utf-8")
    print("Updated sitemap.xml")

# 4. Update rss.xml
rss_file = REPO_DIR / "rss.xml"
if rss_file.exists():
    r_content = rss_file.read_text(encoding="utf-8")
    for kor, eng in MAPPING.items():
        import urllib.parse
        enc_kor = urllib.parse.quote(kor)
        r_content = r_content.replace(f"/health/{enc_kor}/", f"/health/{eng}/")
        r_content = r_content.replace(f"/health/{enc_kor}", f"/health/{eng}/")
        r_content = r_content.replace(f"/health/{kor}/", f"/health/{eng}/")
        r_content = r_content.replace(f"/health/{kor}", f"/health/{eng}/")
    rss_file.write_text(r_content, encoding="utf-8")
    print("Updated rss.xml")

print("Migration completed successfully!")

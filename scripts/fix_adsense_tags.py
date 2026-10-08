import re
from pathlib import Path

p = Path(".")
html_files = list(p.glob("*.html")) + list((p / "health").glob("**/*.html"))

fixed_count = 0
for hf in html_files:
    content = hf.read_text(encoding="utf-8")
    original = content
    
    # 1. Remove Site Kit platform meta tags
    content = re.sub(r'<!-- Site Kit에서 추가한 Google AdSense 메타 태그 -->[\s\S]*?<!-- Site Kit에서 추가한 Google AdSense 메타 태그 종료 -->', '', content)
    content = re.sub(r'<meta name="google-adsense-platform-account" content="[^"]*">\s*', '', content)
    content = re.sub(r'<meta name="google-adsense-platform-domain" content="[^"]*">\s*', '', content)
    
    # 2. Normalize AdSense script tags: remove &host=ca-host-pub-...
    content = re.sub(r'https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-3406696816625207(?:&|&amp;|&#038;)host=ca-host-pub-[0-9]+', 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3406696816625207', content)
    content = re.sub(r'https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-3406696816625207&amp;host=ca-host-pub-[0-9]+', 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3406696816625207', content)
    content = re.sub(r'https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-3406696816625207&host=ca-host-pub-[0-9]+', 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3406696816625207', content)
    
    # 3. Clean up comments
    content = content.replace("<!-- Site Kit에 의해 추가된 Google AdSense 스니펫 -->", "")
    content = content.replace("<!-- Site Kit에 의해 추가된 Google AdSense 스니펫 종료 -->", "")
    
    if content != original:
        hf.write_text(content, encoding="utf-8")
        fixed_count += 1

print(f"Fixed AdSense tags in {fixed_count} files!")

# 4. Enhance privacy.html with official Google AdSense Cookie requirements
privacy_file = p / "privacy.html"
if privacy_file.exists():
    pc = privacy_file.read_text(encoding="utf-8")
    old_section3 = """        <h2>3. 제3자 광고 및 데이터 활용</h2>
        <p>본 사이트는 서비스 운영 및 품질 개선을 위해 다음과 같은 외부 서비스를 활용합니다.</p>
        <ul>
          <li><strong>Google AdSense:</strong> 광고 게재를 위해 사용자의 방문 기록 및 관심 분야를 분석하는 쿠키를 사용합니다. 이는 익명화된 데이터로 처리됩니다.</li>

        </ul>"""

    new_section3 = """        <h2>3. Google AdSense 및 제3자 광고 쿠키 정책</h2>
        <p>본 사이트는 서비스 운영 및 양질의 무료 콘텐츠 제공을 위해 <strong>Google AdSense</strong>를 포함한 제3자 광고 서비스를 활용합니다.</p>
        <ul>
          <li><strong>광고 쿠키의 사용:</strong> Google을 포함한 제3자 제공업체는 사용자가 본 웹사이트 또는 다른 웹사이트를 이전에 방문한 기록을 바탕으로 광고를 게재하기 위해 쿠키(Cookie)를 사용합니다.</li>
          <li><strong>맞춤형 광고 게재:</strong> Google의 광고 쿠키 사용을 통해 Google 및 그 파트너는 사용자의 본 사이트 및 인터넷상의 다른 사이트 방문 정보를 기반으로 적절한 맞춤형 광고를 표시할 수 있습니다.</li>
          <li><strong>맞춤형 광고 수신 거부(Opt-out):</strong> 사용자는 언제든지 <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google 광고 설정</a> 페이지를 방문하여 맞춤형 광고 게재를 비활성화할 수 있습니다. 또한 <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">AboutAds.info</a>를 통해서도 제3자 업체의 쿠키 사용을 선택적으로 차단하실 수 있습니다.</li>
        </ul>"""

    if old_section3 in pc:
        pc = pc.replace(old_section3, new_section3)
        privacy_file.write_text(pc, encoding="utf-8")
        print("Updated privacy.html with full Google AdSense compliant cookie policy!")

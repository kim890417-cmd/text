import re
from pathlib import Path

index_path = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo\index.html")
content = index_path.read_text(encoding="utf-8")

# 1. Enhanced robots, author, keywords
robots_tag = '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">'
author_tag = '<meta name="author" content="건강노트">'
keywords_tag = '<meta name="keywords" content="건강노트, 건강 매거진, 영양성분표 보는법, 식단 계산, 혈당 스파이크, 콜레스테롤 수치, 비타민 하루 권장량, 기초대사량 계산기, 건강 계산기">'

if '<meta name="robots" content="index,follow">' in content:
    content = content.replace(
        '<meta name="robots" content="index,follow">',
        f'{robots_tag}\n{author_tag}\n{keywords_tag}'
    )
    print("Replaced robots and added author & keywords")

# 2. Add Schema.org structured data JSON-LD
schema_json = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://healthfit100.com/#website",
      "url": "https://healthfit100.com/",
      "name": "건강노트",
      "alternateName": ["healthfit100", "헬스핏100"],
      "description": "영양제 표시 읽기, 식단 계산, 건강검진 수치 해석과 일상 습관을 노트의 질문과 비교로 정리하는 건강 전문 매거진",
      "inLanguage": "ko-KR",
      "publisher": {
        "@type": "Organization",
        "@id": "https://healthfit100.com/#organization",
        "name": "건강노트",
        "url": "https://healthfit100.com/about",
        "logo": {
          "@type": "ImageObject",
          "url": "https://healthfit100.com/images/note/note-glucose.webp"
        }
      }
    },
    {
      "@type": "Organization",
      "@id": "https://healthfit100.com/#organization",
      "name": "건강노트",
      "url": "https://healthfit100.com/",
      "logo": "https://healthfit100.com/images/note/note-glucose.webp",
      "sameAs": [
        "https://app.healthfit100.com/"
      ]
    }
  ]
}
</script>"""

if "</head>" in content and "application/ld+json" not in content:
    content = content.replace("</head>", f"{schema_json}\n</head>")
    print("Added Schema.org WebSite JSON-LD")

index_path.write_text(content, encoding="utf-8")
print("index.html SEO update complete!")

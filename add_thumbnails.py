import os

repo_path = r'C:\Users\User\Desktop\키워드 글쓰기\healthfit_repo'

IMAGE_MAP = {
    '아연-효능과-하루-권장량-총정리-남성-건강에-꼭-필요한-이유': (
        'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=800&h=450&fit=crop&q=80',
        '아연 영양제 효능과 하루 권장량'
    ),
    '단백질-하루-섭취량-계산법과-필수-아미노산-식품': (
        'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=800&h=450&fit=crop&q=80',
        '단백질 하루 섭취량 계산법과 고단백 식품'
    ),
    '철분제-효능과-빈혈-증상-예방-가이드-복용-시-주의할-음식-및-부작용': (
        'https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=800&h=450&fit=crop&q=80',
        '철분제 효능과 빈혈 예방 영양제'
    ),
    '잠-잘-오는-음식-5가지와-멜라토닌-영양제-복용-솔직-후기': (
        'https://images.unsplash.com/photo-1541480601022-2308c0f02487?w=800&h=450&fit=crop&q=80',
        '잠 잘 오는 음식과 멜라토닌 수면 영양제'
    ),
    '눈-뻑뻑함과-계단-어지러움-루테인과-철분제-낭비-없': (
        'https://images.unsplash.com/photo-1576678927484-cc907957088c?w=800&h=450&fit=crop&q=80',
        '루테인 철분제 복용법과 눈 건강 영양제'
    ),
    '멀티비타민-언제-먹어야-효과-좋을까': (
        'https://images.unsplash.com/photo-1516997121675-4c2d1684aa3e?w=800&h=450&fit=crop&q=80',
        '멀티비타민 복용 시간과 효과 극대화 방법'
    ),
    '칼슘-하루-권장-섭취량': (
        'https://images.unsplash.com/photo-1563636619-e9143da7973b?w=800&h=450&fit=crop&q=80',
        '칼슘 하루 권장 섭취량과 흡수율 높이는 방법'
    ),
    '마그네슘-하루-권장량': (
        'https://images.unsplash.com/photo-1498557850523-fd3d118b962e?w=800&h=450&fit=crop&q=80',
        '마그네슘 하루 권장량과 부작용 없는 복용법'
    ),
    '단백질-권장량': (
        'https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=800&h=450&fit=crop&q=80',
        '단백질 하루 권장량과 고단백 식품 추천'
    ),
    '근육-유지와-다이어트를-위해-단백질-섭취의-중요성': (
        'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800&h=450&fit=crop&q=80',
        '근육 유지와 다이어트를 위한 단백질 섭취'
    ),
    'tdee계산하는법': (
        'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800&h=450&fit=crop&q=80',
        'TDEE 계산하는 법과 다이어트 칼로리 설정'
    ),
    '오메가3': (
        'https://images.unsplash.com/photo-1519682577862-22b62b24e493?w=800&h=450&fit=crop&q=80',
        '오메가3 복용시간 및 하루 권장량'
    ),
    '다이어트를-하는-분들이-매일-아침-오르는-체중계의': (
        'https://images.unsplash.com/photo-1535914254981-b5012eebbd15?w=800&h=450&fit=crop&q=80',
        '다이어트 체중 변동 이유와 올바른 체중 관리법'
    ),
    '기초대사량-계산법': (
        'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=800&h=450&fit=crop&q=80',
        '기초대사량 계산법과 다이어트 적용 방법'
    ),
    '여자-적정-체중': (
        'https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=800&h=450&fit=crop&q=80',
        '여자 적정 체중 기준과 건강한 체중 관리'
    ),
    '영양제-상한섭취량': (
        'https://images.unsplash.com/photo-1587854680352-936b22b91030?w=800&h=450&fit=crop&q=80',
        '영양제 상한 섭취량과 과다복용 주의사항'
    ),
    '소주-주량-계산': (
        'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&h=450&fit=crop&q=80',
        '소주 주량 계산과 적정 음주량 기준'
    ),
    '임산부-엽산-권장량': (
        'https://images.unsplash.com/photo-1476703993599-0035a21b17a9?w=800&h=450&fit=crop&q=80',
        '임산부 엽산 권장량과 임신 초기 영양제'
    ),
    '서브웨이-칼로리': (
        'https://images.unsplash.com/photo-1509722747041-616f39b57569?w=800&h=450&fit=crop&q=80',
        '서브웨이 칼로리 메뉴별 정리'
    ),
    '스타벅스-칼로리': (
        'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800&h=450&fit=crop&q=80',
        '스타벅스 음료 칼로리 정리'
    ),
    '와인칼로리': (
        'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800&h=450&fit=crop&q=80',
        '와인 칼로리와 다이어트 주의사항'
    ),
    '임산부-체중증가': (
        'https://images.unsplash.com/photo-1491013516836-7db643ee125a?w=800&h=450&fit=crop&q=80',
        '임산부 적정 체중 증가량과 임신 체중 관리'
    ),
    '생리주기-계산법': (
        'https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?w=800&h=450&fit=crop&q=80',
        '생리주기 계산법과 가임기 계산'
    ),
    '운동-소모-칼로리-계산': (
        'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&h=450&fit=crop&q=80',
        '운동 소모 칼로리 계산과 종목별 칼로리 소모량'
    ),
    'bmi-계산법': (
        'https://images.unsplash.com/photo-1576678927484-cc907957088c?w=800&h=450&fit=crop&q=80',
        'BMI 계산법과 체질량지수 해석'
    ),
    '하루-물-섭취량': (
        'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=800&h=450&fit=crop&q=80',
        '하루 물 섭취량 권장량과 수분 보충 방법'
    ),
    '하루-카페인-권장량': (
        'https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=800&h=450&fit=crop&q=80',
        '하루 카페인 권장량과 카페인 과다 섭취 주의'
    ),
    '헬스장-트레이너나': (
        'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800&h=450&fit=crop&q=80',
        '헬스장 트레이너 선택 방법과 운동 효과'
    ),
}

def make_figure_html(img_url, alt_text):
    return f'''<figure class="post-thumb-img-content" style="margin:0 0 1.5em 0;border-radius:8px;overflow:hidden;text-align:center;">
<img src="{img_url}" alt="{alt_text}" width="800" height="450" loading="lazy" style="width:100%;height:auto;display:block;object-fit:cover;">
<figcaption style="font-size:12px;color:#888888;margin-top:6px;text-align:center;">사진 출처: Unsplash</figcaption>
</figure>
'''

updated_count = 0
for dirname, (img_url, alt_text) in IMAGE_MAP.items():
    filepath = os.path.join(repo_path, 'health', dirname, 'index.html')
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 기존 div 기반 썸네일 제거 후 figure 형태로 대체
    fig_html = make_figure_html(img_url, alt_text)
    
    if '<div class="post-thumb-img-content"' in content:
        # Replace existing div block up to </div>
        start = content.find('<div class="post-thumb-img-content"')
        end = content.find('</div>\n', start) + len('</div>\n')
        content = content[:start] + fig_html + content[end:]
    elif '<figure class="post-thumb-img-content"' not in content:
        target = '<header class="entry-header "'
        if target in content:
            content = content.replace(target, fig_html + target, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    updated_count += 1

print(f'{updated_count}개 파일 이미지 출처(사진 출처: Unsplash) 표시 완료!')

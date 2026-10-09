import os
import re
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = r"C:\Users\sadase\Desktop\블로그 설정\fonts"
F_BLACKHAN = os.path.join(FONT_DIR, "BlackHanSans-Regular.ttf")
F_PRETEND = os.path.join(FONT_DIR, "Pretendard-Bold.ttf")

if not os.path.exists(F_BLACKHAN):
    F_BLACKHAN = r"C:\Windows\Fonts\malgunbd.ttf"
if not os.path.exists(F_PRETEND):
    F_PRETEND = r"C:\Windows\Fonts\malgunbd.ttf"

os.makedirs("images/tools", exist_ok=True)

# -------------------------------------------------------------------
# Infographic Generator Function
# -------------------------------------------------------------------
def create_infographic(
    badge_text: str,
    title_text: str,
    subtitle_text: str,
    steps: list,
    output_path: str
):
    W, H = 1200, 675
    canvas = Image.new("RGBA", (W, H), (15, 23, 42, 255)) # Slate-900
    draw = ImageDraw.Draw(canvas)

    font_badge = ImageFont.truetype(F_PRETEND, 22)
    font_title = ImageFont.truetype(F_PRETEND, 36)
    font_sub = ImageFont.truetype(F_PRETEND, 22)

    # Top Badge
    bbox = draw.textbbox((0, 0), f" {badge_text} ", font=font_badge)
    bw, bh = bbox[2] - bbox[0] + 20, bbox[3] - bbox[1] + 12
    draw.rounded_rectangle((60, 45, 60 + bw, 45 + bh), radius=8, fill=(2, 132, 199))
    draw.text((70, 51), f" {badge_text} ", font=font_badge, fill=(255, 255, 255))
    draw.text((60 + bw + 20, 52), "건강노트 HealthFit 팩트체크", font=font_badge, fill=(148, 163, 184))

    # Title & Subtitle
    draw.text((60, 102), title_text, font=font_title, fill=(255, 255, 255))
    draw.text((60, 156), subtitle_text, font=font_sub, fill=(56, 189, 248))

    # Grid parameters
    n_cards = len(steps)
    gap = 20
    total_w = W - 120
    card_w = (total_w - (n_cards - 1) * gap) // n_cards
    card_h = 425
    start_x = 60
    start_y = 200

    font_step = ImageFont.truetype(F_PRETEND, 20)
    font_time = ImageFont.truetype(F_PRETEND, 23 if n_cards <= 3 else 21)
    font_item = ImageFont.truetype(F_PRETEND, 19 if n_cards <= 3 else 17)
    font_tip_title = ImageFont.truetype(F_PRETEND, 18 if n_cards <= 3 else 16)
    font_tip_body = ImageFont.truetype(F_PRETEND, 18 if n_cards <= 3 else 16)

    for i, s in enumerate(steps):
        cx = start_x + i * (card_w + gap)
        cy = start_y
        card_color = s.get('color', (56, 189, 248))

        # Card container
        draw.rounded_rectangle((cx, cy, cx + card_w, cy + card_h), radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
        # Top accent strip
        draw.rounded_rectangle((cx, cy, cx + card_w, cy + 8), radius=4, fill=card_color)

        # Header step & label
        draw.text((cx + 18, cy + 22), s['step'], font=font_step, fill=card_color)
        draw.text((cx + 18, cy + 50), s['time'], font=font_time, fill=(255, 255, 255))

        # Divider
        draw.line([(cx + 18, cy + 90), (cx + card_w - 18, cy + 90)], fill=(51, 65, 85), width=1)

        # Content items
        iy = cy + 106
        for item in s['items']:
            draw.rounded_rectangle((cx + 14, iy, cx + card_w - 14, iy + 44), radius=8, fill=(15, 23, 42))
            draw.text((cx + 22, iy + 10), f"• {item}", font=font_item, fill=(241, 245, 249))
            iy += 52

        # Tip box at bottom
        tip_box_h = 135
        tip_y = cy + card_h - tip_box_h - 14
        draw.rounded_rectangle((cx + 14, tip_y, cx + card_w - 14, cy + card_h - 14), radius=10, fill=(15, 23, 42, 180))

        draw.text((cx + 22, tip_y + 12), "✓ 핵심 가이드:", font=font_tip_title, fill=card_color)

        # wrap tip text
        words = s['tip'].split()
        lines = []
        cur = ""
        max_chars = 14 if n_cards == 4 else 18
        for w in words:
            if len(cur + " " + w) > max_chars:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)

        ty = tip_y + 40
        for line in lines[:3]:
            draw.text((cx + 22, ty), line, font=font_tip_body, fill=(203, 213, 225))
            ty += 26

    # Outer decorative frame
    draw.rounded_rectangle((20, 20, W - 20, H - 20), radius=20, outline=(255, 255, 255, 30), width=2)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    canvas.convert("RGB").save(output_path, "PNG", optimize=True)
    print(f"Generated infographic: {output_path}")

# -------------------------------------------------------------------
# Data Map for 11 Tools
# -------------------------------------------------------------------
INFOGRAPHICS = [
    {
        'id': 'routine',
        'file': 'routine.html',
        'badge': '시그니처 가이드',
        'title': '하루 4단계 영양제 복용 골든타임 가이드',
        'subtitle': '흡수율을 2배 높이고 상극 충돌을 피하는 과학적 타이밍',
        'steps': [
            {
                'step': '1단계',
                'time': '기상 직후 (공복)',
                'items': ['유산균 (프로바이오틱스)', '비타민 B군'],
                'tip': '미온수 1~2잔 먼저 마셔 위산 희석 후 복용',
                'color': (56, 189, 248) # sky
            },
            {
                'step': '2단계',
                'time': '점심 식사 직후',
                'items': ['비타민 D', '오메가3', '루테인'],
                'tip': '지용성 성분은 식사 중 담즙산 분비 시 흡수 50%↑',
                'color': (250, 204, 21) # yellow
            },
            {
                'step': '3단계',
                'time': '저녁 식사 직후',
                'items': ['칼슘', '아연'],
                'tip': '철분과 최소 2시간 분리 복용, 위장 부담 완화',
                'color': (52, 211, 153) # emerald
            },
            {
                'step': '4단계',
                'time': '취침 1시간 전',
                'items': ['마그네슘', '테아닌'],
                'tip': '신경과 근육 이완을 도와 편안한 숙면 유도',
                'color': (192, 132, 252) # purple
            }
        ],
        'caption': '건강노트 의학 연구 기준 하루 4단계 최적 영양제 복용 시간표'
    },
    {
        'id': 'calorie',
        'file': 'calorie.html',
        'badge': '다이어트 에너지',
        'title': '에너지 균형 & 일일 500kcal 적자(Deficit) 공식',
        'subtitle': '기초대사량(BMR)과 활동대사량(TDEE)으로 설계하는 감량 플랜',
        'steps': [
            {
                'step': '1단계',
                'time': '기초대사량 (BMR)',
                'items': ['호흡·심장박동 생명 유지', '총 소비의 60~70% 차지'],
                'tip': '절대 BMR 이하로 굶지 않아야 요요와 근손실 방지',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '활동대사량 (TDEE)',
                'items': ['BMR × 활동계수(1.2~1.9)', '하루 실제 총 칼로리 소비'],
                'tip': '내 일상 움직임에 맞는 정확한 활동 계수 적용',
                'color': (250, 204, 21)
            },
            {
                'step': '3단계',
                'time': '하루 500kcal 적자',
                'items': ['주당 3,500kcal 에너지 절감', '요요 없는 건강한 체중 감량'],
                'tip': '1주일에 순수 체지방 약 0.45kg을 안전하게 감량',
                'color': (52, 211, 153)
            }
        ],
        'caption': '미플린-세인트 지오르 공식 기반 BMR, TDEE 및 체지방 감량 적자 계산'
    },
    {
        'id': 'bmi',
        'file': 'bmi.html',
        'badge': '체성분 정밀 진단',
        'title': '대한비만학회 한국인 성인 BMI 비만도 4단계 기준',
        'subtitle': '체질량지수(BMI)와 허리둘레를 함께 보는 표준 체형 진단',
        'steps': [
            {
                'step': '1단계',
                'time': '저체중 (18.5 미만)',
                'items': ['면역력 저하 주의', '골밀도 & 근육량 관리'],
                'tip': '균형 잡힌 단백질 섭취와 점진적 근력 운동 권장',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '정상 체중 (18.5~22.9)',
                'items': ['가장 이상적인 건강 체중', '만성질환 사망 위험 최저'],
                'tip': '현재의 건강한 식습관과 유산소 활동 유지',
                'color': (52, 211, 153)
            },
            {
                'step': '3단계',
                'time': '비만전단계 (23.0~24.9)',
                'items': ['과체중 단계 진입', '내장지방 축적 모니터링'],
                'tip': '식사량 10% 조절 및 일상 활동량 증가 권장',
                'color': (250, 204, 21)
            },
            {
                'step': '4단계',
                'time': '1단계 비만 (25.0 이상)',
                'items': ['허리둘레 동시 관리 필수', '고혈압·당뇨 위험 증가'],
                'tip': '남 90cm / 여 85cm 복부비만 여부 함께 확인',
                'color': (244, 63, 94)
            }
        ],
        'caption': '대한비만학회 아시아-태평양 비만 진단 기준표'
    },
    {
        'id': 'protein',
        'file': 'protein.html',
        'badge': '영양 섭취 기준',
        'title': '활동 강도별 하루 단백질 권장 섭취량 가이드',
        'subtitle': '체중 1kg당 최적 단백질(g)과 근육 단백질 합성 골든타임',
        'steps': [
            {
                'step': '1단계',
                'time': '일반 성인 (좌식)',
                'items': ['체중 1kg당 0.8~1.0g', '체중 60kg 기준 48~60g'],
                'tip': '생체 조직 유지 및 노화에 따른 근감소증 예방',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '다이어트 & 유산소',
                'items': ['체중 1kg당 1.2~1.4g', '체중 60kg 기준 72~84g'],
                'tip': '칼로리 적자 상태에서 근손실 방지 & 높은 포만감',
                'color': (250, 204, 21)
            },
            {
                'step': '3단계',
                'time': '고강도 근력 운동',
                'items': ['체중 1kg당 1.6~2.0g', '체중 60kg 기준 96~120g'],
                'tip': '식사당 25~30g씩 3~4회 나누어 섭취 시 합성 극대화',
                'color': (52, 211, 153)
            }
        ],
        'caption': '한국인 영양소 섭취기준 및 국제스포츠영양학회(ISSN) 권장 단백질량'
    },
    {
        'id': 'exercise',
        'file': 'exercise.html',
        'badge': '운동 대사 소비',
        'title': '운동 종목별 시간당 칼로리 소모량 (METs 기준 / 65kg)',
        'subtitle': '신체활동 강도와 체중을 반영한 정확한 에너지 소비율',
        'steps': [
            {
                'step': '1단계',
                'time': '가벼운 걷기 (3.5 METs)',
                'items': ['시간당 약 238 kcal 소모', '일상 출퇴근 및 산책'],
                'tip': '식후 15분 걷기는 혈당 스파이크 예방에 탁월',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '자전거 타기 (6.0 METs)',
                'items': ['시간당 약 410 kcal 소모', '유산소 심폐 지구력'],
                'tip': '관절 부담 없이 지속 가능한 안전한 유산소 운동',
                'color': (52, 211, 153)
            },
            {
                'step': '3단계',
                'time': '인터벌 러닝 (8.0 METs)',
                'items': ['시간당 약 546 kcal 소모', '체지방 급속 산화'],
                'tip': '운동 후에도 칼로리가 소모되는 EPOC 효과 유도',
                'color': (250, 204, 21)
            },
            {
                'step': '4단계',
                'time': '수영 / 웨이트 (9.5 METs)',
                'items': ['시간당 약 648 kcal 소모', '전신 근력 및 대사 촉진'],
                'tip': '근육량 증가로 기초대사량을 높이는 근본적 감량',
                'color': (244, 63, 94)
            }
        ],
        'caption': '미국 스포츠의학회(ACSM) 신체활동 METs 표준 소비 칼로리'
    },
    {
        'id': 'water',
        'file': 'water.html',
        'badge': '수분 밸런스',
        'title': '내 몸 맞춤 하루 수분 섭취량 & 최적 음용 타이밍',
        'subtitle': '체중과 활동량을 반영한 하루 물 필요량과 마시는 방법',
        'steps': [
            {
                'step': '1단계',
                'time': '내 필요 수분량 계산',
                'items': ['체중(kg) × 30~35mL', '60kg 성인 = 약 1.8~2.1L'],
                'tip': '음식 속 수분을 감안해 순수 물은 1.5~2.0L 목표',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '최적의 음용 타이밍',
                'items': ['기상 직후 미온수 1잔', '식전 30분 1잔, 일과 중 수시'],
                'tip': '식사 직후 찬물 과음은 소화효소를 희석할 수 있음',
                'color': (52, 211, 153)
            },
            {
                'step': '3단계',
                'time': '탈수 예방 핵심 수칙',
                'items': ['갈증 전 미리 한 모금씩', '커피 마신 후 동량 물 보충'],
                'tip': '소변 색이 옅은 레모네이드 색이면 적정 수분 상태',
                'color': (250, 204, 21)
            }
        ],
        'caption': '보건복지부 한국인 수분 섭취기준 및 세계보건기구(WHO) 가이드'
    },
    {
        'id': 'caffeine',
        'file': 'caffeine.html',
        'badge': '카페인 안전 한도',
        'title': '음료별 카페인 함량 & 일일 최대 안전 한도 가이드',
        'subtitle': '식품의약품안전처 고시 기준과 부작용 없는 섭취 타이밍',
        'steps': [
            {
                'step': '1단계',
                'time': '일일 최대 안전 한도',
                'items': ['성인: 하루 400mg 이하', '임산부: 하루 300mg 이하'],
                'tip': '청소년은 체중 1kg당 2.5mg 이하로 제한 권고',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '대표 음료 속 함량',
                'items': ['아메리카노: 150~200mg', '에너지음료: 100mg / 캔커피: 75mg'],
                'tip': '하루 아메리카노 2잔이면 일일 한도의 약 80% 도달',
                'color': (250, 204, 21)
            },
            {
                'step': '3단계',
                'time': '카페인 골든타임',
                'items': ['기상 2시간 후 첫 커피', '취침 6시간 전 섭취 중단'],
                'tip': '기상 직후엔 코르티솔 분비로 카페인 내성 증가 주의',
                'color': (192, 132, 252)
            }
        ],
        'caption': '식품의약품안전처 카페인 일일 섭취 기준 및 음료별 함량 분석'
    },
    {
        'id': 'alcohol',
        'file': 'alcohol.html',
        'badge': '간 건강 대사',
        'title': '위드마크(Widmark) 공식 기준 체내 알코올 분해 시간',
        'subtitle': '체중과 성별에 따른 간 알코올 대사 속도와 숙취 해독 팁',
        'steps': [
            {
                'step': '1단계',
                'time': '소주 1병 (360mL / 16.9도)',
                'items': ['남성(70kg): 약 4시간 10분', '여성(55kg): 약 6시간 00분'],
                'tip': '체중이 적고 체지방률이 높을수록 분해 시간 증가',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '캔맥주 2캔 (500mL × 2)',
                'items': ['남성(70kg): 약 2시간 40분', '여성(55kg): 약 3시간 50분'],
                'tip': '음주 후 수면 중에는 간 대사 속도가 느려질 수 있음',
                'color': (250, 204, 21)
            },
            {
                'step': '3단계',
                'time': '숙취 해독 3대 원칙',
                'items': ['충분한 수분과 전해질 공급', '당분 & 비타민B·C 섭취'],
                'tip': '사우나나 과도한 땀 배출은 탈수를 유발해 간에 치명적',
                'color': (52, 211, 153)
            }
        ],
        'caption': '도로교통공단 및 경찰청 공인 위드마크 알코올 분해 추정치'
    },
    {
        'id': 'supplement',
        'file': 'supplement.html',
        'badge': '영양제 안전 분석',
        'title': '주요 비타민 & 미네랄 일일 권장량(RDA) vs 상한선(UL)',
        'subtitle': '중복 복용으로 인한 과다증과 부작용을 예방하는 안전 기준',
        'steps': [
            {
                'step': '1단계',
                'time': '비타민 D',
                'items': ['권장: 400~1,000 IU', '상한선: 4,000 IU'],
                'tip': '지용성 비타민으로 장기 과다 복용 시 고칼슘혈증 주의',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '아연 (Zinc)',
                'items': ['권장: 8~10 mg', '상한선: 35 mg'],
                'tip': '종합비타민과 면역 단일제 중복 시 구리 결핍 위험',
                'color': (250, 204, 21)
            },
            {
                'step': '3단계',
                'time': '마그네슘 (보충제)',
                'items': ['권장: 300~350 mg', '상한선: 350 mg'],
                'tip': '음식 외 보충제 상한선 초과 시 삼투성 설사 유발',
                'color': (52, 211, 153)
            },
            {
                'step': '4단계',
                'time': '비타민 A',
                'items': ['권장: 700~800 μg RAE', '상한선: 3,000 μg RAE'],
                'tip': '지용성 축적으로 간 독성 우려, 베타카로틴 형태 권장',
                'color': (244, 63, 94)
            }
        ],
        'caption': '보건복지부 2020 한국인 영양소 섭취기준(KDRIs)'
    },
    {
        'id': 'checkup',
        'file': 'checkup.html',
        'badge': '검진 종합 판독',
        'title': '국가건강검진 4대 핵심 수치 정상·주의·위험 신호등 기준',
        'subtitle': '혈압, 공복 혈당, 간수치(AST·ALT), LDL 콜레스테롤 판독표',
        'steps': [
            {
                'step': '1단계',
                'time': '혈압 (수축기/이완기)',
                'items': ['정상: 120 / 80 mmHg 미만', '주의: 120~139 / 80~89'],
                'tip': '140/90 mmHg 이상 시 1기 고혈압 진료 권장',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '공복 혈당',
                'items': ['정상: 100 mg/dL 미만', '주의: 100~125 mg/dL'],
                'tip': '126 mg/dL 이상 시 당뇨병 정밀 검사 필수',
                'color': (52, 211, 153)
            },
            {
                'step': '3단계',
                'time': '간수치 (AST · ALT)',
                'items': ['정상: 40 IU/L 이하', '주의: 41~80 IU/L'],
                'tip': '80 IU/L 초과 시 지방간·간염 정밀 초음파 필요',
                'color': (250, 204, 21)
            },
            {
                'step': '4단계',
                'time': 'LDL 콜레스테롤',
                'items': ['정상: 100 mg/dL 미만', '경계: 130~159 mg/dL'],
                'tip': '160 mg/dL 이상 시 심혈관 위험 관리 요망',
                'color': (244, 63, 94)
            }
        ],
        'caption': '국민건강보험공단 일반건강검진 종합 판정 기준표'
    },
    {
        'id': 'quiz',
        'file': 'quiz.html',
        'badge': '셀프 케어 진단',
        'title': '건강노트 30초 라이프스타일 자가진단 & 1순위 케어 영역',
        'subtitle': '4가지 핵심 문항으로 내 몸의 불균형을 즉시 분석',
        'steps': [
            {
                'step': '1단계',
                'time': '활력 & 수면 영역',
                'items': ['기상 시 개운함 부족', '오후 3시 만성 피로감'],
                'tip': '수면 주기 개선과 비타민 B군·마그네슘 보충 처방',
                'color': (56, 189, 248)
            },
            {
                'step': '2단계',
                'time': '대사 & 식습관 영역',
                'items': ['식후 쏟아지는 극심한 졸음', '잦은 정제당·가공식품 섭취'],
                'tip': '식이섬유 우선 거꾸로 식사법과 혈당 스파이크 관리',
                'color': (250, 204, 21)
            },
            {
                'step': '3단계',
                'time': '운동 & 신체 활동',
                'items': ['주당 유산소 활동량 부족', '좌식 생활로 근력 저하'],
                'tip': '주 150분 중강도 유산소 및 주 2회 근력 운동 루틴 추천',
                'color': (52, 211, 153)
            }
        ],
        'caption': '건강노트 임상 연구 기반 1:1 라이프스타일 자가진단 리포트'
    }
]

# -------------------------------------------------------------------
# Execution: Generate Infographics and Inject into 11 HTML files
# -------------------------------------------------------------------
def run():
    print("=== 1. Generating Infographic Guide Images for 11 Tools ===")
    for info in INFOGRAPHICS:
        tid = info['id']
        out_img = f"images/tools/{tid}_guide.png"
        create_infographic(
            badge_text=info['badge'],
            title_text=info['title'],
            subtitle_text=info['subtitle'],
            steps=info['steps'],
            output_path=out_img
        )

    print("\n=== 2. Injecting Hero Previews & Infographics into 11 Tool Pages ===")
    for info in INFOGRAPHICS:
        html_file = info['file']
        tid = info['id']
        caption = info['caption']
        if not os.path.exists(html_file):
            continue

        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # A. Inject Hero Preview below subtitle if not already present
        hero_tag = f"""
        <div class="tool-preview-wrap" style="max-width:760px; margin:0 auto 28px; border-radius:16px; overflow:hidden; box-shadow:0 6px 20px rgba(0,0,0,0.06); border:1px solid #e2e8f0;">
          <img src="/images/thumbnails/banner_{tid}.jpg" alt="{info['title']}" style="width:100%; height:auto; aspect-ratio:16/9; object-fit:cover; display:block;">
        </div>"""

        if 'tool-preview-wrap' not in content:
            # find <p class="subtitle">...</p>
            sub_m = re.search(r'(<p class=[\'"]subtitle[\'"][^>]*>[\s\S]*?</p>)', content)
            if sub_m:
                content = content.replace(sub_m.group(1), sub_m.group(1) + hero_tag, 1)

        # B. Inject Infographic inside <article class="content-rich"> if not already present
        info_block = f"""
        <div class="content-img-wrap" style="margin:26px 0 32px; border-radius:14px; overflow:hidden; border:1px solid #e2e8f0; box-shadow:0 4px 14px rgba(0,0,0,0.04);">
          <img src="/images/tools/{tid}_guide.png" alt="{info['title']}" style="width:100%; height:auto; display:block;" loading="lazy">
          <div style="background:#f8fafc; padding:10px 16px; font-size:0.84rem; color:#64748b; text-align:center; border-top:1px solid #e2e8f0;">
            ▲ {caption}
          </div>
        </div>"""

        if f'{tid}_guide.png' not in content:
            # Inject after the first <h2> inside <article class="content-rich">
            art_m = re.search(r'(<article[^>]*class=[\'"][^\'"]*content-rich[^\'"]*[\'"][^>]*>[\s\S]*?)(<h2>[\s\S]*?</h2>)', content)
            if art_m:
                # insert after first h2 + its first paragraph
                h2_end = art_m.end()
                # find next </p> after h2
                next_p = content.find('</p>', h2_end)
                if next_p != -1:
                    insert_pos = next_p + 4
                    content = content[:insert_pos] + info_block + content[insert_pos:]
                else:
                    content = content[:h2_end] + info_block + content[h2_end:]

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {html_file} with Hero Preview & Infographic Guide!")

if __name__ == '__main__':
    run()

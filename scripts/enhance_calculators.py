import re
from pathlib import Path

REPO_DIR = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo")

# 1. Enhance bmi.html
bmi_path = REPO_DIR / "bmi.html"
bmi_content = bmi_path.read_text(encoding="utf-8-sig")

bmi_extra = """
        <h2>BMI와 함께 꼭 확인해야 할 '허리둘레'와 '마른 비만'</h2>
        <p>체질량지수(BMI)가 정상 범위(18.5~22.9)에 속하더라도 안심할 수 없는 경우가 바로 <strong>'마른 비만(정상 체중 비만)'</strong>입니다. 근육량이 적고 내장지방이 복부에 집중된 경우, 겉보기에는 날씬해 보여도 고혈압, 당뇨병, 고지혈증 등 대사증후군 위험이 비만 환자만큼 높습니다.</p>
        <table>
          <thead>
            <tr>
              <th>구분</th>
              <th>대한비만학회 복부비만 기준</th>
              <th>건강 관리 권장 사항</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>성인 남성</strong></td>
              <td>허리둘레 <strong>90cm (약 35.4인치)</strong> 이상</td>
              <td>내장지방 감량을 위한 유산소 운동 및 복합 탄수화물 섭취</td>
            </tr>
            <tr>
              <td><strong>성인 여성</strong></td>
              <td>허리둘레 <strong>85cm (약 33.5인치)</strong> 이상</td>
              <td>하체 근력 운동 병행 및 충분한 단백질 섭취</td>
            </tr>
          </tbody>
        </table>

        <h2>자주 묻는 질문 (FAQ)</h2>
        <div style="display:flex; flex-direction:column; gap:14px; margin-top:16px;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 근력 운동을 많이 해서 체중이 많이 나가는데 비만인가요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 아닙니다. BMI는 체지방과 근육을 구별하지 못합니다. 골격근량이 많은 분은 체지방률이 10~15%로 매우 낮아도 과체중이나 비만으로 계산될 수 있으므로 인바디(체성분 검사) 결과를 우선해야 합니다.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 다이어트할 때 매일 아침 체중계에 올라가야 하나요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 체중은 수분 섭취량, 염분 섭취, 수면 상태에 따라 하루 1~2kg씩 자연스럽게 요동칩니다. 매일의 숫자에 일희일비하기보다는 주 1회 일정한 조건(기상 후 공복)에서 측정하는 것을 권장합니다.</p>
          </div>
        </div>

        <h3 style="margin-top:35px;">함께 읽으면 좋은 추천 건강 가이드</h3>
        <ul>
          <li><a href="/health/blood-pressure-stages-hypertension-diet/">고혈압 전단계 수치 기준과 낮추는 법, DASH 식단 가이드</a></li>
          <li><a href="/health/다이어트를-하는-분들이-매일-아침-오르는-체중계의/">다이어트 중 매일 아침 체중계 숫자가 흔들리는 과학적 이유</a></li>
          <li><a href="/calorie">하루 필요 칼로리(TDEE) 및 감량 목표 칼로리 계산기</a></li>
        </ul>
"""

if "<h2>BMI의 한계</h2>" in bmi_content:
    parts = bmi_content.split("<h2>BMI의 한계</h2>")
    # insert before disclaimer
    disc_marker = '<p style="background:#f8f9fa; border-radius:14px;'
    sub_parts = parts[1].split(disc_marker)
    new_bmi = parts[0] + "<h2>BMI의 한계</h2>" + sub_parts[0] + bmi_extra + "\n" + disc_marker + sub_parts[1]
    bmi_path.write_text(new_bmi, encoding="utf-8")
    print("Enhanced bmi.html")


# 2. Enhance calorie.html
cal_path = REPO_DIR / "calorie.html"
cal_content = cal_path.read_text(encoding="utf-8-sig")

cal_extra = """
        <h2>기초대사량(BMR) 이하로 굶으면 살이 더 안 빠지는 이유</h2>
        <p>빠른 체중 감량을 위해 하루 800~1,000kcal 이하로 극단적인 절식을 하는 분들이 많습니다. 하지만 기초대사량보다 적게 먹으면 신체는 '기아 상태'로 인식하여 생존 모드에 돌입합니다.</p>
        <ul>
          <li><strong>갑상선 호르몬 감소 및 대사 저하:</strong> 체온 유지와 심장 박동 등 생명 유지 에너지를 스스로 20~30% 줄여버립니다.</li>
          <li><strong>근육 분해(근손실):</strong> 부족한 에너지를 보충하기 위해 지방보다 소모가 빠른 골격근 단백질을 분해해 에너지로 씁니다. 근육이 줄어들면 기초대사량이 더 낮아지는 악순환이 발생합니다.</li>
          <li><strong>요요 현상:</strong> 절식을 중단하고 일반 식사로 돌아왔을 때, 낮아진 대사율 때문에 이전보다 훨씬 적게 먹어도 남은 에너지가 전부 체지방으로 축적됩니다.</li>
        </ul>

        <h2>자주 묻는 질문 (FAQ)</h2>
        <div style="display:flex; flex-direction:column; gap:14px; margin-top:16px;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 다이어트 정체기가 왔을 때는 어떻게 해야 하나요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 체중이 줄어들면 줄어든 체중에 맞춰 TDEE도 감소합니다. 따라서 3~5kg 감량할 때마다 칼로리 계산기로 권장 칼로리를 재산출하고, 단백질 비율을 높이거나 유산소 운동 대신 근력 운동 비중을 늘려 대사를 자극해야 합니다.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 하루 500kcal 적자(Deficit)가 가장 이상적인가요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 네. 지방 1kg을 연소하는 데 약 7,700kcal가 필요합니다. 하루 500kcal씩 섭취를 줄이거나 운동으로 소모하면 1주일에 약 3,500kcal(체지방 약 0.45kg)를 안전하게 감량할 수 있어 근손실과 요요가 거의 없습니다.</p>
          </div>
        </div>

        <h3 style="margin-top:35px;">함께 읽으면 좋은 추천 건강 가이드</h3>
        <ul>
          <li><a href="/health/blood-sugar-spike-prevention-diet/">식후 혈당 스파이크 증상과 낮추는 법, 거꾸로 식사법</a></li>
          <li><a href="/health/fatty-liver-foods-diet/">지방간에 좋은 음식과 피해야 할 음식, 식단 가이드</a></li>
          <li><a href="/protein">체중과 운동량에 맞는 단백질 섭취량 계산기</a></li>
        </ul>
"""

if '<p style="background:#f8f9fa;' in cal_content:
    parts = cal_content.split('<p style="background:#f8f9fa;')
    new_cal = parts[0] + cal_extra + '\n<p style="background:#f8f9fa;' + parts[1]
    cal_path.write_text(new_cal, encoding="utf-8")
    print("Enhanced calorie.html")


# 3. Enhance protein.html
prot_path = REPO_DIR / "protein.html"
prot_content = prot_path.read_text(encoding="utf-8-sig")

prot_extra = """
        <h2>단백질 섭취의 3대 골든 룰</h2>
        <ol>
          <li><strong>끼니당 25~35g 분할 섭취:</strong> 우리 몸이 한 번의 식사에서 근육 합성에 효율적으로 사용할 수 있는 단백질 양은 약 20~40g(달걀 3~4개 또는 닭가슴살 1~1.5덩이) 수준입니다. 한 끼에 몰아서 100g을 먹으면 남은 단백질은 체지방으로 축적되거나 신장을 거쳐 배출됩니다.</li>
          <li><strong>충분한 수분 섭취 필수:</strong> 단백질 대사 과정에서 암모니아가 생성되며, 이는 간에서 요소로 전환되어 소변으로 배출됩니다. 고단백 식단을 유지할 때는 평소보다 물을 500ml 이상 더 마셔야 신장 부담을 예방할 수 있습니다. <a href="/water">물 섭취량 계산기</a>를 활용해 보세요.</li>
          <li><strong>운동 후 1~2시간 이내 보충:</strong> 근력 운동 후 1~2시간은 근육 합성이 가장 활발한 시간대입니다. 단백질과 약간의 탄수화물을 함께 섭취하면 인슐린이 분비되어 아미노산이 근육으로 신속하게 흡수됩니다.</li>
        </ol>

        <h2>자주 묻는 질문 (FAQ)</h2>
        <div style="display:flex; flex-direction:column; gap:14px; margin-top:16px;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 단백질 보충제(웨이 프로틴)를 꼭 먹어야 하나요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 일반 식사(달걀, 닭가슴살, 생선, 두부, 고기)로 하루 목표량을 채울 수 있다면 굳이 보충제를 먹지 않아도 됩니다. 보충제는 바쁜 일상에서 간편하게 부족분을 채우는 보조 수단입니다.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 노년층도 단백질을 많이 먹어야 하나요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 네, 오히려 더 적극적으로 챙겨야 합니다. 나이가 들수록 근단백질 합성 능력이 떨어지는 '동화 저항성'이 발생하므로, 노년기 근감소증(사코페니아)과 낙상 예방을 위해 체중 1kg당 1.2g 이상의 단백질 섭취가 권장됩니다.</p>
          </div>
        </div>

        <h3 style="margin-top:35px;">함께 읽으면 좋은 추천 건강 가이드</h3>
        <ul>
          <li><a href="/health/근육-유지와-다이어트를-위해-단백질-섭취의-중요성/">근육 유지와 다이어트를 위한 단백질 섭취의 중요성</a></li>
          <li><a href="/health/vitamin-d-benefits-daily-intake-timing/">비타민D 복용시간과 하루 권장량, 마그네슘 결합 가이드</a></li>
          <li><a href="/calorie">하루 칼로리(TDEE) 및 기초대사량 계산기</a></li>
        </ul>
"""

if '<p style="background:#f8f9fa;' in prot_content:
    parts = prot_content.split('<p style="background:#f8f9fa;')
    new_prot = parts[0] + prot_extra + '\n<p style="background:#f8f9fa;' + parts[1]
    prot_path.write_text(new_prot, encoding="utf-8")
    print("Enhanced protein.html")


# 4. Enhance water.html
water_path = REPO_DIR / "water.html"
water_content = water_path.read_text(encoding="utf-8-sig")

water_extra = """
        <h2>물을 마시는 하루 4대 골든타임</h2>
        <ul>
          <li><strong>기상 직후 미온수 1잔 (300ml):</strong> 수면 중 호흡과 땀으로 손실된 수분을 보충하고, 끈적해진 혈액의 점도를 낮추며 위장 운동을 깨웁니다.</li>
          <li><strong>식사 30분 전 1잔:</strong> 소화액 분비를 촉진하고 과식을 자연스럽게 예방합니다. 단, 식사 도중이나 직후 과도한 물 섭취는 소화 효소를 희석할 수 있으니 한두 모금만 드시는 것이 좋습니다.</li>
          <li><strong>나른한 오후 3시 1잔:</strong> 가벼운 탈수는 피로와 집중력 저하의 주요 원인입니다. 커피 대신 시원한 물 한 잔이 뇌 활동을 깨웁니다.</li>
          <li><strong>취침 1시간 전 반 잔:</strong> 수면 중 혈액 응고를 예방합니다. 단, 잠들기 직전 과도하게 마시면 야간뇨로 숙면을 방해할 수 있으니 가볍게 적셔줍니다.</li>
        </ul>

        <h2>자주 묻는 질문 (FAQ)</h2>
        <div style="display:flex; flex-direction:column; gap:14px; margin-top:16px;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 커피나 녹차로 하루 물 섭취량을 채워도 되나요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 카페인은 이뇨 작용을 촉진하여 마신 양보다 약 1.5배의 수분을 소변으로 배출시킵니다. 커피를 한 잔 마셨다면 그만큼 맹물 한 잔을 추가로 마셔주는 것이 이상적입니다. 보리차나 현미차 같은 곡물차는 생수 대체가 가능합니다.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 물을 너무 많이 마시면 안 좋은 점이 있나요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 짧은 시간(1~2시간) 내에 2~3L 이상의 물을 급격히 마시면 혈액 속 나트륨 농도가 비정상적으로 희석되는 '저나트륨혈증(물 중독)'이 올 수 있습니다. 두통, 메스꺼움, 부종이 발생할 수 있으므로 하루 동안 시간 간격을 두고 천천히 나누어 마셔야 합니다.</p>
          </div>
        </div>

        <h3 style="margin-top:35px;">함께 읽으면 좋은 추천 건강 가이드</h3>
        <ul>
          <li><a href="/health/하루-물-섭취량/">하루 물 섭취량 계산법: 혈액 순환과 노폐물 배출 가이드</a></li>
          <li><a href="/health/blood-pressure-stages-hypertension-diet/">고혈압 전단계 수치 기준과 나트륨 배출 DASH 식단</a></li>
          <li><a href="/health/하루-카페인-권장량/">하루 카페인 권장량과 커피가 수분 대사에 미치는 영향</a></li>
        </ul>
"""

if '<p style="background:#f8f9fa;' in water_content:
    parts = water_content.split('<p style="background:#f8f9fa;')
    new_water = parts[0] + water_extra + '\n<p style="background:#f8f9fa;' + parts[1]
    water_path.write_text(new_water, encoding="utf-8")
    print("Enhanced water.html")


# 5. Enhance supplement.html
supp_path = REPO_DIR / "supplement.html"
supp_content = supp_path.read_text(encoding="utf-8-sig")

supp_extra = """
        <h2>영양제 시너지 궁합 vs 피해야 할 상극 조합</h2>
        <table>
          <thead>
            <tr>
              <th>구분</th>
              <th>영양제 조합</th>
              <th>상호작용 원리 및 복용 팁</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="color:#007bff; font-weight:700;">추천 시너지</td>
              <td><strong>비타민 D + 마그네슘</strong></td>
              <td>마그네슘은 비타민D를 체내 활성형으로 변환하는 필수 효소를 활성화함</td>
            </tr>
            <tr>
              <td style="color:#007bff; font-weight:700;">추천 시너지</td>
              <td><strong>철분 + 비타민 C</strong></td>
              <td>비타민C의 산성 환경이 난흡수성 철분을 2가 철(Fe2+)로 환원시켜 흡수율 극대화</td>
            </tr>
            <tr>
              <td style="color:#e74c3c; font-weight:700;">주의 조합</td>
              <td><strong>칼슘 vs 철분</strong></td>
              <td>동일한 장내 수송 통로(DMT1)를 공유하여 서로의 흡수를 강력히 방해 (최소 2시간 간격 복용)</td>
            </tr>
            <tr>
              <td style="color:#e74c3c; font-weight:700;">주의 조합</td>
              <td><strong>종합비타민 + 단일 미네랄</strong></td>
              <td>이미 종합비타민에 포함된 아연, 비타민A 등이 중복되어 일일 상한량을 초과할 위험</td>
            </tr>
          </tbody>
        </table>

        <h2>자주 묻는 질문 (FAQ)</h2>
        <div style="display:flex; flex-direction:column; gap:14px; margin-top:16px;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 영양제는 식전과 식후 중 언제 먹어야 하나요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 수용성 비타민(비타민B군, C)이나 유산균은 흡수율을 위해 아침 공복에 물과 함께 복용하는 것이 좋습니다. 반면 지용성 비타민(A, D, E, K), 오메가3, 루테인은 식사 중 분비되는 담즙산과 지방이 있어야 흡수되므로 반드시 식사 직후 복용해야 합니다.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px 20px;">
            <h4 style="margin:0 0 6px; color:#1e293b;">Q. 비타민C 메가도스(하루 6,000mg 이상)는 안전한가요?</h4>
            <p style="margin:0; font-size:0.92rem; color:#475569; line-height:1.6;">A. 비타민C는 수용성이라 남는 양이 배출되지만, 과도한 고용량 복용 시 삼투성 설사, 복통, 그리고 대사산물인 옥살산염으로 인한 신장 결석 위험이 증가할 수 있습니다. 성인 일일 상한섭취량은 2,000mg입니다.</p>
          </div>
        </div>

        <h3 style="margin-top:35px;">함께 읽으면 좋은 추천 건강 가이드</h3>
        <ul>
          <li><a href="/health/vitamin-d-benefits-daily-intake-timing/">비타민D 복용시간과 하루 권장량, 마그네슘 시너지</a></li>
          <li><a href="/health/iron-anemia-side-effects/">철분제 복용법과 부작용, 변비·위장장애 줄이는 법</a></li>
          <li><a href="/health/오메가3/">오메가3 복용시간과 EPA·DHA 하루 섭취량, rTG 고르는 법</a></li>
        </ul>
"""

if '<p style="background:#f8f9fa;' in supp_content:
    parts = supp_content.split('<p style="background:#f8f9fa;')
    new_supp = parts[0] + supp_extra + '\n<p style="background:#f8f9fa;' + parts[1]
    supp_path.write_text(new_supp, encoding="utf-8")
    print("Enhanced supplement.html")

# 6. Update privacy.html date to today
privacy_path = REPO_DIR / "privacy.html"
privacy_content = privacy_path.read_text(encoding="utf-8-sig")
privacy_content = privacy_content.replace("2026년 5월 31일", "2026년 10월 5일")
privacy_path.write_text(privacy_content, encoding="utf-8")
print("Updated privacy.html date to 2026년 10월 5일")

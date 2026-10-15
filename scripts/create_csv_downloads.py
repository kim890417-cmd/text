import csv
from pathlib import Path

csv1 = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo\downloads\note-nutrition-facts-sugar-serving-size-calculation.csv")
csv2 = Path(r"C:\Users\sadase\Desktop\키워드 글쓰기\healthfit_repo\downloads\note-caffeine-daily-intake-drinks-record-method.csv")

csv1.parent.mkdir(parents=True, exist_ok=True)

with open(csv1, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["날짜", "제품명·종류", "표시 기준량(g)", "표시 당류(g)", "총내용량(g)", "실제 먹은 양 기준 당류(g)", "비용·식비 체감"])
    for _ in range(7):
        writer.writerow(["", "", "", "", "", "", ""])

with open(csv2, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["날짜", "음료 종류·제품명", "용량(ml)", "카페인 함량(mg)", "마신 시각", "하루 누적 합계(mg)", "수면·취침 영향 체감"])
    for _ in range(7):
        writer.writerow(["", "", "", "", "", "", ""])

print("CSVs generated successfully!")

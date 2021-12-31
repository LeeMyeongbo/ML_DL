import codecs

# 데이터 변수 선언
filename = "test_02.csv"
csv = codecs.open(filename, "r", "utf-8").read()

# CSV을 파이썬 리스트로 변환
data = []
rows = csv.split("\r\n")  # 레코드 구분 줄바꿈 (\r\n이 줄바꿈 기호)
for row in rows:
    if row == "":
        continue
    cells = row.split(",")  # 필드 데이터 구분
    data.append(cells)

# 결과 출력
for c in data:
    print(c[1], c[2])

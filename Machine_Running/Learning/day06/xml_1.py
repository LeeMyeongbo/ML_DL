from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"

# Web 데이터 다운로드 후 파일 저장
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# Web 데이터 분석
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

# Web 데이터 정보 추출
info = {}  # 비어있는 딕셔너리 생성
for location in soup.find_all("location"):
    name = location.find('city').string
    weather = location.find('wf').string
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)

# 각 지역의 날씨 구분해서 출력
for weather in info.keys():
    print("+", weather)
    for name in info[weather]:
        print("| - ", name)

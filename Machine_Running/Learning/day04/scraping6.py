from bs4 import BeautifulSoup
import urllib.request as req

# HTML 가져오기
url = "https://www.naver.com"
res = req.urlopen(url)
# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
# 원하는 데이터 추출
logo = soup.select_one("div#PM_ID_ct.wrap>div.header>div.special_bg>div.area_flex>div.area_logo>h1>a>span.naver_logo").string
print("logo =", logo)

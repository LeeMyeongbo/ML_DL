import requests
from bs4 import BeautifulSoup

USER = 'myeongbo123'
PASS = '432513'
login_info = {"m_id": USER, "m_passwd": PASS}

# 모듈 객체 생성 및 선언
# 세션 시작
session = requests.session()

# 로그인 페이지 접근
url_login = "https://www.hanbit.co.kr/member/login_proc.php"  # 보통 로그인 화면은 php 또는 jsp로 함
res = session.post(url_login, data=login_info)
res.raise_for_status()

# 마이페이지 접근
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 웹페이지에서 데이터 추출
soup = BeautifulSoup(res.text, "html.parser")

miliage = soup.select_one('div#container>div.myhanbit_wrap>div.sm_mymileage>dl.mileage_section1>dd>span').get_text()
ecoin = soup.select_one('div#container>div.myhanbit_wrap>div.sm_mymileage>dl.mileage_section2>dd>span').get_text()
print('마일리지 :', miliage)
print('e코인 :', ecoin)

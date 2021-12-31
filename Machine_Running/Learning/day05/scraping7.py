from selenium import webdriver  # 모듈 로딩

# 크롬 브라우저 제어 드라이버 생성
driver = webdriver.Chrome('C:/Users/Administrator/PycharmProjects/chromedriver.exe')

# 크롬 브라우저 드라이버를 활용한 웹 페이지 제어
# 웹 사이트 가져오기
driver.get('http://www.naver.com')

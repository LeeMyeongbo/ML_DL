from selenium import webdriver

# 크롬 브라우저 제어 드라이버 생성
driver = webdriver.Chrome('C:/Users/Administrator/PycharmProjects/chromedriver.exe')

# 크롬 브라우저 드라이버를 활용한 웹페이지 제어
driver.get('http://www.naver.com')

# 웹페이지 특정 요소에 접근 후 값 전송
driver.find_element_by_xpath('//*[@id="query"]').send_keys('안녕하세요.')
# 3초 대기
driver.implicitly_wait(3)
# 웹 사이트의 특정 요소에 접근 후 동작 제어어
driver.find_element_by_xpath('//*[@id="search_btn"]').click()

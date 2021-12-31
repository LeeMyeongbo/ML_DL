from selenium import webdriver

# 크롬 브라우저 제어 드라이버 생성
print('페이지 이동중...')
driver = webdriver.Chrome('C:/Users/Administrator/PycharmProjects/chromedriver.exe')

# 웹 브라우저 접근 후 제어
driver.get('http://www.naver.com')
driver.implicitly_wait(3)  # 3초 대기
driver.save_screenshot("Website.png")  # 화면 캡쳐 및 저장
driver.find_element_by_xpath('//*[@id="PM_ID_themecastBody"]/div/div/div/ul/li[10]').click()


from selenium import webdriver

print("로그인 페이지로 이동합니다..")
driver = webdriver.Chrome('C:/Users/Administrator/PycharmProjects/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('http://www.naver.com')
ID = 'myeongbo123'
PW = '1234958'
driver.save_screenshot('naver.png')

driver.find_element_by_xpath('//*[@id="account"]/div/a').click()
driver.find_element_by_xpath('//*[@id="id"]').send_keys(ID)
driver.find_element_by_xpath('//*[@id="pw"]').send_keys(PW)
driver.save_screenshot('naver1.png')
driver.find_element_by_xpath('//*[@id="log.login"]').click()

driver.implicitly_wait(3)
driver.save_screenshot('naver2.png')

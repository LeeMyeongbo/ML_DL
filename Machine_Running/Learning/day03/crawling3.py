import urllib.request
import urllib.parse

API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

# 매개변수 url 인코딩
values = {'stnld': '108'}  # 지역번호
print(type(values))

params = urllib.parse.urlencode(values)  # 키=값 형태로 인코딩

# 요청 전용 url 생성
url = API + "?" + params
print("url=", url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)

with open('text3.txt', mode='w', encoding='utf-8') as file:
    file.write(text)
    print('저장 완료')


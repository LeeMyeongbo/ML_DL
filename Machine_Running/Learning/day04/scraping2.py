from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html>
    <body>
      <h1>스크레이핑이란?</h1>
      <p>웹 페이지를 분석하는 것</p>
      <p>원하는 부분을 추출하는 것</p>
    </body>
</html>
"""  # 이거도 하나의 문자열이 됨!!


soup = BeautifulSoup(html, 'html.parser')  # html 분석 객체 생성

# 원하는 부분 추출
h1 = soup.html.body.h1
print(h1.string)
p1 = soup.html.body.p
print(p1.string)
p2 = p1.next_sibling.next_sibling
print(p2.string)

from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html>
    <body>
      <h1 id="main">스크레이핑이란?</h1>
      <p id="sub1">웹 페이지를 분석하는 것</p>
      <p id="sub2">원하는 부분을 추출하는 것</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')  # html 분석 객체 생성

# id를 이용하여 원하는 부분 추출
main = soup.find(id="main")
sub1 = soup.find(id="sub1")
sub2 = soup.find(id="sub2")
print('main =', main.string)
print('sub1 =', sub1.string)
print('sub2 =', sub2.string)

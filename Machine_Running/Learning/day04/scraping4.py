from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
      <li><a href="http://www.naver.com">naver</a></li>
      <li><a href="http://wwww.daum.net">daum</a></li>
    </ul>
</body></html>
"""
# html 분석
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all("a")  # find_all() 여러 개 요소 검출
# 링크 목록 출력
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)

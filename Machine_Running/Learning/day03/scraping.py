from bs4 import BeautifulSoup

fp = open("Test4.html", encoding="utf-8")  # html 파일 열기
soup = BeautifulSoup(fp, "html.parser")  # 스크래핑 객체 생성 (html 파일이므로 html 파서 이용)

sel = lambda q: print(soup.select_one(q).string)  # 람다 표현
sel("#nu")  # 항상 아이디 앞에선 #을 붙여야 함!
sel("li#nu")  # li 중에서 아이디가 nu인 놈
sel("ul > li#nu")  # '>' : 자식을 가리킬 때 사용
sel("#bible #nu")
sel("#bible > #nu")
sel("ul#bible > li#nu")
sel("li[id='nu']")
sel("li:nth-of-type(4)")

print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)

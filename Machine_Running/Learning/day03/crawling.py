import urllib.request
# URL 경로 지정과 png 파일 이름 설정
url = "http://uta.pw/shodou/img/28/214.png"
name = 'test.png'

# 다운로드
mem = urllib.request.urlopen(url).read()

# 바이너리 모드로 파일 open & write
with open(name, mode='wb') as file:
    file.write(mem)
    print('저장되었습니다.')

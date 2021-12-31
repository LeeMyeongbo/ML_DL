import urllib.request

# 데이터 읽어 들이기
url = 'http://api.aoikujira.com/ip/ini'
res = urllib.request.urlopen(url)
data = res.read()  # 바이트 데이터 읽어오기
print('type(data) =', type(data))  # 타입 체크

# 바이너리를 문자열로 변환
text = data.decode('utf-8')  # utf-8로 디코딩
print(text)

# 데이터를 다시 파일로 저장
with open('test2.txt', mode='w', encoding='utf-8') as file:
    file.write(text)
    print('저장완료')

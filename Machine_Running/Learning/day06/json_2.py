import json

# 변수 선언
data = {
    'data': '2020-01-13',
    'price': {
        'apple': 1300,
        'pineapple': 2000,
        'grape': 1900
    }
}

savename = "jdata.json"

# JSON 형식으로 저장
jdata = json.dumps(data)

# JSOn 파일 생성
with open(savename, mode='w', encoding='utf-8') as file:
    file.write(jdata)

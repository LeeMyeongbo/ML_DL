import urllib.request as req
import os.path
import json

# 변수 선언
url = "https://api.github.com/repositories"
savename = "repo.json"

# Web 데이터 json 파일 다운로드
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# JSON 파일 분석
s = open(savename, "r", encoding="utf-8").read()
items = json.loads(s)
i = 1

# JSON 파일 출력
for item in items:
    print(str(i) + ' - ①. name : ' + item["name"] + ", " + 'login = ' + item["owner"]["login"])
    print(str(i) + ' - ②. full name : ' + item["full_name"] + ", " + 'node_ID : ' + item["owner"]["node_id"])
    i = i + 1

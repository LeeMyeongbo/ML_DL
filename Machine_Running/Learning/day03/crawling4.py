import sys
import urllib.request as req
import urllib.parse as pa

if len(sys.argv) <= 1:
    sys.exit()
regionNumber = sys.argv[1]

API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
values = {'stnld': regionNumber}
params = pa.urlencode(values)
url = API + "?" + params
print("url=", url)

data = req.urlopen(url).read()
text = data.decode('utf-8')
print(text)

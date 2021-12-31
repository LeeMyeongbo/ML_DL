import urllib.request as req
import gzip, os, os.path

savepath = 'C:/Users/Administrator/PycharmProjects/day08/handwritings'
baseurl = 'http://yann.lecun.com/exdb/mnist/'
files = ['train-images-idx3-ubyte.gz', 'train-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz', 't10k-labels-idx1-ubyte.gz']

# 다운로드
if not os.path.exists(savepath):
    os.mkdir(savepath)  # 디렉토리가 존재하지 않는다면 생성
for f in files:  # files 리스트에 각각 요소에 대해 반복
    url = baseurl + f
    loc = savepath + '/' + f
    print("download :", url)
    if not os.path.exists(loc):  # 링크가 존재하지 않는다면
        req.urlretrieve(url, loc)

# Gzip 압축 해제
for f in files:
    gz_file = savepath + '/' + f
    raw_file = savepath + '/' + f.replace(".gz", "")
    print("gzip :", f)
    with gzip.open(gz_file, "rb") as fp:  # b가 붙어야지 바이너리 (b 안 붙으면 텍스트)
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)
print("ok")

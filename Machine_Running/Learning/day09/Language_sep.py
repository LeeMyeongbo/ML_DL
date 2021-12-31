from sklearn import svm, metrics
import glob
import os.path, re, json


# 텍스트 중 알파벳 출현 빈도 조사 함수
def check_freq(fname):
    name = os.path.basename(fname)  # 파일 이름만 반환
    print('name => {}'.format(name))

    # 파일이름 앞에 알파벳 2개 시작 파일 체크
    lang = re.match(r'^[a-z]{2,}', name).group()  # 매치된 문자열 반환
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.lower()  # 소문자 변환
    # 숫자 세기 변수 초기화
    cnt = [0 for n in range(0, 26)]  # 알파벳 26개 리스트 생성
    code_a = ord("a")  # 'a'의 코드값 반환
    code_z = ord("z")  # 'z'의 코드값 반환
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z:
            cnt[n - code_a] += 1

    # 출현 빈도로 변환
    total = sum(cnt)
    freq = list(map(lambda n: n / total, cnt))
    return (freq, lang)


# 파일 로딩 가능
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    print("file list = {}".format(file_list))

    for fname in file_list:
        print('fname => {}'.format(fname))
        r = check_freq(fname)  # 파일변 알파벳 출현빈도 체크
        print('r => {}'.format(r))
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs": freqs, "labels": labels}


data = load_files("./Languages/train/*.txt")
test = load_files("./Languages/test/*.txt")
# JSON으로 결과 저장
with open("Languages/freq.json", 'w', encoding='utf-8') as fp:
    json.dump([data, test], fp)

# 학습 및 예측
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])
predict = clf.predict(test["freqs"])

# 결과
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)

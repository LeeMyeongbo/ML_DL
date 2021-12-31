from sklearn.model_selection import train_test_split
from sklearn import datasets, svm, metrics
from sklearn.metrics import accuracy_score
import cv2
from sklearn.externals import joblib

def predict_digit(filename):
    _clf = joblib.load("digits.pkl")  # 학습한 데이터 읽어 들이기
    my_img = cv2.imread(filename)  # 직접 그린 손글씨 이미지 읽어 들이기
    my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)  # 이미지 데이터를 학습에 적합하게 변환
    my_img = cv2.resize(my_img, (8, 8))
    my_img = 15 - my_img // 16  # 흑백 반전
    my_img = my_img.reshape((-1, 64))
    res = _clf.predict(my_img)
    return res[0]

# 데이터 읽기
digits = datasets.load_digits()
print("type(digits) =>", type(digits))
print("digits =>", digits)

x = digits.images
y = digits.target
x = x.reshape((-1, 64))  # 2차원 배열을 1차원 배열로 변환

# 데이터를 학습 전용과 테스트 전용으로 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 데이터 학습
clf = svm.LinearSVC()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

# 학습 데이터 저장
joblib.dump(clf, 'digits.pkl')

# 이미지 파일을 지정해서 실행
n = predict_digit('./IMAGE/my2.png')
print("my2.png =", str(n))

n = predict_digit('./IMAGE/mynum.png')
print("mynum.png =", str(n))

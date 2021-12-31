import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 붓꽃 CSV 데이터 수집
csv = pd.read_csv('iris.csv')

# 필요한 데이터(column) 추출
csv_data = csv[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
csv_label = csv["species"]

# 학습 데이터와 테스트 전용 데이터 분류
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

# 데이터 학습 & 예측
clf = svm.SVC()
clf.fit(train_data, train_label)  # 학습
pre = clf.predict(test_data)

# 정확도 검사
ac_score = metrics.accuracy_score(test_label, pre)
print("정답률 =", ac_score)

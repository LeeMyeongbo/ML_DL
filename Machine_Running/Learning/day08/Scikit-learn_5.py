import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# 데이터 읽어 들이기
wine = pd.read_csv("winequality-white.csv", sep=";", encoding="utf-8")

# 데이터를 레이블과 데이터로 분리
y = wine["quality"]  # 답
x = wine.drop("quality", axis=1)  # 문제

# 학습 전용과 테스트 전용으로 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

print("학습시킨 데이터 \n", x_train)
print("학습시킨 데이터의 답 \n", y_train)
print("시험할 데이터 \n",  x_test)
print("시험할 데이터의 답 \n", y_test)

# 학습하기
model = RandomForestClassifier()
model.fit(x_train, y_train)

# 평가하기
y_pred = model.predict(x_test)
print("시험 데이터를 통해 도출해낸 답 \n", y_pred)
print(classification_report(y_test, y_pred))
print("정답률 =", accuracy_score(y_test, y_pred))

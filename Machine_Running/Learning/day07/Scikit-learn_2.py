import pandas as pd
from sklearn import svm, metrics

# XOR 계산 결과 데이터
xor_input = [
    [0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:, 0:1]
xor_label = xor_df.ix[:, 2]
print(xor_data)
print(xor_label)

# 데이터 학습과 예측
clf =svm.SVC()
clf.fit(xor_data, xor_label)  # 학습
pre = clf.predict(xor_data)  # 예측

# 정답 추출
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 =", ac_score)

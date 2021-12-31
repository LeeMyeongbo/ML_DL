from sklearn import datasets
import matplotlib.pyplot as plt

# 손글씨 데이터 읽어오기
digits = datasets.load_digits()

# 숫자 0 이미지 및 값 확인
digit0 = digits.images[0]
plt.imshow(digit0, cmap="gray")
plt.show()
print(digit0)

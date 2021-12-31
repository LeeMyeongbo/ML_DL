import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

# 데이터 변수 선언
DEBUG = True

# 데이터 준비 및 노드 준비
iris_data = pd.read_csv('./iris.csv', encoding='utf-8')
y_labels = iris_data.iloc[1:, -1]  # iris name 라벨
x_datas = iris_data.iloc[1:, :-1]  # iris별 4가지 구분 데이터
if DEBUG:
    print(iris_data)
    print('y_labels ==============================================\n', y_labels)
    print('x_datas ==============================================\n', x_datas)
labels = {'setosa': [1., 0., 0.], 'versicolor': [0., 0., 0.], 'virginica': [0., 0., 1.]}

# One-Hot Encoding 데이터 생성
y_nums = list(map(lambda v: labels[v], y_labels))
if DEBUG:
    print('y_nums ==============================================\n', y_nums)

# 학습 & 테스트 데이터 생성
x_train, x_test, y_train, y_test = train_test_split(x_datas, y_nums, train_size=0.8)

# 연산 노드 생성
x = tf.placeholder(tf.float32, [None, 4])  # iris 속성 4개 입력값 저장
y_ = tf.placeholder(tf.float32, [None, 3])  # 정답 레이블 입력 공간
w = tf.Variable(tf.zeros([4, 3]))  # 가중치
b = tf.Variable(tf.zeros([3]))  # 바이어소스

# 손실 함수 정의
y = tf.nn.softmax(tf.matmul(x, w) + b)  # softmax를 거쳐 출력된 예측값

# 실제값과 예측값 오차 계산, W, b 업데이트
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(cross_entropy)

# 검사
predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))  # 예측값과 실제값 검사
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

# 세션 생성
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

train_feed_dict = {x: x_train, y_: y_train}
for step in range(300):
    sess.run(train, feed_dict=train_feed_dict)
acc = sess.run(accuracy, feed_dict={x: x_test, y_: y_test})
print('accuracy =>', acc)

from keras.models import load_model
import numpy as np
import cv2 as cv
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 학습이 완료된 모델을 불러온다.
mlp_model = load_model('./mnist_mlp_model.h5')
cnn_model = load_model('./mnist_cnn_model.h5')
size = 28


# 입력(글씨체 이미지)을 학습 모델에 통과시켜 예측값과 그 확률을 반환
def predict_num_by_MLP(img):
    img = cv.resize(img, (size, size))
    img = img.reshape(1, 784).astype('float')
    img = img / 255
    p = mlp_model.predict(img, verbose=0)
    max_prob = max(p[0])
    if max_prob > .10:
        return p.argmax(axis=-1), round(max_prob * 100, 2)
    return "none", 0


def predict_num_by_CNN(img):
    img = cv.resize(img, (size, size))
    img = img.reshape(1, size, size, 1)
    img = img / 255
    p = cnn_model.predict(img, verbose=0)
    max_prob = max(p[0])
    if max_prob > .10:
        return p.argmax(axis=-1), round(max_prob * 100, 2)
    return "none", 0


test_img = cv.imread('./test.jpg', 0)
font_shape = cv.FONT_HERSHEY_SIMPLEX
font_org = (0, 40)
font_color = (255, 255, 255)
font_size = 1
font_thickness = 2

# 함수가 반환한 결과 값(match)과 확률(prob)을 반환 (입력한 글씨체가 match 일 확률이 prob 로 가장 높다는 뜻)
match, prob = predict_num_by_MLP(test_img)

# 결과를 보여줄 바탕 이미지 만들고 거기에 결과 텍스트 저장
result_img = np.zeros((50, test_img.shape[1]), dtype=np.uint8)
cv.putText(result_img, str(match) + ':' + str(prob) + '%', font_org, font_shape, font_size, font_color, font_thickness)
result_show = cv.vconcat([test_img, result_img])
cv.imwrite('./test_MLP_result.jpg', result_show)


match, prob = predict_num_by_CNN(test_img)

result_img = np.zeros((50, test_img.shape[1]), dtype=np.uint8)
cv.putText(result_img, str(match) + ':' + str(prob) + '%', font_org, font_shape, font_size, font_color, font_thickness)
result_show = cv.vconcat([test_img, result_img])
cv.imwrite('./test_CNN_result.jpg', result_show)

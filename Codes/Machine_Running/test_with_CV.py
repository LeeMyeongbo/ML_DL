from tensorflow.keras.models import load_model
import cv2 as cv

# 학습이 완료된 모델의 파라미터를 불러온다.
mlp_model = load_model('./mnist_mlp_model.h5')
cnn_model = load_model('./mnist_cnn_model.h5')
size = 28
# 입력을 학습 모델에 통과시켜 클래스와 확률값을 반환하는 함수를 정의한다.
def predict_num_by_MLP(Image):
    Image = cv.resize(Image, (size, size))
    Image = Image.reshape(1, 784).astype('float')
    Image = Image / 255
    prob = mlp_model.predict_proba(Image)
    max_prob = max(prob[0])
    if(max_prob>.10):
        return mlp_model.predict_classes(Image), max_prob
    return "none", 0

def predict_num_by_CNN(Image):
    Image = cv.resize(Image, (size, size))
    Image = Image.reshape(1, size, size, 1);
    Image = Image / 255
    prob = cnn_model.predict_proba(Image)
    max_prob = max(prob[0])
    if(max_prob>.10):
        return cnn_model.predict_classes(Image), max_prob
    return "none", 0
    

#이미지를 입력받아 변수에 저장한다.
Test_Image = cv.imread('./TEST.jpg', 0)

#함수가 반환한 클래스와 확률 값을 변수에 저장한다.
match, prob = predict_num_by_MLP(Test_Image)

#결과를 이미지 파일로 저장하여 보여준다.
Test_Image2 = cv.resize(Test_Image, (200, 200))

#아래는 한 줄로 된 코드
cv.putText(Test_Image2, str(match)+' '+str(prob*100)+'%', (30,30), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)
cv.imwrite('./TEST_mlp_result.jpg', Test_Image2)

match, prob = predict_num_by_CNN(Test_Image)
Test_Image2 = cv.resize(Test_Image, (200, 200))

cv.putText(Test_Image2, str(match)+' '+str(prob*100)+'%', (30,30), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)
cv.imwrite('./TEST_cnn_result.jpg', Test_Image2)

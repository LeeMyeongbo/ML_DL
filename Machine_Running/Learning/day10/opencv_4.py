import cv2
import matplotlib.pyplot as plt

HAAR_CASCADE = './CV_HAAR/haarcascade_frontalface_alt.xml'
img_file = './IMAGE/cute.PNG'
DEBUG = True

# 1. 케스케이드 파일 지정해서 검출기 생성
cascade = cv2.CascadeClassifier(HAAR_CASCADE)
if DEBUG:
    print('cascade = {}'.format(cascade))

# 2. 이미지를 읽어 들이고 그레이 스케일로 변환
img = cv2.imread(img_file)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. 얼굴 인식하기
face_list = cascade.detectMultiScale(img_gray, minSize=(150, 150))

# 4. 결과 확인하기
if len(face_list) == 0:
    print("실패")
    quit()

# 5. 인식한 부분 표시
for(x, y, w, h) in face_list:
    print("얼굴의 좌표 =", x, y, w, h)
    red = (0, 0, 255)
    cv2.rectangle(img, (x, y), (x + w, y + h), red, thickness=10)

# 6. 이미지 출력하기
cv2.imwrite("face-detect.png", img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

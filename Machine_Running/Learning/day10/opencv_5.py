import cv2, os
import matplotlib.pyplot as plt

img_file = './IMAGE/cute.PNG'

# 1. 검출기 생성
cascade = cv2.CascadeClassifier('./CV_HAAR/haarcascade_frontalface_alt.xml')

# 지정된 부분 모자이크 처리 함수
def mosaic(img, rect, size):
    # 모자이크 적용할 부분 추출하기
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]

    # 축소하고 확대
    i_small = cv2.resize(i_rect, (size, size))
    i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)

    # 모자이크 적용
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2


# 2. 이미지 읽어 들이고 그레이 스케일로 변환
img = cv2.imread(img_file)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. 얼굴 검출하기
face_list = cascade.detectMultiScale(img_gray, minSize=(150,150))
if len(face_list) == 0:
    quit()

# 4. 인식한 부분에 모자이크 처리
for (x, y, w, h) in face_list:
    mos = mosaic(img, (x, y, x+w, y+h), 10)

# 5. 이미지 출력
newfile = os.path.dirname(img_file) + '/cute_mos.PNG'
print('newfile =', newfile)
cv2.imwrite(newfile, mos)
plt.imshow(cv2.cvtColor(mos, cv2.COLOR_BGR2RGB))
plt.show()

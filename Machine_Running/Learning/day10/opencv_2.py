import cv2
import matplotlib.pyplot as plt

img_name = './IMAGE/1416295979013.jpeg'
img_save = './IMAGE/1416295979013_resize.jpeg'
DEBUG = True

# 1. 이미지 읽기
img = cv2.imread(img_name)

# 2. 이미지 변경 및 저장
im2 = cv2.resize(img, (500, 500))
ret = cv2.imwrite(img_save, im2)

if DEBUG:
    print('ret = {}'.format(ret))
if ret:
    plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
    plt.show()
else:
    print('--SAVE FAIL')
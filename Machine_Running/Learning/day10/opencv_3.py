import cv2
import matplotlib.pyplot as plt

img_name = './IMAGE/1416295979013_resize.jpeg'
img_save = './IMAGE/1416295979013_cut.jpeg'
DEBUG = True

# 1. 이미지 읽기
img = cv2.imread(img_name)
if DEBUG:
    print('img = {}'.format(img))

# 2. 이미지 잘라내기
im2 = img[150:450, 150:450]

# 3. 잘라낸 이미지 저장
ret = cv2.imwrite(img_save, im2)

if DEBUG:
    print('ret = {}'.format(ret))
if ret:
    plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
    plt.show()
else:
    print('--SAVE FAIL')

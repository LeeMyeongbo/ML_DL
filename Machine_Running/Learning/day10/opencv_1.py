import urllib.request as req
import cv2, os
import matplotlib.pyplot as plt

img_name = './IMAGE/test.jpg'
img_url = 'http://uta.pw/shodou/img/28/214.png'
DEBUG = True

# 1. 이미지 다운
# 이미지 저장 폴더 존재여부 체크 후 없을 경우 폴더 생성
if not os.path.exists(os.path.dirname(img_name)):
    os.makedirs(img_name)
# 지정된 url에서 다운받은 이미지를 저장된 경로 & 이름으로 저장
req.urlretrieve(img_url, img_name)

# 2. 이미지 읽기
img = cv2.imread(img_name)
if DEBUG:
    print('type(img) = {}'.format(type(img)))
    print('img.shape = {}'.format(img.shape))
    print('img ============ \n{}\n'.format(img))

# 3. 이미지 보기
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# 4. 읽어온 이미지를 새로운 파일로 저장
img_save = './IMAGE/copy_test.jpg'
ret = cv2.imwrite(img_save, img)
if DEBUG:
    print('ret = {}'.format(ret))

print('Image Save OK!!') if ret else print('Fail...')

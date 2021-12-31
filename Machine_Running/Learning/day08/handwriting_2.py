import struct
import os

# csv 변환 메소드
def to_csv(name, maxdata):
    # 레이블 파일과 이미지 파일 열기
    lbl_f = open('./handwritings/' + name + '-labels-idx1-ubyte', "rb")
    img_f = open('./handwritings/' + name + '-images-idx3-ubyte', "rb")
    # csv 파일 생성
    csv_f = open('./handwritings/' + name + ".csv", 'w', encoding='utf-8')

    # 1. 헤더 정보 읽기
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_count = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols

    # 2. 이미지 데이터 읽고 csv로 저장
    res = []
    for idx in range(lbl_count):
        if idx > maxdata:
            break
        label = struct.unpack("B", lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label) + ",")
        csv_f.write(",".join(sdata) + "\r\n")

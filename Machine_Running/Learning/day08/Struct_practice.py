import struct

data = struct.pack('iid', 1, 2, 3.)  # int float float
print('type(data) = {}'.format(type(data)))
print('data => {}'.format(data))

# 바이너리데이터 => 수치데이터 쓰기 & 읽기
(i, x, y) = struct.unpack('iid', data)
print('type(data) = {}'.format(type(data)))
print('data => {}, {}, {}'.format(i, x, y))

try:
    file = open('data.txt', 'w', encoding='utf-8')

    for i in range(1, 6):  # i=1 부터 i=5까지 반복
        data = '%d번째 줄\n' % i  # %d 자리에 i 들어감
        file.write(data)

finally:
    file.close()



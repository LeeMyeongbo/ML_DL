try:
    file = open('test.html', mode='r', encoding='utf-8')

    while True:
        line = file.readline()
        if not line:
            break
        print(line)

finally:
    file.close()

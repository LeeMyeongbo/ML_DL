import sqlite3

# 데이터 변수 선언
filepath = 'test2.sqlite'

# 데이터베이스 제어
# 1. 데이터베이스 연결
conn = sqlite3.connect(filepath)

# 2. 테이블 생성 및 데이터 넣기
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""CREATE TABLE items(
    item_id INTEGER PRIVARY KEY,
    name    TEXT,
    price INTEGER)""")

# 3. 변경 내용 적용
conn.commit()

# 데이터 넣기
# 1. 데이터베이스 접근 포인트 획득
cur = conn.cursor()

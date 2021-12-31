import sqlite3

# 데이터 변수 선언
dbpath = 'test.sqlite'

# 1. 데이터 베이스 생성 및 연결
conn = sqlite3.connect(dbpath)

# 2. 테이블 생성 및 데이터 넣기
cur = conn.cursor()
cur.executescript("""
/* items 테이블이 이미 있다면 제거 */
DROP TABLE IF EXISTS items;

/* 테이블 생성 */
CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);
/* 데이터 넣기 */
INSERT INTO items(name, price)VALUES('Apple', 800);
INSERT INTO items(name, price)VALUES('Orange', 780);
INSERT INTO items(name, price)VALUES('Banana', 430);
""")

# 3. 데이터베이스 반영
conn.commit()

# 데이터 추출
# 1. 데이터베이스 접근 포인트 즉 커서 획득
cur = conn.cursor()

# 2. SQL 명령문 실행
cur.execute("Select item_id, name, price FROM items")

# 3. SQL 명령문 실행 결과
item_list = cur.fetchall()  # 모든 데이터 가져오기(튜플 타입)
# 출력
for it in item_list:
    print(it)

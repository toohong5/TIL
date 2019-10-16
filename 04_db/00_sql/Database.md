 sqlite3 설치

https://www.sqlite.org/download.html

**Precompiled Binaries for Windows**

[sqlite-dll-win64-x64-3300100.zip](https://www.sqlite.org/2019/sqlite-dll-win64-x64-3300100.zip)

[sqlite-tools-win32-x86-3300100.zip](https://www.sqlite.org/2019/sqlite-tools-win32-x86-3300100.zip)

c드라이브에 sqlite3 폴더 생성후 압축 풀기

환경변수 설정..(C:\sqlite 생성)

git bash -> winpty sqlite3

code ~/.bashrc 에서 alias 지정

source ~/.bashrc

# Database

c->insert

r-> select

u->update

d->delete

- 빈 데이터 베이스 만들기

```bash
$ sqlite3 tutorial.sqlite3
.databases
.mode csv # csv로 모드변경
.import hellodb.csv examples # examples => 테이블이름
.tables # 테이블 생성되었는지 확인
SELECT * FROM examples;	# database(examples) 전체 조회
.headers on	# 예쁘게 보자!
.mode column
```

- 테이블 생성

  CREATE TABLE table(

  ​	column1 datatype primary key,

  ​	column2 datatype,

  

  )....

  ```bash
  CREATE TABLE classmates (
     ...> id INTEGER PRIMARY KEY,
     ...> name TEXT );
  
  ```

- datatype
  - 유연하게 데이터가 들어간다. ('123' -> integer로 설정하면 자동으로 123으로 변경됨)
  - boolean 없음(0, 1 로 저장된다.)
- `.`  : 은 sqlite3 프로그램의 기능을 실행하는 것.
- `;` : 세미콜론 까지가 하나의 명령(Query)으로 간주
- SQL 문법은 소문자로 작성해도 된다.(단, 대문자를 권장)
- 하나의 DB에는 여러개의 table이 존재한다.

- table, schema 조회

  ```bash
  .schema table
  .tables
  ```

- table 삭제(DROP)

  DROP TABLE tablename;

  ```bash
  DROP TABLE classmates;
  ```

## DATA 추가, 삭제, 수정, 조회

### DATA 추가(INSERT)

- 새로운 행 추가

​	INSERT INTO table(column1, column2, ...) -> 모든 열에 데이터를 넣으려면 () 생략 가능.

​		VALUES(value1, value2, ...);

* id `INTEGER PRIMARY KEY` : rowid 를 대체 ( `INT PRIMARY KEY` 로 사용할 수 없음!!!)

- rowid는 자동으로 작성되는데... 직접 만든 id는 컬럼으로 명시되어야함. 

  => rowid를 사용하는게 편리..

### DATA 조회(SELECT)

- 원하는 개수만큼 가져오기

  ```bash
  SELECT rowid, name FROM classmates LIMIT 1;
  ```

- 특정위치에서부터 가져오기

  ```bash
  # 3번째 행 이후로 1개의 행 가져오기
  SELECT rowid, name FROM classmates LIMIT 1 OFFSET 3;
  ```

- 특정 값만 가져오기

  ```bash
  SELECT rowid, name FROM classmates WHERE address='서울';
  ```

- 특정 column 중복 없이 가져오기

  ```bash
  SELECT DISTINCT age FROM classmates; # age 중복없이 가져오기
  ```

### DATA 삭제(DELETE)

​	DELETE FROM table

​	WHERE 조건;

- rowid를 기준으로 접근한다

  ```bash
  # rowid가 4인 행 삭제
  DELETE FROM classmates WHERE rowid=4;
  ```

- 일부 행을 삭제하고 새 행을 삽입하면 삭제 된 행의 값을 재사용하려고 시도한다.

  - `AUTOINCREMENT` => 재사용방지..

    ```bash
    CREATE TABLE tests (
       ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
       ...> name TEXT NOT NULL);
    # 특정 id 삭제 후 다시 그 id 사용하지 않는다..
    ```

    - 엄격하게 필요로 하지 않으면 사용하지 않는것을 권장

    - row id 의 최대값은 64bit 8바이트 실수의 최대값(9,223,372,036,854,775,807 => 922경)

      INSERT INTO를 한다면..

      1. AUTOINCREMENT 가 없을 때 : 중간에 없는 ID를 재사용하므로 에러가 나지 않을 것.
      2.  AUTOINCREMENT 가 있을 때 : 최대 레코드를 넘어서기 때문에 에러가 발생.

### DATA 수정(UPDATE)

​	UPDATE table

​	SET col1=value1, col2=value2,

​		WHERE condition;

- 특정 id의 레코드 수정

  ```bash
  UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=4;
  ```



## WHERE(조건문)

```bash
$ .mode csv
$ .import users.csv users
.headers on
# age가 30 이상인 사람
SELECT * FROM users WHERE age >= 30;
# age가 30 이상인 사람의 이름가져오기
SELECT first_name FROM users WHERE age >= 30;
# age가 30 이상이고 성이 김인 사람의 성과 나이면 가져오기
SELECT last_name, age FROM users WHERE age >= 30 and last_name='김';
# 
```

- 레코드(행)의 개수 반환

  select count(column) from table;

  ```bash
  SELECT COUNT(*) FROM users;
  ```

- AVG(column), SUM(), MIN(), MAX()

  - 숫자일때만 가능

  ```bash
  # 30살 이상인 사람들의 평균 나이
  SELECT AVG(age) FROM users WHERE age >= 30;
  # 계좌 잔액이 가장 높은 사람과 액수
  SELECT MAX(balance), first_name FROM users;
  # 30살 이상인 사람의 계좌 평균 잔액
  SELECT AVG(balance) FROM users WHERE age >= 30;
  ```

  

- LIKE(패턴 비교)

  SELECT * FROM table

  WHERE column LIKE '' ;

  - 패턴

    `_` : 반드시 한 개의 문자가 존재해야한다.

    `%` : 이 자리에 문자열이 있을수도, 없을수도 있다.

    ex)

    ​	2% : 2로 시작하는 값

    ​	%2 : 2로 끝나는 값

    ​	%2% : 2가 들어가는 값

    ​	_2% : 아무값이나 들어가고 두번째가 2로 시작하는 값

    ​	1_ _ _ : 1로 시작하고 4자리인 값

    ​	2 _ % _ % (=2_ _%) : 2로시작하고 적어도 3자리인 값

  ```bash
  # 20대인 사람?
  SELECT * FROM users WHERE age LIKE '2%';
  # 지역번호가 02인 사람
  SELECT * FROM users WHERE phone LIKE '02-%';
  # 이름이 준으로 끝나는 사람
  SELECT * FROM users WHERE first_name LIKE '%준';
  # 핸드폰 중간번호가 5114인 사람만
  SELECT * FROM users WHERE phone LIKE '%-5114-%';
  ```

## ORDER(정렬)

​	ORDER BY col1 col2 ASC|DESC; (오름차순_ASC이 디폴트)

```bash
# 나이순으로 오름차순 정렬하여 상위 10개만 뽑기
SELECT * FROM users ORDER BY age LIMIT 10;
# 나이, 성 순으로 오름차순 정렬하여 상위 10개만 뽑기
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
# 계좌 잔액순으로 내림차순 정렬하여 성과 이름 10개만 뽑기
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
```

## ALTER(수정)

### 테이블 이름 바꾸기

ALTER TABLE exist_table

RENAME TO new_table;

```bash
ALTER TABLE articles RENAME TO news;
```

### 새로운 컬럼 추가

ALTER TABLE table

ADD COLUMN col_name DATATYPE;

```bash
ALTER TABLE news
   ...> ADD COLUMN created_at DATETIME NOT NULL;
#Error: Cannot add a NOT NULL column with default value NULL
# 해결 1.  NOT NULL 조건 빼고 작성
ALTER TABLE news
   ...> ADD COLUMN created_at DATETIME;
# 해결 2. 디폴트값 설정하기(null 이면 1로..)
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;
```
- **공식문서(https://docs.djangoproject.com/en/2.2/ref/models/fields/)에서 model field 확인하기**

- sqlite3 다운로드(https://www.sqlite.org/download.html)

  sqlite3 -> **Precompiled Binaries for Windows**-> 2, 3번째 다운

  c드라이브에 sqlite폴더 만들어서 다운받은 압축파일 풀어서 넣기

  환경변수에서 시스템변수 -> path-> C:\sqlite 만들기

  바탕화면 git bash에서 winpty sqlite3으로 확인하기

  .exit로 나갈 수 있음

  code ~/.bashrc

  alias sqlite3="winpty sqlite3"로 단축기 설정 (맥은 필요없데여)

  source ~/.bashrc 로 설정

- vscode에서...

  - sqlite3 db.sqlite3로 켜고

    - 보고싶은 테이블 열어보기

      .schema articles_article

- 집에서 clone받고 migrate 새로 해야한데!!(db는 안올라간데)

# 01_django_crud

## 1. SQL 기본용어정리

- 스키마 : 전체적인 메타정보

- sql도 프로그래밍 언어!
-  create read update delete(CRUD)
- SQL과 Python Object 사이에 ORM이 있어 파이썬 조작을 sql문으로 바꿔줌
- ORM 장점
  - sql문 몰라도 db 사용가능
  - sql의 절차적인 접근이 아닌 객체 지향적 접근 가능
  - 매핑 정보가 명확하여 ERD를 보는 것에 대한 의존도를 낮출 수 있다.
  - ORM 은 독립적으로 작성되어 있고, 해당 객체들을 재활용 할 수 있다. 개발자는 객체에 집중함으로써 해당 DB에 종속될 필요 없이 자유롭게 개발할 수 있다. (DB규칙에서 벗어나서 개발자가 자유롭게 개발 가능)
- ORM 단점
  - ORM 만으로 완전히 거대한 서비스를 구현하기가 어렵다.
    - 사용하기는 편하지만, 설계는 매우 신중하게 해야함
    - 프로젝트의 규모가 커질 경우 난이도가 올라가게 된다.
    - 순수 SQL 보다 약간의 속도저하가 생길 수 있다.
  - 이미 프로세스가 많은 시스템에서는 ORM으로 대체하기가 어렵다.
- 결론....
  - 생산성을 위해 ORM 채택(SQL 배울 시간에 파이썬으로 빠르게 개발하는게 낫다는 판단)
  - ORM을 사용하여 얻게되는 생산성은 약간의 성능저하나 다른 단점들을 상쇄할 만큼 뛰어나기 때문
  - 장점으로 인한 생산성 증가가 훨씬 크기 때문에 현대에는 대부분 프레임워크들이 ORM을 사용하고 있다.
  - 즉, 우리는 DB를 객체(object)와 인스턴스(instance)로 조작하기 위해 ORM을 배운다. _ 파이썬의 OOP 개념 알고오기!!!!!!



## 2. 모델

- 모델은 단일한 데이터에 대한 정보를 가지고 있다.
- 필수적인 필드(칼럼, 열)와 데이터(레코드, 행)에 대한 정보를 포함한다. 일반적으로 각각의 **모델(클래스)**는 단일한 데이터베이스 테이블과 **매핑(연결, 연동)**된다.
- 모델은 부가적인 메타데이터를 가진 **DB의 구조(layout)를 의미**

- 사용자가 저장하는 데이터들의 **필수적인 필드와 동작(behavior)을 포함**

### 1) 필드

#### 1. CharField()

- 길이의 제한이 있는 문자열을 넣을 때 사용
- `max_length`는 필수 인자다
- 필드의 최대길이(문자)이며 DB와 django의 유효성검사(값을 검증)에서 사용됨.
- 텍스트 양이 많을 경우 `TextField()`로 사용

#### 2. TextField()

- 글의 수가 많을 때 사용(제한 없을때)
- `max_length ` 옵션을 줄 수 있지만 모델과 실제 DB에는 적용되지 않는다. 길이 제한을 주고 싶다면  `CharField()` 를 사용해야 한다.

#### 3. DateTimeField()

- 시간과 날짜를 기록하기 위한 필드
- `auto_now_add=True`
  - django ORM이 최초 INSERT(테이블에 데이터 입력)시에만 현재 날짜와 시간 작성
  - 최초 생성일자 
- `auto_now=True`
  - django ORM이 SAVE를 할 때마다 현재 날짜와 시간을 작성
  - **최종 수정일자**

### 2) model 로직

- DB 컬럼과 어떠한 타입으로 정의할 것인지에 대해 `django.db` 모듈의 `models`의 상속을 받아서 적용된다.
- 각 모델은 **`django.db.models.Model`클래스의 서브 클래스**로 표현된다.(자식클래스)
- 모든 필드는 기본적으로 NOT NULL(DB에 NULL 값은 들어갈 수 없다) 조건이 붙는다.
- 각각의 클래스 변수들은 모델의 데이터베이스 필드를 나타낸다.

### 3) Migrations

1. `migrations`

   ```bash
   $ python manage.py makemigrations
   ```

   - makemigrations 명령어는 모델(models.py)을 작성/변경한 사항을 django에게 알리는 작업. (ORM에 보낼 PYTHON 코드 설계도를 작성)
   - 테이블에 대한 설계도(django ORM이 만들어줌)를 생성

2. `migrate`

   - migrations 로 만든 설계도를 기반으로 실제 `db.sqlite2` DB에 반영한다.
   - **모델에서의 변경사항들과 DB 스키마가 동기화**를 이룬다.(모델과 DB의 정보가 동기화됨)

```bash
$ python manage.py sqlmigrate app_name 0001
```

- 해당 migrations 설계도가 SQL문으로 어떻게 해석되어 동작할지 미리 볼 수 있다.(필수는 아님 그냥 확인하는 용도)

```BASH
$ python manage.py showmigrations
```

- migrations 설계도가 migrate 되었는지 여부 확인 (X로 표시되면 되었다는 뜻) _ 필수아님 확인하는 용도

### 4) Model 변경 시 작성 순서 :warning:

* model 날리는법 : migrations의 숫자로된 파일들 지우고 db 날리기

1. `models.py` : 작성 및 변경(생성/수정하는 곳)
2. `makemigrations` : migrations 파일 만들기(설계도)
3. `migrate` : 실제 DB에 적용 및 동기화(테이블 생성)

테이블의 이름은 app이름과 model에 작성한 class 이름이 조합되어져서  자동으로 만들어 진다.(**모두 소문자**)

모델의 클래스 변수들은 반드시 **소문자**로 작성한다.

- python manage.py makemigrations

  -> articles/migrations/0001_initial.py이 생성됨(db 가기전의 파이썬 설계도임. orm이 저걸 sql로 해석해서 보냄)

- python manage.py sqlmigrate articles 0001 -> 0001이 어떻게 해석되어 넘어가는지 보여줌

- python manage.py makemigrations => models 변경했으면 설계도 업데이트 해줘야함!! (0002가 생성됨 -> 최신설계도임)

- 최종설계도 기준으로 migrate해준다!

- sqlite 설치하기!! -> f1-> sqlite -> open database -> db.sqlite3 선택 (비었는지 확인)

- python manage.py migrate 테이블 생성=>앱이름_클래스이름으로 테이블이 생성된다.(내가 작성한 테이블 외에 기본적으로 만들어지는 애들이 있음!(installed_apps에 있는 애들))

  <hr>

## 3. CRUD(DB API 조작)

### 1. Django Shell

- django 프로젝트 설정이 로딩된 파이썬 shell

- 일반 파이썬 shell로는 django 환경에 접근 불가

- 즉, django 프로젝트 환경에서 파이썬 shell을 끌어다 활용한다고 생각

- pip install ipython 설치

- python manage.py shell 로 켠다

- from articles.models import Article => models.py에서 작성한 클래스를 import 해준다

- Article.objects.all() => 테이블이 내용 전부 조회(READ)

  ```bash
  # ORM 문법
  # DB에 쿼리를 날려서 인스턴스 객체 전부를 달라고 하는 뜻
  # 만약에 레코드(행)가 하나라면, 인스턴스 단일객체로 반환
  # 두 개 이상이면 QuerySet 형태로 반환
  # all() : 모든 내용을 가져오라는 메소드임
  Article.objects.all()
  # 위와 아래가 동일한 일을 함
  select *
  from articles_article;
  ```

  #### 1) CREATE

  - 레코드 한 줄 작성하기

    ```bash
    article = Article() # 인스턴스 생성
    article.title = 'first' # title에 first라는 값 생성
    article.content = 'django!'
    # 값만 넣어 준 것 뿐임...
    article.save() # 테이블에 저장해줌!
    Article.objects.all() # 내용 불러와서 확인
    article.pk # id와 같은 것 임.(몇 개의 id가 있는지 보여줌)
    article.full_clean() # 유효성검증 방법
    ```

  - 데이터 객체를 만드는(생성, CREATE) 하는 3가지 방법

    1. shell에서..(위의 방법)

       ```python
       $ python manage.py shell #shell 켜기
       
       # SQL 문에서 작성법 - 특정 테이블에 새로운 레코드(행)을 추가하여 데이터 추가
       # INSERT INTO table (column1, column2, ...) VALUES(value1, value2, ...)
       # INSERT INTO articles_article (title, content) VALUES ('first', 'django!')
       
       >>> article = Article() # 인스턴스 생성
       >>> article.title = 'first' 
       # title에 first라는 값 생성
       >>>article.content = 'django!'
       
       # save 를 하지 않으면 아직 DB에 값이 저장되지 않음
       >>> article
       <Article: Article object (None)>
       >>> Article.objects.all()
       <QuerySet []>
       
       # save 를 하고 확인해보면 저장된 것을 확인할 수 있다.
       >>> article.save()
       >>> article
       <Article: Article object (1)>
       >>> Article.objects.all()
       <QuerySet [<Article: Article object (1)>]>
       
       # 인스턴스 article 을 활용하여 변수에 접근할 수 있다.(저장된 값 확인)
       >>> article.title
       'first'
       >>> article.content
       'django'
       >>> article.created_at
       datetime.datetime(2019, 8, 21, 2, 44, 11, 944512, tzinfo=<UTC>)
       
       ```

    2. 함수의 키워드 인자 이용

       ```python
       >>> article = Article(title='second', content='django!!')
       >>>article.save()
       ```

    3.  세번째

       - `create()`를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스텝으로 끝난다. (바로 저장되어서 유효성 검증을 할 수가 없음....)

       ```python
       >>> Article.objects.create(title='third', content='django!!!')
       # save도 한번에 됨!
       ```

    - 유효성 검사
      - save 전에 `full_clean()` 메서드를 통해 article 이라는 인스턴스 객체가 검증(validation)에 적합한지를 알아 볼 수 있다.
      - `models.py`에 필드 속성과 옵션에 따라 검증을 진행한다.

  

  #### 2) READ

  ```python
  # 1. SELECT * FROM articles_article;
  # 1. DB에 있는 모든 글 가져오기
  >>> Article.objects.all()
  -------------
  # 2. SELECT * FROM articles_article WHERE title='first';
  # 2. DB에 저장된 글 중에서 title이 first 인 글만 가져오기
  >>> Article.objects.filter(title='first')
  
  # 3. SELECT * FROM articles_article WHERE title='first' LIMIT 1;
  # 3. DB에 저장된 글 중에서 title이 first 인 글 중에서 첫번째 글만 가져오기
  >>> Article.objects.all().first()
  >>> Article.objects.all().last() # 마지막 값
  ---------------
  # 4-1. SELECT * FROM articles_article WHERE id=1;
  # 4-1. DB에 저장된 글 중에서 PK가 1인 글만 가져오기
  >>> Article.objects.get(pk=1)
  
  # PK 만 .get() 으로 가져올 수 있다. (.get()은 값이 중복이거나 일치하는 값이 없으면 에러를 발생시킨다.) 즉, pk 에만 사용하자.
  
  # 4-2. filter 의 경우 존재하지 않으면 에러가 아닌 빈 쿼리셋을 반환한다. 마치 딕셔너리에서 value를 꺼낼 때 [] 방식으로 꺼내냐 혹은 .get 으로 꺼내냐 하는 차이와 유사
  >>> Article.objects.filter(pk=100)
  <QuerySet []>
  # id 에 접근할 때 filter는 적합하지 않음
  
  # 4-3. filter / get
  # filter 자체가 여러 값을 가져올 수 있기 때문에 django가 개수를 보장하지 못한다. 그래서 0개, 1개라도 무조건 쿼리셋으로 반환한다.
  
  -----------
  # 5-1. 오름차순
  # SELECT * FROM articles_article ORDER BY title ASC;
  >>> Article.objects.order_by('pk') # 해당 column을 오름차순으로 정렬해서 출력
  
  # 5-2. 내림차순
  # SELECT * FROM articles_article ORDER BY title DESC;
  >>> Article.objects.order_by('-pk')
  
  ---------------
  
  # 6. 쿼리셋은 리스트 자료형은 아니지만, 리스트에서 할 수 있는 인덱스 접근 및 슬라이싱이 모두 가능하다.
  >>> Article.objects.all()[2]
  >>> Article.objects.all()[1:3]
  
  ---------------
  
  # 7. LIKE / startswith / endswith
  # django ORM은 이름(title)과 필터(contains)를 더블 언더스코어(__)로 구분한다.
  # 더블언더스코어 == 던더(dunder)스코어
  # LIKE
  >>> Article.objects.filter(title__contains='fir')
  
  # startswith
  >>> Article.objects.filter(title__startswith='fir')
  
  # endswith
  >>> Article.objects.filter(content__endswith='!')
  
  ```

  

  1. DB의 모든 글 가져오기

     ``` python
     Article.objects.all()
     ```

  2. 저장과 동시에 읽어오기

     ```python
     >>>Article.objects.create(title='fifth', content='django!!!!!')
     <Article: 5번글 - fifth : django!!!!!>
     ```

  3. 특정조건의 db 읽어오기

     ```python
     >>>articles = Article.objects.filter(title='first')
     >>>articles
     <QuerySet [<Article: 1번글 - first : django!>]>
     >>>type(articles)
     django.db.models.query.QuerySet
     # 인스턴스가 아닌 QuerySet으로 저장됨.
     
     # 첫번째 값만 가져옴
     >>>Article.objects.filter(title='first').first()
     # 해당 조건의 마지막 값만 가져옴
     >>>Article.objects.filter(title='first').last()
     
     
     ```

  4. 하나만 가져오기(key로 접근한다.) _ id로 가져올때는 `.get()`사용!!

     ```python
     >>>article = Article.objects.get(pk=1)
     >>>article
     <Article: 1번글 - first : django!>
     >>>type(article)
     articles.models.Article
     # QuerySet이 아닌 인스턴스임
     
     >>>Article.objects.get(title='first')
     MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
     # 중복값 있으면 에러!
     
     # 없는 키에 접근시 에러남
     
     # filter로 없는키에 접근시 빈 QuerySet나옴!
     >>>Article.objects.filter(pk=10)
     <QuerySet []>
     ```

  5. 역순 출력

     ```python
     >>> Article.objects.order_by('-pk')
     # column 명 앞에 - 붙여준다!
     
     # 인덱싱 사용 가능
     >>> articles = Article.objects.all()[1:3]
     # 특정 인덱스 접근 가능
     >>> 
     ```

  6.  조건

     ```python
     >>>articles = Article.objects.filter(title__contains='fir')
     # title에 'fir' 포함하는 모든 글 가져오기
     >>>articles = Article.objects.filter(title__startswith='fir')
     # 'fir'로 시작하는..
     >>>articles = Article.objects.filter(content__endswith='!')
     # '!'로 끝나는 content 가져오기
     
     ```

     

  #### 3) UPDATE

  - update하고 저장해야 테이블에도 변경됨.

  ```python
  # article 인스턴스 객체의 인스턴스 변수에 들어있는 기존 값을 변경하고 저장
  >>> article = Article.objects.get(pk=1)
  >>> article.title = 'byebye' # 새로운 값
  >>> article.save() # 테이블에서 값 변경하고 저장
  ```

  #### 4) DELETE

  - 한번 지워진 id는 다시 생기지 않고 새로 데이터 생성시 마지막 값 다음것 부터 생긴다.

  ``` python
  # article 인스턴스 객체를 생성후 .delete() 메서드를 호출
  >>> article = Article.objects.get(pk=1)
  
  >>> article.delete()
  ```

  

  - 핵심은 우리는 ORM을 통해 클래스의 인스턴스 객체로 DB를 조작 할 수 있다는것!!
  - 앞으로 CRUD 로직을 직접 작성하면서 위에서 배운 코드들을 다시 활용하게 될 것이다.

  #### 5) QuerySet 기본 개념

  - 전달 받은 객체의 목록
    - QuerySet : 쿼리 set 객체
    - Query : 단일 객체
  - DB 로부터 데이터를 읽고, 필터를 걸거나 정렬 등을 수행
  - Query를 던지는 Language(django ORM) 를 활용해서 DB에게 데이터에 대한 조작을 요구한다.

  `QuerySet`

  - objects 사용하여 **다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체**
  - 단일한 객체를 반환(return)할 때는  테이블(class)의 인스턴스로 리턴 됨

  `objects`

  - Model Manager와 Django Model 사이의 Query 연산(쿼리 날리기)의 인터페이스 역할을 해주는 친구
  - 즉, `models.py`에 설정한 클래스(테이블)을 불러와서 사용할 때 DB와의 인터페이스 역할(쿼리를 날려주는 역할)을 하는 매니저이다.
  - 쉽게 이해하려면 ORM의 역할이라고 생각하면 된다.
  - DB ------------ objects ------------ Python Class(models.py)
  - Manager(objects) 를 통해 특정 데이터를 조작(메서드)할 수 있다.



## 4. ADMIN

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지.
- `models.py`에 작성한 클래스를 `admin.py`에 등록하고 관리.
- record 생성 여부 확인에 매우 유용하고 직접 레코드를 작성할 수도 있다.
- CRUD 로직을 모두 관리자페이지에서 사용할 수 있다.



- python manage.py createsuperuser  => 

1. list_display

   - admin 페이지에서 우리가 `models.py`에 정의한 각각의 속성(칼럼)들의 값(레코드)을 보여준다.

2. list_filter

   - 특정 필드에 의해 변경목록을 필터링 할 수 있게 해주는 Filter 사이드바를 추가한다.
   - 표시되는 필터의 유형은 필드의 유형에 따라 다르다

3. list_display_links

   - 목록 내에서 링크로 지정할 필드 적용(설정하지 않으면 기본값을 첫번째 필드에 링크가 적용)

4. list_editable

   - 목록 상에서 직접 수정할 필드 적용

5. list_per_page

   - 한 페이지에 표시되는 항목 수를 제어(기본 값 : 100)

   

## 5. Django extensions

https://django-extensions.readthedocs.io/en/latest/installation_instructions.html

https://django-extensions.readthedocs.io/en/latest/shell_plus.html

- Django-extension 은 커스텀 확장 tool이다.
- Django app 구조로 되어 있기 때문에 프로젝트에서 사용하기 위해서는 app 등록 과정을 거쳐야 한다.('django_extensions', 를 settings에 추가)
- 


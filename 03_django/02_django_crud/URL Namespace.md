# URL Namespace

## 1.  하드코딩 URL 제거

- {% url  'name' %} template tag

문제점

- app이 여러개가 되면, 단순히 url name만 가지고는 어떤 app의 url인지 알 수 없다.

## 2. URL namespace 설정

- app_name = 'appname'

- {% url  'appname:name' 넘겨줄인자%}



# HTTP 기본속성

- 쿠키 : 
- 세션 : 로그인상태 유지시켜 줌
- URL(uniform resource identifilter) : 파일식별자
  - 인터넷 상에서 자원이 어디 있는지 알려주기 위한 규약
  - 
- URI(uniform resource identifilter): 통합 자원 식별자
  - 인터넷에 자원을 나타내는 유일한 주소
  - 인터넷에서 요구되는 기본조건으로서 http에 항상 붙어다닌다.
- URI > URL=URN (모든 URL은 URI다.)
- Example
  - https://www.google.com 
    - 서버 주소=> URI이면서URL
  - https://github.com/ss-02-djpy2/TIL/blob/master/03_django/markdown/Django_01.md 
    - 주소 + 디렉토리 파일의 주소(경로, 자원의 위치) => URI이면서 URL
  - [https://www.google.com/search?q=삼성](https://www.google.com/search?q=삼성)
    - 주소 + 특정 문자열(query string)(search?q=)
    - search 까지가 url + `q=삼성` 이라는 식별자가 필요하므로 URI 이지만 URL은 아니다. (식별자가 있으면 URL 아님!)
  - https://getbootstrap.com/docs/4.3/getting-started/introduction/#starter-template
    - #.. : fragment임
    - URI
- HTTP METHOD
  - GET: 표시요청, 데이터를 받기만 함
  - POST: 모델의 자료를 보냄
  - PUT/PATCH : 수정할때
  - DELETE: 삭제요청
  - 실제로 http에서는 공식적으로 GET, POST 만 사용된다.
- RESTful (Rrepresentational State Transfer)
  - 주소보면 직관적으로 뭐가 나올지 알 수 있어야 한다.
  - url깔끔하게 작성해보자..
  - 주소의 모양을 딱 봤을때 알아볼 수 있게 url 깔끔하게 정돈하자는뜻
  - 약속(규약)아님!!
  - 자원(uri), 행위(), 
  - `규칙`
    - uri는 정보의 자원을 표현해야 한다
    - 자원에 대한 행위는 http  method로 표현한다
  - ex)
    - GET/users/1/read
      - 주소에 행위가 들어가지 않는게 좋다...
      - read라는 불필요한 정보 들어감.(자원에 대한 정보만 들어가는게 바람직하다..)
    - GET/users/1/delete/
      - 행동은 method앞에 들어가는게 좋다..
      - DELETE/users/1/이 더 바람직 함!(서버의 행동 자체를 바꿈->삭제method!)
    - GET/users/1/create/
      - 모델을 건드는 요청은 POST..
      - POST/users/1/
  - url 작성 팁!
    1. 기본
       - / 는 계층관계를 나타냄..
       - URI에는 소문자를 사용
       - _대신 - 활용
    2. 리소스 관계를 표현하는 방법
  - 같은 주소로 들어가는데 get이냐 post냐에 따라 행동을 다르게 할 것 이다.(new+create) -> 주소를 하나로 만들고 method만 바꾼다..
    - GET articles/create/ 글을 작성하는 페이지
    - POST articles/create/ 글이 실제로 작성
  - form tag에 action이 없다면, 현재 머물고 있는 URL로 요청을 보낸다.
  - a tag는 get방식만 지원..
  - post는 form tag에서..





# Model Instance Method

## 1. `get_absolute_url()`

- 모델에 작성하는 메서드임



# URL Reverse 를 수행하는 함수들

## 1. reverse()

- 리턴 값: string(문자열)

- 특정 문자열을 얻고 싶을 때

  ```python
  reverse('articles:index') # '/articles/' 가 리턴됨
  ```

## 2. redirect()

- 리턴 값 : HttpResponseRedirect(객체)

- 내부적으로 `resolve_url()`을 사용

- view 함수에서 특정 url로 돌려보내고자 할 때 사용

  ```python
  redirect('articles:article')
  # <HttpResponseRedirect status_code=200, "text/html"; charset=utf-8, url="/articles/">
  ```

  

## 3. url template tag( `{% url %}`)

- 내부적으로 `reverse()`를 사용



## `redirect(모델 인스턴스) `를 통해서 모델 인스턴스의 get_absolute_url() 함수를 자동으로 호출!



# 실습

2번째 app => jobs

1. model 2 개 컬럼(name: 20자 제한/ past_job: 제한 없음)
2. view 2개 => index / past_life(past_job 모델에 저장하고 모델에 존재하면 그대로 가져오고 새로운 이름이면 faker 동작시켜 결과나옴)

포인트

- 입력된 이름이 db에 있는지 없는지
- 있다면 기존 db에서 그대로 가져와서 출력
- 없다면 faker를 통해 생성된 새로운 직업과 함께



app생성 -> settings-> models.py 작성-> makemigrations->admin.py 작성 -> 작성 잘되면..->urls.py생성 (프로젝트의 urls.py에 연결) -> views.py -> index 작성

pip install python -decouple


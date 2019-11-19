# Django & Vue js

데이터 전송 방법

https://jwt.io/

## JWT(Jason Web Token)

- 정보를 안전하게 json 객체로 전송하기 위한 간결하고 독립적인 방법

- 사용하는 곳

  1. 회원인증(인증을 위한 수단)
     - 서버가 유저 정보에 기반한 토큰을 발급해 유저에게 전달하고, 유저는 서버에 요청을 보낼때마다 JWT를 보함하여 전달.
     - 서버는 세션을 유지할 필요 없이 유저의 요청정보 안에 있는 JWT 만 확인하면 된다.(서버 자원 아낄 수 있음)

  2. 정보교환(모든 요청에 jwt가 붙어서 응답받게됨)
     - 정보가 서명되어 있기 때문에 정보를 보낸 사람의 정보 혹은 정보가 조작여부 확인 등이 가능

- xxxx(header).yyyy(payload_내용).zzzz(signiture) : 하나의 토큰임

- 세션, 쿠키와 함께 모바일과 웹의 인증을 책임지는 대표 기술 중 하나. 세션/쿠키의 정보 전달 방식과 유사하게 사용자는 Access Token (JWT token) 을 HTTP header에 실어서 서버로 요청을 보냄.

- 세션 / 쿠키 방식과 가장 큰 차이점은 세션 / 쿠키는 세션 저장소에 유저의 정보를 넣지만, JWT는 토큰안에 유저의 정보를 넣는다. ( 세션측에서 부하가 걸리지 않도록 TOKEN쪽에 정보를 넣는다. 서버측에선 저장하지 않는다! )

- Client 의 입장에서는 HTTP header에 세션 ID/ 토큰을 실어서 보낸다는 점은 동일하지만, Server 입장에서는 인증을 위해 암호화 (JWT 방식)를 하냐 혹은 별도의 저장소(세션/쿠키 방식) 를 이용하느냐의 차이(서버에선 암호화하는 기술만 가지고 있음: JWT)

### 요약

- 두 개체에서 JSON 객체를 사용하여 가볍고 `자가 수용적인`(self-contained, 필요한 모드 정보를 자체적으로 지님) 방식으로 정보를 안정성 있게 전달.
- 세션 상태를 저장하는 것이 아니라 필요한 정보를 JWT 에 저장해서 사용자가 가지고 있게 하고, 해당 JWT를 증명서 처럼 사용하는 방식.

### 장점

1. 세션/쿠키 처럼 별도의 저장소 관리가 필요 없고 발급한 이후에 검증만 하면 된다.
2. 토큰을 기반으로 한 다른 인증시스템에 접근이 용이하기 때문에 확장성이 뛰어나다. 
3. 모바일 환경에 적합 ( 쿠키와 같은 데이터로 인증할 필요가 없기 때문 )
4. Python, JS, Ruby, Go 등 주류 프로그래밍 언어에서 대부분 지원된다.

### 단점

1. 이미 발급 된 JWT는 유효기간이 완료될 때까지 계속 사용하기 때문에 악용될 가능성이 있다. ( 한 번 발급된 토큰은 값을 수정하거나 폐기할 수 없다.) 그래서 이 문제는 Access Token의 유효기간(expire time) 을 짧게하고 Refresh Token 등을 이용해서 중간중간 새로운 토큰을 재발행 해준다.
2. 세션/쿠키 방식에 비해 claim JWT 토큰의 길이가 길어지기 때문에 인증 요청이 많아 질수록 네트워크의 대역폭이 낭비될 수 있다. ( 네트워크 과부하 / API 호출 시 매 호출마다 헤더에 붙여서 전달하기 때문 )

- ### header

  - token의 type(jwt)과 사용 algorithm의 명칭이 들어감

- ### payload(정보)

  - 토큰에 담길 정보가 들어있는 곳(claim - key:value 형태로 데이터가 들어감)

  1. #### registerd claim

     - 토큰에 대한 정보들을 담기 위해 이름이 이미 정해진 클레임들(키값이 정해져있음). 클레임의 사용은 모두 선택적이다.(필수 인자 따로 없음, 필요한 것만 넣는다.)

  2. #### public claim

     - 공개 클레임은 충돌이 되지 않는 이름을 가지고 있어야 함. 보통 충돌을 방지하기 위해 key 값을 URI 형태로 만든다.( ex: 'https://test.co.kr/jwt_token': true )

  3. #### private claim

     - 등록된 클레임도 아니고 공개 클래임도 아님. 클라이언트와 서버간에 협의하에 사용되는 클레임들.
     - key 값이 중복되서 충돌이 될 수 있으니 유의해서 사용. (이름이 겹치는 경우가 생길 수 있음 주의!)
     - 예) `{"username": "admin"}`

- ### signiture(서명)

  - header와 payload의 값에 비밀키로 hashing
  - HEADER 의 인코딩 값과, PAYLOAD 의 인코딩 값을 합친 후 주어진 비밀키로 해쉬를 생성한 값



------------------

```bash
# vue 먼저
$ vue create todo-front
$ mkdir todo-back
$ cd todo-back/
$ python -m venv venv
$ source venv/Scripts/activate
$ pip list
$ pip install django
$ django-admin startproject todoback .
$ python manage.py startapp todos
$ cd ..
$ cd todo-front/
$ vue ui
# 경로 설정하고 프로젝트 가져오기
# 플러그인에서 plugin-router 설치
$ npm run serve
```



## router-link

- router 지원 앱에서 사용자 네비게이션을 가능하게하는 컴포넌트
- 목표 위치는 `to` prop 으로 지정된다.
- 라우팅은 URI에 따라 해당하는 정적 파일을 내려주는 방식인데 이를 브라우저에서 구현하는 것이 SPA 개발의 핵심
- `router-link` 는 `a` 태그보다 선호되는데 이유는 HTML5 히스토리 모드에서 클릭 이벤트 자체를 차단하여 브라우저가 페이지를 다시 로드하지 않도록 한다.

## router-view

- 라우팅이 경로에 맞는 컴포넌트를 제공하는 데 해당 경로에 맞는 컴포넌트를 렌더링 해주는 부분 

--------

## CORS (Cross-Origin Resource Sharing)

https://developer.mozilla.org/ko/docs/Web/HTTP/Access_control_CORS

### 정의

- 한 도메인에서 로드되어 다른 도메인에 있는 리소스와 상호 작용 하는 것.
- 즉, 도메인이나 포트가 다른 서버의 자원을 요청하는 메커니즘.

### 문제상황

1. 요청을 할 때 cross-origin HTTP 에 의해 요청을 한다

2. 하지만 CORS 와 같은 상황이 발생하면 외부 서버에 의한 요청 데이터를 브라우저에서 차단하기 때문에 (보안 목적) 정상적으로 데이터를 받을 수 없다.

3. 예를 들어, http://localhost:8080/ 에서 vue 를 실행하고, http://localhost:8000/ 에서 django를 실행할 경우 포트가 달라 다른 도메인으로 인지하고 브라우저가 요청을 차단한다.

    

### 해결방법

1. 서버(django)와 클라이언트(vue) 가 같은 도메인과 포트를 사용하도록 한다.
2. 서버에서 cross-origin HTTP 요청을 허가한다. (우리가 해결할 방법)
   -  실제 API 서버들은 이러한 CORS 제한과 관련된 처리를 모두 해두어야한다.


# 01_django

## 1. Form(GET 방식)



## 2. Form(POST 방식)

- csrf 사이트간 요청위조

  웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지의 보안을  무력화 시키거나, 수정, 삭제 등의 강제적인 작업을 하게하는 공격방법.

  django는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash 값을 token으로 부여한다.  이 token 값이 없는 요청은 잘못된 요청이라고 판단하여 접근을 거부한다.(403 error)

- csfr_tocken에 주의

## 3. static 정적파일

- image/ css/ js 파일과 같이 해당 내용이 고정되어 응답을 할때 별도의 처리 없이 그대로 보여주면 되는 파일들
- load 해야함
- {% static ' 주소 '%}

## 4. URL 로직 분리(프로젝트 & 앱)

- 주소/앱/파일명 으로 접근

- 장고의  namespace 오류 : pages와 utilities에 동일한 이름의 templates가 있을 경우 발생
  - settings의 installed_apps에서 가장 상단의 앱에 있는 templates를 읽어옴

## 5. Django namespace(template , static)

- templates/static 을 수정(이름공간 만들기)
  - pages라는 앱의 templates에 앱 이름과 동일한 폴더 하나더 만들어 html 파일들 넣기

## 6. Template Inheritance(상속)_block

{% block 부모의 공간이름 %}

{% end block %}

- 코드 반복하지 않기 위함
- 프로젝트에서 templates를 만들고 그 안에 base.html 생성
- settings의 templates에 

`'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')],`

(base dir, 프로젝트명, 파일명)

- extends는 최상단에 위치시키기!!
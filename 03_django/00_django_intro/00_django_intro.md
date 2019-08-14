# django

- 파이썬으로 100% 짜여진 프레임워크..
- 특징
  - 다용도성
  - 안전성 : 해시값으로 비밀번호 받기때문에 장고도 비번 모름
  - 확장성
  - 완결성
  - 쉬운 유지보수 : 반복을 싫어해 코드가 간결해 짐
  - 포터블
- django의 성격
  - 독선적 : 개발자의 자유도 떨어짐, 코드 간결해짐, 생산성 높음(빠른개발 가능) _ 대부분의 프레임워크, 장고는 다소 독선적...
  - 관용적 : 여러 컴포넌트들을 개발자가 붙여쓸 수 있음, 제약 거의 없이 개발 가능. 최소한의 도움만 줌, 개발자가 손볼게 많음...(간결하지 못 할 수 도 있음)
- what is django?
  - dynamic web(web app) : 상황에 따라 사용자의 입력에 따라 사이트가 동적으로 바뀜





** 장고 사용시 3.7버전 사용!

*** 3.7의 의존성(가상환경)

 본인의 컴퓨터에서 잘 작동하던 프로그램도, 다른 프로그램에 설치 했을 때 잘 동작하리라는 보장이 없음

파이썬도 같은 버전, 같은 모듈을 쓴다는 보장이 없다.

특정 프로그램만을 실행하기 위한 파이썬 환경을 따로 만들어서, 그 환경속에서만 모듈을 관리하고, 앱을 실행시키기 위해 가상환경을 설정한다.

다른 앱을 실행시키는 일이 생기면 그 가상환경을 빠져나와 다른 환경을 만드는 방식으로 진행한다.

내가 가상환경에서 작업하고 있는지 잘 확인해야함!!



*명령어

- 단축어 설정....=> code ~/.bashrc

- python -m venv 가상환경경로+이름
- python -m venv ssafy =>내가 있는 곳에 ssafy라는 가상환경 만들기
- python -m venv ~documents/ssafy => document라는 경로에 ssafy만들기

- source venv/Scripts/activate => 가상환경 켜기
- pip list 로 환경 환인하기
- deactivate 로 끄기

- gitignore.io에서 장고, 비쥬얼스튜디오 코드 가져오기
- 

- pip install django
- python -m django --version =>2.2.4ver



- 장고 프로젝트 만들기
- django-admin startproject django_intro . => 현재폴더에 django_intro라는 폴더 만들기
- 프로젝트 실행하기
- python  manage.py runserver



- 장고 MV(VIEW)C => MT(TEMPLATE)V(VIEW) ( 장고는 MTV 패턴기반프레임워크) 
  - M(Model) : 데이터를 관리
  - T(Template) : 사용자가 보는 화면
  - V(View) : 중간 관리자



- 장고 앱만들기

  - python manage.py startapp pages (앱 이름은 복수형으로 만들기!!)

  - 뷰와 모델이 먼저 만들어짐, 템플릿은 우리가 직접 만들어야함.

  - settings.py의 INSTALLED_APPS에 'pages.apps.PagesConfig', 를 등록!!! (pates라는 폴더의 apps.py에 pages를 등록)

  - app등록시 , 필수!

  - ​    \# app 등록 순서

    ​    \# 1. local apps

    ​    \# 2. Third party apps

    ​    \# 3. Django apps

- 맨 먼저 view!

  ```python
  def index(request): # 첫번째 인자는 반드시 request
      return render(request, 'index.html') # render()의 첫번째 인자도 반드시 request
  ```

- 다음은 project의 url

  ```python
  from pages import views # 생성한 app pages 폴더 안의 view.py 파일을 가져온다.
  
  urlpatterns = [
      path('index/', views.index), # url 경로 마지막에 / 를 붙이는 습관!
      path('admin/', admin.site.urls),
  ]
  
  ```



- 코드 작성 순서!!!!

  1. view : 만들고자 하는 view 함수 작성

     ```python
     def index(request): # 첫번째 인자는 반드시 request
         return render(request, 'index.html') # render()의 첫번째 인자도 반드시 request
     ```

  2. urls : views에서 만든 함수에 주소를 연결

     ```python
     from pages import views # 생성한 app pages 폴더 안의 view.py 파일을 가져온다.
     
     urlpatterns = [
         path('index/', views.index), # url 경로 마지막에 / 를 붙이는 습관!
         path('admin/', admin.site.urls),
     ]
     ```

  3. templates : 해당 view 함수가 호출 될 때, 보여질 페이지 (templates라는 폴더에 이름.html 파일 만들기)

     ```html
     # templates 파일에 .html파일 생성
     <!DOCTYPE html>
     <html lang="ko">
     <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
     </head>
     <body>
       <h1>introduce!!!</h1>
     </body>
     </html>
     ```

     

  django extension 설치!

  repository-> json open settings에 코드 복붙

  ```python
  "files.associations": {
      "**/*.html": "html",
      "**/templates/**/*.html": "django-html",
      "**/templates/**/*": "django-txt",
      "**/requirements{/**,*}.{txt,in}": "pip-requirements"
  },
  "emmet.includeLanguages": {"django-html": "html"},
  ```

  ```python
  # settings.json
  
  {
      "terminal.integrated.cwd": "${workspaceFolder}",
      "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
      "window.zoomLevel": 1,
      "editor.fontFamily": "Hack, Fira Code, Consolas, 'Courier New', monospace",
      "[html]": {
          "editor.tabSize": 2
      },
      "[css]": {
          "editor.tabSize": 2
      },
      "[django-html]": {
          "editor.tabSize": 2
      },
  
      "files.associations": {
          "**/*.html": "html",
          "**/templates/**/*.html": "django-html",
          "**/templates/**/*": "django-txt",
          "**/requirements{/**,*}.{txt,in}": "pip-requirements"
      },
      "emmet.includeLanguages": {"django-html": "html"},
  
      "beautify.language": {
          "js": {
          "type": ["javascript", "json"],
          "filename": [".jshintrc", ".jsbeautifyrc"]
          // "ext": ["js", "json"]
          // ^^ to set extensions to be beautified using the javascript beautifier
          },
          "css": ["css", "scss"],
          "html": ["htm", "html", "django-html"]
          // ^^ providing just an array sets the VS Code file type
      }
        
  }
  ```

- view - image

- image.html

- 랜덤 이미지 띄우기

- picsum.photos/500/500.jpg

## 1. Django Template Language (DTL)

- django template에서 사용하는 내장 template system 이다.
- 조건, 반복, 변수 치환, 필터 등 많은 기능을 제공한다.
- 

## 2.

## 3.

## 4.

## 5.


# 1. 가상환경 만들기

- 폴더 안에서...

- git bash -> python -m venv venv

- vscode 에서 `F1`->python interpreter 에서 venv로 설정

- update 하기

- pip install django

- source venv/Scripts/activate => 가상환경 켜기

- pip list 로 가상환경인지 아닌지 확인하기!

- django-admin startproject classroom . (프로젝트 생성)

  

# 2. 앱만들기

- python manage.py startapp pages (앱 이름은 복수형으로 만들기!!)

- settings.py의 INSTALLED_APPS에 'pages.apps.PagesConfig', 를 등록!!! (pates라는 폴더의 apps.py에 pages를 등록)

- 프로젝트에 templates 파일 생성 후 base.html 생성

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    {% block css %}
    {% endblock %}
  </head>
  
  <body>
    <h1 class="text-center">Template Inheritance</h1>
    <hr>
    <div class="container">
      {% block content %}
        <!--여기에 들어오는 순간 base.html의 모든 속성, 부트스트랩 가져가게 됨-->
      {% endblock %}
    </div>
  
  
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
      integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
      integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
    </script>
  </body>
  
  </html>
  ```

- views 에서 함수생성

- urls.py (프로젝트) 에서 등록(from 앱이름 import views)

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('pages/', include('pages.urls')),
      path('admin/', admin.site.urls),
  ]
  ```

- urls.py (앱)을 만든 후

  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('push/', views.push),
      path('pull/', views.pull),
  ]
  ```

- 앱에서 templates 폴더 생성

- templates안에 앱 이름과 동일한 폴더 생성 후 html 파일 만들기

  ```html
  {% extends 'base.html' %}
  {% block content%}
  
  <!--내용 -->
  
  {% endblock %}
  ```

- python manage.py runserver로 열기



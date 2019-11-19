# vue & django

https://github.com/jpadilla/django-rest-framework-jwt

https://jpadilla.github.io/django-rest-framework-jwt/

https://github.com/adamchainz/django-cors-headers#setup

``` bash
$ cd todo-back/
$ source venv/Scripts/activate
$ pip list
$ pip install djangorestframework
$ pip install djangorestframework-jwt
$ pip install django-cors-headers

```

```python
# settings.py
import datetime

INSTALLED_APPS = [
    'todos',
    'rest_framework',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# DRF jwt 설정
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    # JWT 를 encrypt 함. 절대 외부 노출 금지!
    'JWT_SECRET_KEY': SECRET_KEY,
    # 토큰 해싱 알고리즘 (default: HS256)
    'JWT_ALGORITHM': 'HS256',
    # 7일간 유효한 토큰
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 토큰 갱신 허용 여부
    'JWT_ALLOW_REFRESH': True, 
    # 28일마다 토큰 갱신됨(유효기간 연장시)
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28), 
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ORIGIN_WHITELIST = [
]
# 모든 요청을 허용하도록 설정
CORS_ORIGIN_ALLOW_ALL =  True
```

```python
# todoback/urls.py

from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
]
```

- 장고 모델링 시작

  ```python
  # models.py
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  from django.conf import settings
  # Create your models here.
  # 커스텀한 유저모델 사용
  class User(AbstractUser):
      pass
  
  class Todo(models.Model):
      # 1:N 관계
      user = models.ForeignKey(settings.AUTH_USER_MODEL, 		on_delete=models.CASCADE)
      title = models.CharField(max_length=50)
      completed = models.BooleanField(default=False) # default 값 설정 필요
  
      def __str__(self):
          return self.title
  
  # settings.py
  AUTH_USER_MODEL = 'todos.User' # 기본값은 auth.User
  ```

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  $ python manage.py createsuperuser
  ```



- vue-session
  - this.$session.start()
    - session-id 초기화. 만약 세션이 없이 저장하려고 하면 vue-session 플러그인이 자동으로 새로운 세션을 시작
  - this.$session.set(key,value)
    - session 에 해당 key 에 맞는 값을 저장
  - this.$session.has(key)
    - key(JWT)가 존재하는지 여부를 확인 
  - this.$session.destroy()
    - 세션을 삭제

https://www.npmjs.com/package/vue-session

```bash
$ npm i vue-session
```

```js
// main.js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'

Vue.config.productionTip = false
Vue.use(VueSession)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```

## 흐름

### 0. Django

- 회원가입

### 1. Vue -> Django

- 로그인 정보(credentials)를 django 서버로 보냄

### 2. Django

- Vue 에서 받은 유저정보에 해당하는 고유한 Web Token 발급

### 3. Django -> Vue

- 해당 유저에 대한 토큰을 Vue로 보냄

### 4. Vue

- Django 에서 받은 토큰을 vue-session 을 통해 저장 (이 시점부터 vue 에서는 로그인 성공 상태)

### 5. Vue -> Django

- vue-session에 저장된 토큰을 가지고 django 에 로그인 요청 ( 아직 장고에서 로그인 안됨)

### 6. Django

- 최초로 보낸 토큰과 일치하는지 여부를 확인 (장고 세션 에 저장된 토큰 == 요청자의 토큰 이면 로그인 시켜줌)

--------------------------------------

`.start()` 를 통해 `session-id`: `sess`+`Date.now()`가 만들어짐

`.set()`을 통해 `jwt: jwt 값`이 만들어짐

-------------------------

## Vue의 라이프사이클

### 1. Vue instance 생성(create)

### 2. DOM에 부착(mounted)

### 3. 업데이트(Update)

### 4. 사라짐(Destroy)

##  

https://www.django-rest-framework.org/api-guide/views/

## FormData

- 기존 키에 새로운 값을 추가하거나 키가 없는 경우 새로운 키를 추가. (`FormData.append()`)
- `FormData.append(name, value)`
- name: value에 포함되는 데이터 필드 이름
- value: 필드 값


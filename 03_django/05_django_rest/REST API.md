# REST API

- API : Application Programming Interface
- 정해진 형식으로 요청 보내면 요청한 정보를 받을 수 있는 소통방법(어플리케이션 끼리 소통방법)
- 명시적인 주소
- 반드시 지켜야 하는 것은 아님...권장사항
- 

https://www.django-rest-framework.org/

- ```
  pip install djangorestframework
  ```

```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```



- dumpdata

https://docs.djangoproject.com/en/2.2/ref/django-admin/#dumpdata

 ```bash
python manage.py dumpdata --indent 2 musics > dummy.json
 ```

- fixture

  - 데이터베이스의 직렬화(serialized)된 내용을 포함하는 파일 모음이다.
  - 각 fixture는 고유한 이름을 가지며, 이를 구성하는 파일은 여러 응용 프로그램에서 여러 디렉토리에 배포 될 수 있다.
  - django 는 `loaddata` 시 설치된 모든 app 에서 `fixtures` 라고 이름의 폴더를 찾는다.

  ```
  musics/
  	fixtures/
  		musics/
  			dummy.json
  ```

- ```
  python manage.py loaddata musics/dummy.json
  ```

  

https://www.django-rest-framework.org/api-guide/views/



https://github.com/axnsan12/drf-yasg
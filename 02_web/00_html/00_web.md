# 01_Web

- static과 dynamic의 차이!

  static web

  댓글기능이 없는 블로그 등..(github.io, .....)

  dynamic web

  글을 쓰면 새글이 올라옴(변화있음)

- URI : 통합자원 식별자
- URL : 네트워크 상에서 자원이 어디 있는지를 알려주기 위한 고유 규약

- HTML 

  - HYPER TEXT : 페이지 상 링크가 걸림, 링크누르면 다른페이지로 넘어감.(정해진 길이 아닌 다양한 길로 연결됨.)

  - Markup : 
  - Language : html은 프로그래밍 언어 아님!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 연산, 반복, 조건문 안됨, 단순히 문서를 보여주기 위한 도구일 뿐
  - css: 프로그래밍 언어 아님!!!!!!!!!!!!!!!!!!!!!! 색을 입히는 역할함.
  - java script: 웹표준( 얘는 프로그래밍 언어임!) 

- 웹표준은 아직까지도..W3C에서 만들지만 앞으로는 WHATWC에서 만들 예정

- 익스플로어는 왜 브라우저가 아닌가....(왜 안쓰는가...)

  - 웹표준을 지키지 않음.....
  -  모바일 대응을 하지 않음
  - 성능 개선이 없음...느림...

- 모든 사용자가 같은 브라우저는 사용하는게 아니기 때문에 IE(EXPLORE)에도 어느정도 대응을 해야한다.(Cross Browsing)



## 1. HTML 문서의 기본 구조

- OPEN GRAPHIC : 페이스북이 처음 만들었지만 네이버 블로그나 카카오톡 등에서 더 많이 씀
- 

### 1) 스타일가이드

- 들여쓰기는 2칸

- 속성 값들은 " "만 사용하기!

- 태그, 속성, 속성값 등에는 모두 소문자를 사용!

-  최상위 html 태그에는 lang 속성을 주어 문서의 기본 언어를 지정한다.(스크린리더는 lang을 통해 언어를 인식하여 자동으로 음성을 변환하거나 해당 언어에 적합한 발음을 제공한다.) _ 접근성을 위한 것임

- IE 는 특정 META 태그를 사용해 페이지가 특정버전에 맞게 세팅되도록 지정해준다.

- ```python
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  ```

- 속성명들의 =은 붙여쓴다

- boolean 속성값은 따로 명시하지 않는다.

```html
<!-- bad -->
<input type="radio" name="menu" value="1" checked=True>

<!-- good -->
<input type="radio" name="menu" value="1" checked>
```



## 2. dom tree

- ctrl + / : 주석
- ctrl + l : 다음줄 이동
- 요소(element) : <h1> </h1>
- 닫는태그 없는 애들도 있음
- 속성 : 
- div => 공간만 분할할 뿐 의미 없음 클래스 작성하기 위해 사용, 코드의 가독성 좋아지게 할 뿐...
- 시맨틱 태그 : 의미있는 정보의 그룹을 태그로 표현, 특정 기능이 있는 것은 아님!!!!(div와 동일)
- 검색엔진 최적화 : 시맨틱 태그로 했을 때 최적화 되어 검색시 제일 상단에 나온다.



* 설치

open in browser 설치

beautify 설치 ->ctrl+shift+p->shortcut-> beautify selection->ctrl+alt+b로 단축기 설정



alt+shift+방향키 : 위나 아래에 복사

ctrl + alt + 아래키 : 선택




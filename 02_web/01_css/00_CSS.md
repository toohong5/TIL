# 02_CSS

## 1. CSS

- cascading : 떨어져 내리는
- html(구조)로 만들고 예쁘게 포장해주는 역할
- 프로그래밍 언어 아님!!
- html과 별개의 언어임.
- css는 독자적으로 사용할 순 없음.

### 1) 기본 사용법

- selector{선언 1; 선언2;}

  => h1{color: blue; font-size: 15px;}

### 2) CSS 활용하기

#### 1. Inline(인라인)

- html에 css바로 넣는방법

#### 2. Embedding(내부참조)

- html에 css넣는다.
- head의 style안에 설정을 넣는다.

#### 3. link file(외부참조)

- html파일과 별개의 파일을 만들어 연결시킴.

=> 혹시 3개의 방법을 한 h1에 적용시키면...1, 2, 3순으로 적용됨

=> 스타일 적용 우선순위 : Inline -> Embedding -> link file

=> 실제 프로젝트에서 활용시 3번사용 추천(**`컴포넌트화`**로 재사용가능하게 만든다 _ 모듈나눠서 사용)



### 3) CSS의 단위

#### 1. 키워드

#### 2. 크기단위

- px사용 _ 절대단위는 아님...(디바이스별로 px크기 제각각이다..)
- % : 백분율 단위의 상대 단위. 상대적인 사이즈 설정
- em: 배수단위로 상대단위이다. 상대적인 사이즈 설정, 1.2em은 달라질 수 있음.
- rem: 최상위 요소의 사이즈를 기준으로 삼는다. 부모가 html의 최상위 요소이므로 변하지 않음. 1.2rem은 변하지 않음(em보다 rem사용함)
- Viewport 단위 : 디바이스마다 다른 크기의 화면을 가지고 있기 때문에 상대적인 단위인 viewport를 기준으로 만든 단위.(항상 viewport 고려해야함)
  - vw : 너비의 1/100
  - vh : 높이의 1/100
  - vmin : 너비 혹은 높이 중 작은쪽의 1/100
  - vmax : 큰쪽의 1/100



=> 기본 폰트값은 16px임(아무 설정하지 않은 폰트)

#### 3. 색상 표현단위

##### 4. box model

- 

## 2. selector

### 1) 선택자우선순위

	0. !important
 	1. 인라인 스타일
 	2. 아이디 선택자
 	3. 클래스 선택자
 	4. 태그 선택자
 	5. 전체 선택자



## 3. css 스타일가이드

1. 들여쓰기 2문자
2. 클래스, 아이디명은 케밥케이스(kebob-case)를 사용한다.
3. 다중 선택 시 한 줄에 선택자를 하나씩 작성한다.

```css
.bold,
.yellow,
.bold {
    font_weight: bold;
}
```

4. 모든 스타일 뒤에는 ; 을 붙인다.

5. 스타일 지정 시 아이디, 태그 대신에 `클래스`를 사용한다. (되도록, 대부분) _ 클래스 사용을 추천!!

6. 숫자 0 이후에는 불필요한 단위를 작성하지 않는다.

7. `@import` 대신 <link> 방법을 사용한다.

8. 가능한 한 단축어(축약형)를 사용한다.

   (단, 불필요하게 과용하는 것을 피한다.)



## 4. box model

- padding

- margin : 박스의 바깥쪽

- border : 태두리 두깨, 스타일, ....상하좌우 조절 가능

- shorthand : 단축키사용

  ```css
  margin: (상/하/좌/우)
  margin : 상 우 하 좌
  margin: (상/하) (좌/우)
  .margin-3{
  	margin: 10px(상) 20px(좌/우) 30px(하);
  }
  
  .border{
      border: width style color;
  }
  ```

  - emmet

  ```css
  div>ol>li*3
    <div>
      <ol>
        <li></li>
        <li></li>
        <li></li>
      </ol>
    </div>
  
  div#apge>(header>ul.first>li.item$$@3{hi, there}*5>a{link})+footer>p>lorem
    <div id="apge">
      <header>
        <ul class="first">
          <li class="item03">hi, there<a href="">link</a></li>
          <li class="item04">hi, there<a href="">link</a></li>
          <li class="item05">hi, there<a href="">link</a></li>
          <li class="item06">hi, there<a href="">link</a></li>
          <li class="item07">hi, there<a href="">link</a></li>
        </ul>
      </header>
      <footer>
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum tempore possimus quam aperiam, reprehenderit pariatur eius earum culpa, iusto nobis esse illo molestiae dolorem ducimus facere voluptas in, veniam dolore.</p>
      </footer>
    </div>
  
  /*lorem : 더미 데이터*/
  lorem, ipsum
  ```

  

- 마진상쇄 _ 상하에서 발생

https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing

### 1) display  속성

1. block : 한줄을 다 차지함. 정렬에 이용 할 수 있음 _ div, h1~h6, p, ol, ul, table, form
2. inline : 새로운 라인에서 시작하지 않는다.  content너비 만큼 가로폭을 차지함, margin-top, margin-bottom , width, height 로 크기 지정 할 수 없음, 상하여백은 line-height로 지정한다.
3. inline-block : block과 inline 레벨 요소의 특징을 모두 갖는다. 한줄표시, 크기 설정가능.
4. None : 화면에 표시하지 않는다. (공간조차 사라진다.)

### 2) visibility

1. hidden: 박스는 없어졌지만 공간을 차지하고는 있음.

## 5. background

### 1) cover 

- 배경이미지의 크기 비율을 유지한 상태에서 부모요소의 width, height 중 큰 값에 배경 이미지를 맞춘다. 따라서 이미지의 일부가 보이지 않을 수 있다.

### 2) contain

- 배경이미지의 크기비율을 유지한 상태에서 부모 요소의 영역에 배경이미지가 보이지 않는 부분까지 전체가 들어갈 수 있도록 이미지 크기를 조절한다.

### 3) background-attachment

- 스크롤되더라도 배경이미지는 스크롤 되지 않고 고정시킨다.



## 6. font

### 1)



## 7. 위치(position)

### 1.  static

- 좌측상단 기본위치

### 2. relative

- static이었을때를 기준으로 움직인다.

### 3. absolute(절대위치)

- 부모를 찾아 올라가다가 static이 아닌 부모를 고른다. 그 부모를 기준으로 움직임.(자유롭게 움직일 수 있음)
- layout을 깨면서 움직인다(집나간 자식)
- 바로 위의 부모가 자기 부모 아닐 수 도 있음(static이면 부모 아님 그 다음 부모 찾아감.)
- 위치 잘 파악해야함
- 모든 부모가 static이면 최종적으로 html <body> tag를 부모로 선택함.

### 4. fixed(고정위치)

- 주변의 영향을 받지 않고 자기 위치만 지키고 있음.

- 같은 곳에 위치함


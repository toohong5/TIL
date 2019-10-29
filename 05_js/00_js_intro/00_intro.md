# javascript

https://nodejs.org/ko/download/

node.js설치

```bach
node -v
```



## 변수할당법

### 1. let

- 값을 재할당 할 수 있는 변수를 선언
- 단, 각 변수는 한 번만 선언 할 수 있다.(할당은 여러번 가능)
- 블록 유효범위(block scope)를 갖는다. (블록 안에서만 지역변수로서 존재한다. 밖에서는 사용 못함)

```js
// let (변수)
let x = 1

if(x === 1) {
    let x = 2
    // let x = 3으로 재선언 못함!!
    console.log(x) // 2
}
console.log(x)  // 1

// 밖과 안의 x는 서로 다른 x임!
```

### 2. const

- 값이 변하지 않는 상수를 선언하는 키워드
- 담긴 값이 불변임을 뜻하는게 아니다.(재선언과 재할당이 안될 뿐임.)
- 단지 상수의 값은 재할당 할 수 없고 재선언도 안된다.
- 블록 유효 범위(block scope)
- const 선언시에 초기값을 생략하면 오류 발생!

```js
// const (상수)
// 값이 바뀌진 않지만 불변은 아니다...
// const 선언시에 초기값을 생략하면 오류 발생!
// const MY_FAV

const MY_FAV = 7
console.log('my favorite number is: ' + MY_FAV)

// 상수를 재선언, 재할당 하려는 시도는 모두 오류 발생.
MY_FAV = 20 //재할당 할 수 없음!!
const MY_FAV = 20 //재선언도 할 수 없음!!
let MY_FAV = 20 // 재선언 못함

if (MY_FAV === 7) {
    // 블록 유효 범위로 지정된 MY_FAV 이라는 변수를 만드므로 괜찮다.
    // 즉, 전역이 아닌 범위안이므로 이름 공간에서 충돌이 나지 않는다.
    // 여기서도 const 는 재선언이 불가능하기 때문에 let으로 설정.
    let MY_FAV = 20

    console.log('my favorite number is ' + MY_FAV) // 20 -> 같은 블록 안의 let으로 재선언됨.
}
console.log(MY_FAV) // 7 -> 전역변수의 상수
```

### 3. var (변수)

- ES6 이전의 feature로 예기치 않은 문제를 많이 발생시키는 키워드로 절대 사용하지 않는다.

- 함수 유효 범위(function scope)

- var로 선언된 변수의 범위는 현재 실행 문맥인데, 그 문맥이 함수 혹은 함수 외부의 전역으로도 갈 수 있다.

  ```JS
  // var (변수)
  function varTest() {
      var x = 1
      if (true) {
          var x = 2 // 재할당
          console.log(x) // 2,  상위 블록과 같은 변수
      }
      console.log(x) // 2 -> 서로 같은 공간에 존재
  }
  
  function letTest() {
      let x = 1
      if (true) {
          let x = 2 //재할당
          console.log(x) // 2 -> 상위 블록과 다른 변수
      }
      console.log(x) // 1 -> 서로 다른 블록에 있음.
  }
  letTest()
  
  // let과 var
  var a = 1
  let b = 2
  if (a === 1) {
      var a = 11
      let b = 22
  
      console.log(a) // 11 위의 a와 동일. a가 1->11로 바뀜
      console.log(b) // 22  
  
  }
  console.log(a) // 11, var은 함수 밖에도 영향을 미친다.
  console.log(b) // 2
  ```

  

--------------------

- 어디에 쓸지 결정하는건 프로그래머의 몫
- `PI`, `DAYS_IN_JUNE` 과 같은 경우는 상수가 적절
- `WEATHER_TEMP` 처럼 모호한 경우(각자가 생각하는 좋아하는 기온이 다를 수 있으니까..) 이런경우엔 변수가 적절.

----

일단 모든 선언에서 가능한한 상수(const)를 사용해야한다.

먼저 상수를 생각하고 값이 바뀌는 것이 더 자연스러운 상황이라면, 그때 변수로 바꿔서 사용하는 것을 권장.

----------

- 정리
  - var : 할당 및 선언이 자유 / 함수 스코프
  - let : 할당 자유 / 선언은 한번만 / 블록 스코프
  - const : 할당 및 선언 모두 한번만 / 블록 스코프

----

## 식별자(identifier)

- 변수명은 식별자라고 불리며 특정 규칙을 따른다.

1. 반드시 문자, 달러($), 또는 밑줄로 시작해야 한다. 이후는 숫자도 가능.
2. 대소문자를 구분하며 클래스명을 제외하고는 대문자로 시작하지 않는 것이 좋다.
3. 예약어는 사용 불가능(class, super, const, case, function, ....)



## 호이스팅(hoisting)

- 이 개념은 JS 변수, 함수나 표현이 최상단으로 올려지는 것을 말한다.
- 끌어 올려진 변수는 `undefined` 값을 반환한다.
- 변수와 함수를 위한 메모리 공간을 확보하는 과정.

----------------------------------------

### var 할당 과정

var x = 1

1. 선언 + 초기화
2. 할당

### let 할당과정

1. 선언
2. TDZ(Temporal Dead Zone, 임시적 사각지대)
3. 초기화
4. 할당



```js
console.log(a) // error가 아닌 undefined로 나옴...
var a = 10  // 선언만 제일 위로 올림...할당은 밑에서..
console.log(a)

// JS가 이해한 코드
var a // 선언 + 초기화 함께 이루어짐
console.log(a) // undefined
a = 10 // 할당
console.log(a) // 10
//----------------------------------------------------------------------
// let은 안된다...ReferenceError
console.log(b)
let b = 10
console.log(b)

// 마찬가지로 아래와 같은 과정을 거친다.
let b // 선언 + TDZ (초기화 안됨..)
console.log(b)
b = 10  // 할당 불가 (초기화가 아직 안됨)
console.log(b)
// 왜 안되지?

if (x != 1) {
    console.log(y) // undefined
    var y = 3
    if (y === 3) {
        var x = 1
    }
    console.log(y)  // 3
}

if (x === 1) {
    console.log(y) // 3
}

// JS 가 이해한 코드
var x
var y

if (x != 1) {
    console.log(y) // undefined
    var y = 3   // 할당
    if (y === 3) {
        var x = 1
    }
    console.log(y)  // 3
}

if (x === 1) {
    console.log(y) // 3
}
```



-------

let, const 의 정의가 평가되기까지 초기화가 되지 않는다는 의미이지, 호이스팅이 되지 않아 정의가 되지 않는다는 의미와는 다르다.

Barbel 로 ES6+ 문법을 그보다 아래 버전의 JS로 변경해서 사용하기도 한다.(down grade)

## 

## 타입과 연산자

### 1. 타입

1. Primitive
2. Reference

### 2. Primitive

- 불변하다는 특징을 띄고 있다.

1. Numbers

   - `Infinity` : 양의 무한대와 음의 무한대로 나뉨
   - `NaN` : Not a Number, 표현할 수 없는 값, 자기 자신과 일치하지 않는 유일한 값을 표현
     - 0/0, "문자"*10, Math.sqrt(-9)

   ```JS
   // Number
   const a = 13
   const b = -3
   const c = 3.14 // float
   const d = 2.998e8 // 2.998 * 10^8 = 299,800,000
   const e = Infinity
   const f = -Infinity // 음의 무한대
   const g = NaN // Not a Number
   
   console.log(a, b, c, d, e, f, g)
   ```

   

2. Strings

   ```js
   // String
   const sentence1 = 'sentence'
   const sentence2 = "sentence"
   const sentence3 = `sentence`
   
   // backtick(`)
   // const word = "안녕
   // 하세요"
   // 엔터 하면 오류남
   // console.log(word)
   
   const word1 = "안녕 \n 하세요"
   console.log(word1)
   
   const word2 = `안녕
   하세요`
   console.log(word2)
   ```

   

3. Booleans

4. Empty Value

-------------

### Literal

- 값을 프로그램 안에서 직접 지정한다는 의미
- 값을 만드는 방법
- JS는 우리가 제공한 리터럴 값을 받아 데이터를 만듦

```js
// room 변수를 가리키는 식별자 / 'conference_room'(따옴표 안) 은 리터럴
let room = 'conference_room'

let hotelRoom = room

// 에러, conference_room 식별자는 존재하지 않는다.
hotelRoom = conference_room
```

- JS 는 따옴표를 통해 리터럴과 식별자는 구분한다.
- 식별자는 숫자로 시작할 수 없으므로 숫자에는 따옴표가 필요없다.(숫자형 리터럴)

```js
// Template Literal
// JS 에서 문자열을 입력하는 방식.
const age = 10
const message = `홍길동은 ${age}
살입니다.`
console.log(message)

const happy = 'hello'
const hacking = 'world' + 'lol' + '!!!'
console.log(happy, hacking)
```



### `null` // `undefined`

- 동일한 역할을 하는 이 2개의 키워드가 존재하는 이유는 단순한 JS의 설계 실수.
- 큰 차이를 두지 말고 interchangerable 하게 사용할 수 있도록 권장.

`undefined` 

- 값이 없을 경우 JS가 자동으로 할당 해주는 값

  ```JS
  let first_name // 선언만 하고 할당하지 않음. 
  console.log(first_name) // undefined
  ```

`null`

- 값이 없음을 우리가 표현하기 위해서 인위적으로 사용하는 값

  ```js
  let last_name = null
  console.log(last_name) // null - 의도적으로 값이 없음을 표현
  ```

```js
// Number.isNaN() 함수는 값이 NaN 인지 여부를 판별.
// 주어진 값의 유형이 Number이고 값이 NaN이면 true
Number.isNaN(1 + null) // false (숫자임)
Number.isNaN(1 + undefined) // true (숫자가 아님)

Number.isNaN(null) // false
Number.isNaN(undefined) // false
```


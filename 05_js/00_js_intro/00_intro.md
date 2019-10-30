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
- 선언만 최상단으로 끌어올린다.

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



### 연산자

- 일치연산자 : 

- `&&` : and 연산자 (뒤까지 확인)
- `||` : or 연산자 (앞이 true면 뒤까지 확인 안함)
- `!` : not 연산자

- `삼항연산자` : true ? 1 : 2 => `:` 기준으로 true면 왼쪽 false면 오른쪽을 리턴

  ```js
  const result = Math.PI > 4 ? 'yes!':'no!' // no! 가 리턴됨 
  ```

- if

  ```js
  if (userName === '1q2w3e4r') {
  	message = '<h1>This is admin page</h1>'
  } else if (userName === 'ssafy') {
  	message = '<h1>You are from ssafy</h1>'
  } else {
  	message = `<h1>hello ${userName}</h1>`
  }
  
  
  // switch
  switch(userName) {
      case '1q2w3e4r' : {
  		message = '<h1>this is admin</h1>'
      }
      case 'ssafy' : {
  		message = '<h1>you r from ssafy</h1>'
      }
      default: {
  		message = `<h1>hello ${userName}</h1>`
      }
  }
  //"<h1>hello 1q2w3e4r</h1>"
  // switch는 특정 조건을 만족하면 멈춰야하는데 그렇지 않음... break문을 주어야 한다.
  switch(userName) {
      case '1q2w3e4r' : {
  		message = '<h1>this is admin</h1>'
  		break
      }
      case 'ssafy' : {
  		message = '<h1>you r from ssafy</h1>'
  		break
      }
      default: {
  		message = `<h1>hello ${userName}</h1>`
  		break
      }
  }
  
  // "<h1>this is admin</h1>"
  
  
  ```




## 함수

- 함수도 값이다..typeof(func) => function

### 1. 선언식(statement, declaration)

- 코드가 실행되기 전에 로드된다.

```js
// 미리 로드시켜 놓음
function add(num1, num2) {
    return num1 + num2
}

add(2, 7)
console.log(add(2,7)) // 9
```

### 2. 표현식(expression)

- 함수 표현식은 인터프리터가 해당 코드에 도달 했을 때 로드된다.

```js
// 이름없는 함수를 변수에 할당
// 만난 순간에 로드시킴
const sub = function (num1, num2) {
    return num1 - num2
}
console.log(sub(7, 2))
```



### 화살표 함수(Arrow Function)

- 항상 이름이 없음(익명 함수)
- 화살표 함수의 경우 일반 function 키워드로 정의한 함수와 100% 동일한 것이 아니다.
- 변수에 할당할 수 있지만, 이름 붙은 함수(생성자)로는 만들 수 없다. (할당가능, 이름 못가짐)

## DataStructure

### 1. 배열

```js
const numbers = [1, 2, 3, 4,]

console.log(numbers[0])
console.log(numbers[-1]) // undefined : 정확한 양의 정수 index 만 가능!
console.log(numbers.length) // 4

// 원본 파괴
console.log(numbers.reverse())
console.log(numbers)
console.log(numbers.reverse()) // 원상복귀 됨.
console.log(numbers)

// push -> 값 추가, 배열의 길이를 return 함
console.log(numbers.push('a')) // 5 -> 리턴값이 배열의 길이임
console.log(numbers)

// pop -> 배열의 가장 마지막 요소 제거 후 return
console.log(numbers.pop())
console.log(numbers)

// unshift -> 배열의 가장 앞에 요소를 추가하고 배열의 길이를 return
console.log(numbers.unshift('a'))
console.log(numbers)

// shift -> 배열의 가장 앞 요소를 제거 후 return
console.log(numbers.shift())
console.log(numbers)

// includes -> 해당 요소가 배열에 포함되어 있으면 true/ 없으면 false를 return
console.log(numbers.includes(1))
console.log(numbers.includes(0))

console.log(numbers.push('a', 'a'))
console.log(numbers)
console.log(numbers, indexOf('a')) // 4 => 중복이 존재한다면 처음 찾은 요소의 index를 return
console.log(numbers, indexOf('b')) // -1 => 찾고자 하는 요소가 없으면 -1을 return

// join - 배열의 요소를 join 함수의 인자를 기준으로 이어서 문자열로 return / 원본은 변화 없음
console.log(numbers.join()) // '1,2,3,4,a,a' -> ()에 아무것도 넣지 않으면 `,`를 기준으로 가져온다.
console.log(numbers.join('')) // '1234aa'
console.log(numbers.join('-')) // '1-2-3-4-a-a'

console.log(numbers) // 원본은 변화하지 않음
```



### 2. 객체

```js
// 객체
const me = {
    name: 'ssafy',
    'phone number': '01012345678', // key 가 여러단어 일 때
    appleProducts : {
        ipad: '2018pro',
        iphone:'7',
        macbook:'2019pro',
    }
}

console.log(me.name) // ssafy
console.log(me['name']) // ssafy
console.log(me['phone number']) // 키가 여러단어 인 경우 무조건 [] 로 접근!!
console.log(me.phone_number)

console.log(me.appleProducts)
console.log(me.appleProducts.ipad)

// Object Literal (객체 표현법)
var books = ['Learning JS', 'Eloquent JS'] // 배열

var comics = {
    'DC': ['Joker', 'Aquaman'],
    'Marvel': ['Captin Marvel', 'Avengers']
} // 객체

var megazines = null

var bookShop = {
    books: books,
    comics: comics,
    megazines: megazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

// ES6+
// object 의 key와 value가 같다면, 마치 배열처럼 한번만 작성 가능
var bookShopTwo = {
    books,
    comics,
    megazines,
}
console.log(bookShopTwo)
```



### 3. JSON(JS Object Notation, JS 객체 표기법)

- KEY-VALUE 형태의 자료구조를 JS 객체와 유사한 모습으로 표현하는 표기법
- 모습만 비슷할 뿐이고 실제로 Object 처럼 사용하려면 다른 언어들 처럼  JS 에서도 Parsing(구문 분석) 작업이 필요하다.

```JS
// JSON -> trailing comma 사용못함..(객체에서만 가능)
const jsonData = JSON.stringify ({ // JSON -> String으로 바꿈..
    coffee: 'Americano',
    iceCream: 'Mint Choco',
})
console.log(jsonData) // {"coffee":"Americano","iceCream":"Mint Choco"}
console.log(typeof jsonData) // string

const parseData = JSON.parse(jsonData)
console.log(parseData) // { coffee: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof parseData) // object

```

#### 정리

- Object : JS의 key-value 페어의 자료구조
- JSON : 데이터를 표현하기 위한 **단순한 문자열**



### 4. Array Helper Method

- Helper란 자주 사용하는 로직을 재활용할 수 있게 만든 일종의 Library 다.
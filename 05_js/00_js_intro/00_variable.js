// 변수할당법
// 1. var
// 2. let
// 3.const

// let (변수)
let x = 1

if(x === 1) {
    let x = 2
    // let x = 3으로 재선언 못함!!
    console.log(x) // 2
}
console.log(x)  // 1

// 밖과 안의 x는 서로 다른 x임!

// const (상수)
// 값이 바뀌진 않지만 불변은 아니다...
// const 선언시에 초기값을 생략하면 오류 발생!
// const MY_FAV

const MY_FAV = 7
console.log('my favorite number is: ' + MY_FAV)

// 상수를 재선언, 재할당 하려는 시도는 모두 오류 발생.
// MY_FAV = 20 //재할당 할 수 없음!!
// const MY_FAV = 20 //재선언도 할 수 없음!!
// let MY_FAV = 20 // 재선언 못함


if (MY_FAV === 7) {
    // 블록 유효 범위로 지정된 MY_FAV 이라는 변수를 만드므로 괜찮다.
    // 즉, 전역이 아닌 범위안이므로 이름 공간에서 충돌이 나지 않는다.
    // 여기서도 const 는 재선언이 불가능하기 때문에 let으로 설정.
    let MY_FAV = 20

    console.log('my favorite number is ' + MY_FAV) // 20 -> 같은 블록 안의 let으로 재선언됨.
}
console.log(MY_FAV) // 7 -> 전역변수의 상수

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


// 식별자 작성 스타일
// 1. 카멜 케이스(camelCase) - 객체, 변수, 함수 (=== lower-camel-case)
let dog
let variableName

// 배열은 복수형 변수명을 사용
const dogs = []

// 정규 표현식은 'r' 로 시작
const rDecs = /.*/

// 함수
function getPropertyName() {
    return 1
}

// boolean 을 반환하는 변수나 함수 - 'is' 로 시작
let isAvailable = false

// 2. 파스칼 케이스 (PascalCase) - 클래스, 생성자 (=== upper-camel-case)
class User {
    constructor(options) {
        this.name = option.name
    }
}

// 3. 대문자 스네이크 케이스(SNAKE_CASE) - 상수
// 이 표현은 변수와 변수의 속성이 변하지 않는다는 것을 프로그래머에게 알려준다.
const API_KEY = 'avcdseasr'

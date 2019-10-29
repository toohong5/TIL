console.log(a) // error가 아닌 undefined로 나옴...
var a = 10  // 선언만 제일 위로 올림...할당은 밑에서..
console.log(a)

// JS가 이해한 코드
var a // 선언 + 초기화 함께 이루어짐
console.log(a) // undefined
a = 10 // 할당
console.log(a) // 10

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
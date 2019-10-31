// function sleep_3s() {
//     setTimeout(() => console.log('wake up'), 3000)
// }

// console.log('start sleeping') // 1. 출력
// sleep_3s()// 코드의 진행을 막지 않음...마지막에 출력됨.
// console.log('end of program') // start end 바로 나오고 3초 뒤 sleeping (3초 뒤 끝남)....

// function first() {
//     console.log('first')
// }

// function second() {
//     console.log('second')
// }

// function third() {
//     console.log('third')
// }

// first()
// setTimeout(second, 1000) // second 함수를 callback으로
// third()

console.log('Hi')
setTimeout(function ssafy() {
    console.log('ssafy')
}, 5000) // 100후에 콜백큐로 들어간다..마지막에 출력됨.
console.log('bye') // 

// 비동기 함수 사용시 처리 순서
// 1. 콜스택에 hi -> 출력해주고 -> 콜스택 나감
// 2. setTimeout 실행 -> callback호출 -> 5초 뒤에 ssafy가 콜백큐에 들어감...(5초 도는 중..)
// 3. 5초 도는 동안 bye가 콜스택에 들어감 -> 출력 -> 콜스택 나감
// 4. 콜스택이 빈 후 콜백큐의 ssafy를 콜스택으로 보냄 -> 출력 -> 콜스택 나감 -> 끝!
// 결과 : hi -> bye -> ssafy
//--------------------------------------------------------
function printHello() {
    console.log('hello from baz')
}

function baz() {
    setTimeout(printHello, 3000)
}

function bar() {
    baz()
}

function foo() {
    bar()
}

foo()

// foo호출(콜스택) -> bar 호출(콜스택) -> baz 호출(콜스택) -> setTimeout 호출(3초 돌기 시작) -> baz 끝나서 콜스택 빠짐 -> bar 빠짐 -> foo 빠짐
// -> 3초 끝난 뒤 콜백큐에서 printHello가 콜스택 빌때 까지 대기 -> 콜스택에 printHello들어감 -> 출력 -> printHello 콜스택에서 나감 -> 끝

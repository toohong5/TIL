// function doSomething(subject) {
//     console.log(`이제 ${subject} 과목평가 준비를 시작해볼까?`)
// }

// doSomething('django')

// doSomething에 콜백함수 받게하기
// 익명함수로..
function doSomething(subject, callback) {
    console.log(`이제 ${subject} 과목평가 준비를 시작해볼까?`)
}
doSomething('django', function() {
    console.log('며칠 안남았는데?')
})
// 기명함수로 해도 됨..
function alertFinish() {
    console.log('며칠 안남았는데?')
}
doSomething('django', alertFinish)

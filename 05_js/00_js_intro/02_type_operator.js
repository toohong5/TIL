// Number
const a = 13
const b = -3
const c = 3.14 // float
const d = 2.998e8 // 2.998 * 10^8 = 299,800,000
const e = Infinity
const f = -Infinity // 음의 무한대
const g = NaN // Not a Number

console.log(a, b, c, d, e, f, g)

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

// Template Literal
// JS 에서 문자열을 입력하는 방식.
const age = 10
const message = `홍길동은 ${age}
살입니다.`
console.log(message)

const happy = 'hello'
const hacking = 'world' + 'lol' + '!!!'
console.log(happy, hacking)

// Number.isNaN() 함수는 값이 NaN 인지 여부를 판별.
// 주어진 값의 유형이 Number이고 값이 NaN이면 true
Number.isNaN(1 + null) // false (숫자임)
Number.isNaN(1 + undefined) // true (숫자가 아님)

Number.isNaN(null) // false
Number.isNaN(undefined) // false


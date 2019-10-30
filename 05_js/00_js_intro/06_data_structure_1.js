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
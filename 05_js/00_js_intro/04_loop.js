// while
let i = 0

while (i < 6) {
  console.log(i)
  i++ // i 가 1씩 증가됨
}

// for
for (let j = 0; j < 6; j++) {
  console.log(j)
}

const numbers = [0, 1, 2, 3, 4, 5,]

for (let number of numbers) {
  console.log(number)
}

for (const number of [0, 1, 2, 3, 4, 5,]) {
  console.log(number)
}
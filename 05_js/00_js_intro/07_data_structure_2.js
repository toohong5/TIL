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

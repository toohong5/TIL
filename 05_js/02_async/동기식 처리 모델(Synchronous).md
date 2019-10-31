## 동기식 처리 모델(Synchronous)

- 직렬적으로 태스크를 수행
- 태스크는 순차적으로 실행되며 어떤 작업이 수행중이면 다음 작업은 대기
- 예) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때 까지 이후 태스크들은 블로킹(blocking)된다.

------

## 비동기 처리 모델(Asynchronous)

- 병렬적으로 태스크를 수행
- 태스크가 종료되지 않는 상태라 하더라도 다음 태스크를 실행
- 예) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때 까지 기다리지 않고(non-blocking) 즉시 다음 태스크를 수행
- JS 대부분의 DOM 이벤트와 Timer 함수, Ajax 요청은 비동기식 처리 모델로 동작

------

## Blocking vs non-blocking

## 이벤트 루프

- 단 한가지 **콜스택**과 **콜백큐**를 감시하는 역할을 한다.
- 만약 콜스택이 비어 있으면 이벤트 루프는 콜백큐에서 첫 번째 이벤트를 가져다가 콜스택에 밀어넣고, 결과적으로 해당 이벤트가 실행된다. 
- 이러한 반복은 이벤트 루프에서는 `tick` 이라고 한다.
- 이벤트루프는 호스팅 환경(브라우즈 or nodejs)에 내장된 매커니즘
- 이것은 시간의 흐름에 따라 코드의 수행을 처리하며 그때마다 JS 엔진을 작동시킨다.

#### setTimeout(mycallback, msecs)

- callback 함수가 1초 뒤에 실행될 것이다 라는 의미가 아니다!
- **1초 후에 콜백 큐에 추가될 것이라는 의미!**
- 만약에 콜백 큐에 callback 보다 먼저 추가된 이벤트가 있을수도 있기 때문에 실제 1초보다 더 오랜 시간이 걸릴 수도 있다.

http://latentflip.com/loupe/?code=ZnVuY3Rpb24gcHJpbnRIZWxsbygpIHsNCiAgICBjb25zb2xlLmxvZygnSGVsbG8gZnJvbSBiYXonKTsNCn0NCg0KZnVuY3Rpb24gYmF6KCkgew0KICAgIHNldFRpbWVvdXQocHJpbnRIZWxsbywgMCk7DQp9DQoNCmZ1bmN0aW9uIGJhcigpIHsNCiAgICBiYXooKTsNCn0NCg0KZnVuY3Rpb24gZm9vKCkgew0KICAgIGJhcigpOw0KfQ0KDQpmb28oKTs%3D!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D

```js
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
```

```js
function printHello() {
    console.log('hello from baz')
}

function baz() {
    setTimeout(printHello, 3000) // 0초라 해도 먼저 실행되지 않음!!
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

```

--------

## Axios

- `axiosXHR` 을 요청으로 보내고 응답 받은 결과를 `Promise 객체`로 반환 해주는 라이브러리
- axios 는 현재 JS 에서 가장 HOT 한 라이브러리 중 하나이며 프론트 엔프 프레임워크( react, vue) 에서 데이터를 주고 받을 때 필수적으로 사용되고 있음.(프론트엔프 프레임워크(vue로 함..) <-> api 서버와 통신 할때 가장 많이 사용)

```bash
$ npm install axios
```




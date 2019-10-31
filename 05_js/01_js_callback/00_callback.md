# callback

- 인수(매개변수)로 다른 함수에 전달 된 함수
- 명시적으로 호출하는 방식이 아니라 특정 이벤트가 발생했을 때 시스템에 의해 호출되는 함수
  - 다른 함수의 실행이 끝나고 난 뒤에 실행되는 함수. 이따가 너 실행 끝나면 그때 나좀 호출해줘.
- 함수의 호출권한을 내가 아닌 시스템이 가진다.

## JS 함수는 일급객체

### 1. 변수에 담을 수 있다.

### 2. 인자로 전달할 수 있다.

### 3. 반환값으로 전달할 수 있다.

- return n => n + 1

---------------------

- `setTimeout` 

  ```js
  setTimeout(function () {
      console.log('3초 후 출력됩니다.')
  }, 3000) // setTimeout( function, time )
  
  setTimeout( () => console.log('3초'), 3000)
  ```

## 비동기식 처리 모델

- 호출될 함수 (콜백함수)를 미리 매개변수에 전달하고 처리가 종료되면 콜백함수를 호출하는 것.

## 이벤트 리스너

`EventTarget.addEventListener(type, listener)`

1. 무엇을 : 이벤트 타겟 -> 버튼을 - `EventTarget`
2. 언제 : 클릭했을 때 - `type`
3. 어떻게 : 콘솔에 로그를 -`listener`
4. 한다. : 찍어라

----

## JS 코드를 body의 최하단에 위치하는 이유

1. js를 읽는 시간 때문에 body안에 있는 html 요소들이 브라우저에 그려지는게 지연될 수 있기 때문.
2. JS에서 특정 HTML 요소들을 읽고 이벤트를 등록해야 할 때, JS 코드가 먼저 해석되면 해당 요소가 없다고 인식되어 이벤트 등록이 되지 않을 수 있기 때문.

![img](https://slack-imgs.com/?c=1&o1=ro&url=https%3A%2F%2Fweb222.ca%2Fweeks%2Fweek07%2Fimages%2Fdom-tree.png)

#### querySelector 는 위에서 선택자로 요소를 찾으면 가장 먼저 찾아지는 요소를 반환(단수)

#### querySelectorAll 은 위에서부터 선택자로 요소를 찾으며 일치하는 요소들을 모두 반환(복수)

```js
// 삭제
// 1. 부모에 담아서 삭제
// 2. 첫번째, 마지막 자식요소 삭제


// 3.특정 자식요소 선택해 삭제
const bg = document.querySelector('.bg') // 부모요소 가져오기
const dino = document.querySelector('#dino') // 자식요소 가져오기
bg.removeChild(dino)


// 생성
const dino =document.querySelector('#dino')
const newDino = document.createElement('img')
newDino.src = 'https://pbs.twimg.com/profile_images/770139154898382848/ndFg-IDH_400x400.jpg'
newDino.alt = 'dino'
newDino.id = 'dino'
newDino.style.width = '100px'
newDino.style.height = '100px'
// 저장
const bg = document.querySelector('.bg') // 부모선택
bg.append(newDino) // 저장

```



https://developer.mozilla.org/ko/docs/Web/Events

eventListener


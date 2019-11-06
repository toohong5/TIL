## webpack

- 웹팩은 현재 가장 널리 쓰이는 **모듈 번들러**.
- JS 뿐만 아니라,  CSS, IMAGE 파일 등 리소스의 의존성들도 관리한다.

## 모듈

- 어플리케이션을 구성하는 개별적 요소
- 재사용 가능한 코드 조각
- 모듈은 세부사항을 캡슐화한다.
- 특정 기능을 갖는 작은 코드 단위

```javascript
// module.js -> 이 파일을 모듈로 사용
fuction sum(a, b) {
    return a + b
}
fuction sub(a, b) {
    return a + b
}
fuction mul(a, b) {
    return a + b
}

// test.js
import * as lib from './module' // module.js에서 가져옴..
//import { sum, mul } from '.module' // 일부만 가져오기

console.log(lib.sub) // lib.sum, lib.sub, lib.mul로 가져올 수 있음.
```



## 모듈 번들러

- 웹 어플리케이션을 구성하는 자원(HTML, CSS, JS, IMG 등)을 모두 각각의 모듈로 보고 이를 조합해서 병합된 하나의 결과물로 만드는 도구 -> 가장 널리 쓰이는게 웹팩!!

-----

웹팩을 왜 사용하는가..

- 개발을 편하게 모듈 단위로 개발 -> 모듈끼리 연결(의존성)을 신경쓰기 어려워짐 -> 웹팩아 하나로 만들어줘! (웹팩(모듈 번들러)이 대산 하나로 만들어 줌!)



```bash
$ npm init # package.json파일 생성
$ npm install vue # node_modules/vue 폴더 생성
$ npm install webpack webpack-cli -D # 웹팩 설치

# webpack.config.js 파일 만들기 (웹팩 설정파일)
```

### 웹팩의 구조

#### 1. entry (시작) -> `main.js`

- 여러 js 파일들의 시작점 -> 웹팩이 파일을 읽어 들이기 시작하는 부분 (main.js)

```javascript
// main.js

// Vue 인스턴스를 최종으로 만드는 파일
// entry로 읽어들이는 역할을 함.
// 1. 설치된 vue를 추가 (node_modules/vue)
// (내가 만든 파일 아닌 경우 -> install 한 경우) 현재 위치에서 vue 이름을 가진 폴더가 없음 => 자동으로 node_modules 에서 가져옴.
import Vue from 'vue'

// 2. 최상위 컴포넌트 추가
// (내가 만든 파일) 상대 경로 표시 해야함
import App from './App.vue'

new Vue({
    render: h => h() //createElement -> h로 줄여서 사용함
}).$mount('#app') // el과 같은 기능임. 더 유용하게 사용 가능
```



#### 2. module -> javascript외에 모듈 설정해줌

- 웹팩은 JS만 변환 가능하기 때문에 html, css 등은 모듈을 통해서 웹팩이 이해할 수 있도록 변환이 필요하다.
- 변환 내용을 담는 곳



#### 3. plugins

- 웹팩을 통해서 번들된 결과물을 추가 처리하는 부분

#### 4. output

- 여러 js 파일을 **하나로 만들어 낸 결과물**

------

웹팩은 js 코드만 이해가능하기 때문에 vue파일 (vue-loader 설치) 및 html, css 파일(`vue-template-compiler`) 등을 변환하기 위하여 모듈을 설치

```bash
$ npm install vue-loader vue-template-compiler -D

$ npm run build
```

---------------

최상위 컴포넌트(App.vue)

하위 컴포넌트(TodoList.vue)

--------

### 컴포넌트 등록 3 steps (App.vue _ 최상위)

1. `<script>` 에 등록할 컴포넌트 불러오기 (import)
2. `export default` 에 `components` 항목에 등록
3. `<template>` 에서 컴포넌트 사용할 수 있도록 작성

```bash
$ npm install vue-style-loader css-loader -D # css 파일 로더
```


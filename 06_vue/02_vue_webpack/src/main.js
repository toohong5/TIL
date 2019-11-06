// Vue 인스턴스를 최종으로 만드는 파일
// entry로 읽어들이는 역할을 함.
// 1. 설치된 vue를 추가 (node_modules/vue)
// (내가 만든 파일 아닌 경우 -> install 한 경우) 현재 위치에서 vue 이름을 가진 폴더가 없음 => 자동으로 node_modules 에서 가져옴.
import Vue from 'vue'

// 2. 최상위 컴포넌트 추가
// (내가 만든 파일) 상대 경로 표시 해야함
import App from './App.vue'

new Vue({
    render: h => h(App) //createElement -> h로 줄여서 사용함
}).$mount('#app') // el과 같은 기능임. 더 유용하게 사용 가능
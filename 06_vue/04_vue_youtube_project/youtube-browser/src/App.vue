<template>
  <div id="app">
    <!-- 2. 사용하겠다 선언 -->
    <!-- 3. SearchBar.vue 에서 올 이벤트 기다림. -->
    <!-- 만약 inputChange 이벤트가 일어나면 onInputChange 라는 method 가 실행 됨-->
    <search-bar @inputChange="onInputChange"></search-bar>
    <div class="row">
      <video-detail :video="selectedVideo"></video-detail>
      <!-- v-bind를 이용해 VideoList.vue로 데이터 내려줌/ :videos="videos" => 넘겨주는 키값:데이터 -->
      <vidio-list @videoSelect="onVideoSelect" :videos="videos"></vidio-list>
    </div>
  </div>
</template>

<script>
 // 0. 새로운 컴포넌트 import 하기
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VidioList from  './components/VideoList'
import VideoDetail from './components/VideoDetail'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY // key값 가져옴
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
export default {
  name: 'App', // 최상단 컴포넌트이기 때문에 이름이 없어도 되지만 명시적으로 작성한다.(생략도 가능함)
  data() {
    return { // object를 리턴하는 함수!!
        // Vue component 에서는 반드시 Object 를 return 하는 함수로 작성!!
        // component에서는 return 을 한번 더 {} 해줘야 다른 component 들과 독립적인 배열 생성가능.
        videos: [],
        selectedVideo: null,
    }
  },
  components: {
    // 1. 컴포넌트 등록하기
    SearchBar, // 원래는 SearchBar: SearchBar 로 작성.
    VidioList,
    VideoDetail,
  },
  // 4. methods 만들기
  methods: {
    onVideoSelect(video) {
      this.selectedVideo = video
    },
    onInputChange(inputValue) { // inputValue : $emit으로 들어온 input 값
      axios.get(API_URL, { // data
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,// 입력하는 값
        }
      })
      .then(response => {
        this.videos = response.data.items // 영상정보 목록이 저장됨.
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style>

</style>
# vue_youtube

```bash
# 프로젝트 생성
$ vue create youtube-browser
$ cd youtube-browser
$ npm run serve
```

<hr>

```json
// package.json에서 설정..서버 껐다가 켜기

"eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/essential",
      "eslint:recommended"
    ],
    "rules": {
      "no-console": "off"
    },
    "parserOptions": {
      "parser": "babel-eslint"
    }
  },
```

### 단방향 데이터 흐름의 이점

1. vue app의 데이터 흐름을 쉽게 파악할 수 있음

2. 부모 컴포넌트에서 업데이트가 일어나면 자식컴포넌트는 자동 업데이트(즉, 자식 컴포넌트의 상태를 관리하지 않아도 된다.)

3. 하위 컴포넌트가 실수로 부모의 상태를 변경하려 app 데이터의 흐름을 추론하기 어렵게 만드는 것을 방지할 수 있다.

   

- 하위에서 상위로 데이터를 올려 보낼 때는 Event 를 발생시키는 방법을 사용한다. (`emit`) -> 상위가 알아챌 수 있게 event 발생시킴.
- `props` 는 배열, 객체, 함수 등 무엇이든 내려보내는 **속성(properties)**이고, `emit event` 는 자식에서 부모로 **이벤트를 발생** 시키는 것



### SearchBar => App

1. 트리거 : input 값 변경(@input)
   - 인자 : event
   - 실행 함수 : onInput
2. 트리거 : input 내 $emit (inputChange)
   - 인자 : 변경된 값
   - 실행 함수 : onInputChange -> 최종변경된 값을 출력

## 진행 flow

### `SearchBar.vue`

1. 사용자가 검색어 입력(SearchBar에서..) 하면 onInput 함수가 실행

- 검색 결과를 `App.vue` 로 올려줘야함.(검색된 정보를 최상위로 올린 뒤(emit events) props로 다른 컴포넌트들에 내려줘야한다) : 자식 -> 부모로 정보 전달.(emitting event <-> 부모 -> 자식 : props)

2. inputChange 이벤트와 사용자가 입력한 value 가 함께 상위 컴포넌트인 App.vue로 emit 된다.

```vue
<template>
    <div>
        <input @change="onInput" type="text"> <!-- input 될 때마다 함수를 실행시킨다.-->
    </div>
</template>

<script>
    export default {
        name: 'SearchBar',
        methods: {
            onInput(e) { // e: input값
                // 들어온 input을 부모로 올려줌 inputChange라는 이벤트와 함께 e.target.value 보내줌
                // 상위로 데이터 올려줌!
                this.$emit('inputChange', e.target.value) // this.$emit(eventname, args)
            }
        }
    }
</script>

<!-- scoped : SearchBar.vue에만 적용됨-->
<style scoped>
    input {
        width: 75%;
    }

    div {
        text-align: center;
        margin: 20px;
    }
</style>
```

### `App.vue`

3. SearchBar 에서 넘어온 이벤트 inputChange 로 인해 onInputChange함수가 실행된다.
4. onInputChange 함수는 유튜브 api 에 요청을 보내고 비디오 리스트를 응답 받는다.

```vue
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
```



-----

5. 넘겨 받은 비디오 리스트를 videos 라는 배열에 저장한다.

** Vue component 에서는 반드시 Object 를 return 하는 함수로 작성!!

6. `data` object가 (videos 배열이 있는 곳) 업데이트 되면, 해당 컴포넌트(App.vue 가 템플릿을 다시 렌더링한다.)
7. 그리고 바로 자식 컴포넌트들도 모두 다시 렌더링 된다.
8. `VideoList` 컴포넌트가 비디오 배열을 받아 화면에 보여주게 된다.

### `VideoList.vue`

```vue
<template>
    <ul class="col-lg-4 list-group"> <!-- 오른쪽 4 칸 차지-->
        <!-- v-bind로 props 데이터 보냄(video) -->
        <video-list-item v-for="video in videos" :key="video.etag" :video="video" @videoSelect="onVideoSelect"></video-list-item>
    </ul>
</template>

<script>
// App.vue가 아닌 VideoList.vue에 등록해야함!!
import VideoListItem from './VideoListItem'
    export default {
        name: 'VideoList',
        components: {
            VideoListItem,
        },
        methods: {
            onVideoSelect(video) {
                this.$emit('videoSelect', video) // VideoListItem에서 받은 video를 App.vue로 올림.
            }
        },
        // 데이터 받아옴
        props: {
            // App.vue에서 넘긴 값
            videos: {
                type: Array,
                required: true,
            },
        },
    }
</script>

<style>
</style>
```



### `VideoListItem.vue`

```vue
<template>
<!-- 클릭이 일어나면 onVideoSelect 실행됨-->
    <li @click="onVideoSelect" class="list-group-item">
        <!-- computed에 저장된 값 불러온다.. -->
        <img :src="thumbnailUrl" alt="image">
        <div class="media-body">
        {{ video.snippet.title }}
        </div>
    </li>
</template>

<script>
    export default {
        name: 'VideoListItem',
        // VideoList.vue에서 video 받아옴.
        props: {
            video: {
                type: Object, // 배열에서 하나만 가져옴.
                required: true,
            },
        },
        methods: {
            onVideoSelect() {
                this.$emit('videoSelect', this.video) // VideoList.vue로 video를 올려줌
            }
        },
        computed: {
            // 미리 캐싱 시켜놓음...
            thumbnailUrl() {
                return this.video.snippet.thumbnails.default.url
            }
        },
    }
</script>

<style scoped>
  li {
      display: flex;
      cursor: pointer;
  }
  li:hover {
      background-color: lightgray;
  }

</style>
```



### `VideoDetail.vue`

```vue
<template>
<div v-if="video" class="col-lg-8">
    <div class="embed-responsive embed-responsive-16by9">
        <iframe :src="videoUrl" frameborder="0" class="embed-responsive-item"></iframe>
    </div>
    <div class="details">
        <h4>{{ video.snippet.title }}</h4>
        <p>{{ video.snippet.description }}</p>
    </div>
</div>
</template>

<script>
    export default {
        name: 'VideoDetail',
        props: {
            video: {
                type: Object,
                // video 선택이 안될수도 있으므로..required 뻼
            }
        },
        computed: {
            videoUrl() {
                const videoId = this.video.id.videoId // videoId 가져오기
                return `http://www.youtube.com/embed/${videoId}`
            }
        }
    }
</script>

<style scoped>
 .details {
     margin-top: 10px;
     padding: 10px;
     border: 1px solid #ddd;
     border-radius: 4px;
 }
</style>
```


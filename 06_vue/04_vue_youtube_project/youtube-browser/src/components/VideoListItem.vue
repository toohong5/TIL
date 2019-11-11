<template>
<!-- 클릭이 일어나면 onVideoSelect 실행됨-->
    <li @click="onVideoSelect" class="list-group-item">
        <!-- computed에 저장된 값 불러온다.. -->
        <img :src="thumbnailUrl" alt="image">
        <div class="media-body" v-html="video.snippet.title">
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
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
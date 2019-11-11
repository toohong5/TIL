<template>
<div v-if="video" class="col-lg-8">
    <div class="embed-responsive embed-responsive-16by9">
        <iframe :src="videoUrl" frameborder="0" class="embed-responsive-item"></iframe>
    </div>
    <div class="details">
        <h4 v-html="video.snippet.title"></h4>
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
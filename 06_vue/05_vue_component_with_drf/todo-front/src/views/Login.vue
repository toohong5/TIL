<template> <!--보여지는 부분-->
  <div class="about">
    <!--2.-->
    <LoginForm/>
  </div>
</template>

<script>
  // 0.
  // @ 는 `/src` 의 alias
  // import LoginForm from '../components/LoginForm'
  import LoginForm from '@/components/LoginForm'  //절대경로 ( /src를 @ 로...)

  export default {
    // 1.
    name: 'login',
    components: {
      LoginForm,
    }
  }
</script>

<style>

</style>
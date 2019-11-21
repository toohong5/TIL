<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="alert alert-danger" role="alert">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <!-- idx를 키값으로 설정 -->
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>
      </div>


      <div class="form-group">
        <label for="id">ID</label>
        <input 
          type="text"
          class="form-control" 
          id="id" 
          placeholder="아이디를 입력하세요"
          v-model="credentials.username"
          >
      </div>
      <div class="form-group">
        <label for="password">password</label>
        <input 
          type="password" 
          class="form-control" 
          id="password" 
          placeholder="패스워드를 입력하세요"
          v-model="credentials.password"
          >
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
// npm i axios
  import axios from 'axios'
  // redirect 개념임
  import router from '../router'

  export default {
    name: 'LoginForm',
    data() { // 객체로 리턴해야 함
      return {
        credentials: {
          username: '',
          password: '',
        },
        // loading: false, // vuex로 변경
        errors: [],
      }
    },
    // getters
    computed: {
      loading: function() {
        return this.$store.state.loading // store 폴더의 state의 loading 값을 가져온다.
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          // this.loading = true
          this.$store.dispatch('startLoading') // actions 호출은 dispatch로
          // django jwt 를 생성하는 주소로 요청을 보냄
          // 이때 post 요청으로 보내야하며 사용자가 입력한 로그인 정보를 같이 넘겨야 함.
          axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials) // 여기로 데이터(credentials) 보냄
          .then(res => {
            // this.$session.start()
            // this.$session.set('jwt', res.data.token) // (key, value)
            this.$store.dispatch('endLoading') // 로딩 종료
            this.$store.dispatch('login', res.data.token) //토큰 가져오기
            // 성공시 메인페이지로 이동 (index.js의 path로 이동)
            router.push('/')
          })
          // .then 에서 error 발생시 동작함
          .catch(err => {
            // 로그인 실패시 loading 의 상태를 다시 false 로 변경
            // this.loading = false
            this.$store.dispatch('endLoading') // 로딩 종료
            console.log(err)
          })
        } else {
          console.log('로그인 검증 실패')
        }
      },
      checkForm() {
        this.errors = []
        if (!this.credentials.username) {
          this.errors.push("아이디를 입력해주세요.")
        }
        //password 8자 이하인 경우 에러
        if (this.credentials.password.length < 8) {
          this.errors.push("비밀번호는 8자 이상 입력해주세요.")
        }
        // 에러 없으면 true 반환
        if (this.errors.length === 0) {
          return true
        }
      }
    },
  }
</script>

<style>

</style>
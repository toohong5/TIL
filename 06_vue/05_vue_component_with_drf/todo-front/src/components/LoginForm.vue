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

  export default {
    name: 'LoginForm',
    data() { // 객체로 리턴해야 함
      return {
        credentials: {
          username: '',
          password: '',
        },
        loading: false,
        errors: [],
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          this.loading = true
          axios.get('http://127.0.0.1:8000', this.credentials) // 여기로 데이터(credentials) 보냄
          .then(res => {
            console.log(res)
          })
          // .then 에서 error 발생시 동작함
          .catch(err => {
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
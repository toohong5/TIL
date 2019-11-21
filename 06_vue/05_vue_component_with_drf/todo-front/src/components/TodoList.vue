<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body">
        <span @click="updateTodo(todo)" :class="{ complete: todo.completed }">{{ todo.title }}</span> <!--todo.completed에 따라서 취소선 여부 결정-->
        <span @click="deleteTodo(todo)">🗑️</span> <!--삭제버튼 (todo)는 인자.-->
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'TodoList',
    props: {
      todos: {
        type: Array,
        required: true,
      },
    },
    computed: {
      requestHeader: function() {
        return this.$store.getters.requestHeader
      }
    },
    methods: {
      // 장고에 보내서 삭제기능 하도록 함.
      // for 문에서 todo 쓸 수 있으므로...
      deleteTodo(todo) {
        // this.$session.start()
        // const token = this.$session.get('jwt')
        // const requestHeader = {
        //   headers: {
        //     Authorization: 'JWT ' + token
        //   }
        // }
        axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, this.requestHeader) // requestHeader 데이터도 함께 장고로 보냄! (computed의 requestHeader 가져옴)
          .then(res => { // 정상적으로 온다면...
            console.log(res)
            const targetTodo = this.todos.find(function(el) {
              return el === todo
            })
            const idx = this.todos.indexOf(targetTodo) // targetTodo의 인덱스값 가져옴.
            if (idx > -1) {
              this.todos.splice(idx, 1) // idx 부터 1개 삭제
            }
          })
          .catch(err => {
            console.log(err)
          })
      },
      updateTodo(todo) {
        // this.$session.start()
        // const token = this.$session.get('jwt')
        // const requestHeader = {
        //   headers: {
        //     Authorization: 'JWT ' + token
        //   }
        // }
        const requestForm = new FormData ()
        requestForm.append('id', todo.id)
        requestForm.append('title', todo.title)
        requestForm.append('user', todo.user)
        requestForm.append('completed', !todo.completed) // 반대로 반영시켜줌?

        axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestForm, this.requestHeader) // put으로 보낸다. ( computed 의 requestHeader 가져옴)
          .then(res => {
            console.log(res)
            todo.completed = !todo.completed // vue의 화면에 반응 알려줌.
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
  }
</script>

<style>
  .complete {
    text-decoration: line-through;
    color: rgb(112, 112, 112)
  }
</style>
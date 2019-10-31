const axios = require('axios')

axios.get('http://jsonplaceholder.typicode.com/posts1111')
  .then( response => {
      console.log(response)
  })
  .catch( err => {
      console.log(err)
  }) // 주소가 잘못된 경우 에러 띄워줌
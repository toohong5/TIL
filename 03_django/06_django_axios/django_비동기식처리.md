XMLHttpRequest(XHR) : 비동기를 위한 새로운 api

- 브라우저는 XMLHttpRequest 객체를 이용하여 Ajax 요청을 생성하고 전송
- 서버가 브라우저의 요청에 대해 응답을 반환하면 같은 XHR 객체가 그 결과를 처리
- 단 IE 5,6 에서는 ActiveXobject 를 사용해야 한다.



https://github.com/axios/axios

기존 redirect로 인해 index.html 로 페이지가 로딩되는 것이 아닌 JSON 형태로 응답결과를 반환 받기로 변경

JSON 데이터에 liked 변수를 만들어서 template에서 좋아요를 취소할지 추가할지를 판단할 수 있도록 한다.

그래서 True False 값을 통해 좋아요 버튼의 style 값을 변경한다.(색 변경)


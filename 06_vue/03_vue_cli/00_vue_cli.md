```bash
$ npm install -g @vue/cli
```

https://cli.vuejs.org/guide/installation.html

## vue cli로 웹팩 만들기

```bash
$ vue create todo-vue-cli
$ cd todo-vue-cli
$ npm run serve
```

---------

웹팩을 직접 작성했을 때 만들었던 `webpack.config.js` 가 보이지 않는다.

-> `vue.config.js` 는 vue-cli에 의해 자동으로 로드되는 선택적 구성 파일로 변경 되었다.

-> vue-cli 3 버전부터 노출되지 않으며, 설정을 추가하기 위해서는 루트 디렉토리에 직접 파일을 만들고 작성해야 한다.

"@vue/cli-service"에서 로드됨.

```bash
$ vue ui 
```


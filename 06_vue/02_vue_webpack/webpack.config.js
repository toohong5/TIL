// webpack 설정 파일
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')
module.exports = {
    mode: 'development',
    entry: {
        // __dirname : 최상위 위치(entry point) -> Django 에서의 BASE_DIR
        app: path.join(__dirname, 'src', 'main.js')
    },
    module: {
        rules: [
            {
                test: /\.vue$/, // 정규표현식 : `.vue`로 끝나는 애들을 use를 통해 사용하겠다는 뜻// \.으로 `.` 인식 `$/`로 경로 끝냄
                use: 'vue-loader',
            },
            {
                test:/\.css$/,
                use: ['vue-style-loader', 'css-loader'] // 여러개 일때는 배열로 작성
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin(),
    ], // plugins는 배열로
    output: {
        filename: 'app.js',
        path: path.join(__dirname, 'dist'),
    },
}
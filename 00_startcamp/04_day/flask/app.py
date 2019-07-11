from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
   # return 'Hello World!'
   return render_template('index.html')


@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY!'


@app.route('/dday')
def dday():
    #오늘날짜
    today_time = datetime.now()
    #수료날짜
    endgame = datetime(2019, 11, 29)
    #dday = 수료날짜 - 오늘 날짜
    dday = endgame-today_time
    return f'{dday.days} 일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>' # h1으로 보냄


@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내 봅시다</h1>
    <ul>
        <li>1번</li>
        <li>2번</li> 
    </ul>
    """

#변수 라우팅(variable routing)
@app.route('/greeting/<name>') # <(string: 기본값으로 생략가능, 다른 형(int, float)에서는 사용해야함)변수명>
def greeting(name):
    #return f'반갑습니다! {name}'
    return render_template('greeting.html', html_name=name)


@app.route('/cube/<int:number>')
def cube(number):
    #연산을 모두 끝내고 변수만 cube.html로 넘긴다.
    result = number**3
    #return f'{number}의 세제곱은 {number**3}입니다.'
    return render_template('cube.html', result=result, number=number) #html 변수로 저장


@app.route('/lunch/<int:number>')
def lunch(number):
    menu=['스시', '삼겹살', '치킨', '닭갈비', '카레', '햄버거']
    return f'{random.sample(menu,number)}'


# render template
@app.route('/movie')
def movie():
    movies = ['토이스토리4', '알라딘', '기생충', '스파이더맨', '엔드게임']
    return render_template('movie.html', movies=movies)


#FLASK REQUEST & RESPONSE

@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    print(request.args)
    name = request.args.get('data') #text값이 들어있음
    return render_template('pong.html',name=name)

#fake naver, fake google 만들기

#https://search.naver.com/search.naver?query=
@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

#view 함수 2개 templates 2개(이름받는 곳/ 결과 출력하는 곳)
@app.route('/name')
def name():
    return render_template('name.html')


@app.route('/result')
def result():
    personalities=['인성', '상냥함', '체력', '돈복', '인싸력', '악마력']
    y_name = request.args.get('name') #text값이 들어있음
    result = random.sample(personalities,3)
    return render_template('result.html',result=result, y_name=y_name)

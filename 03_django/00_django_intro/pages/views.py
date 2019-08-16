# django imports style guide
# 1. standard library
# 2. third-party
# 3. Django
# 4. local django

import random
from datetime import datetime
from pprint import pprint
import requests
from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'pages/index.html') # render()의 첫번째 인자도 반드시 request

def introduce(request, name, age):
    context = {'name': name, 'age': age}
    return render(request, 'pages/introduce.html', context)

def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context) # context에 딕셔너리 들어감! {'template에서 가져올 이름': pick에서 뽑은거}

def image(request):
    return render(request, 'pages/image.html')

# variable routing
# 동적라우팅 (주소자체를 변수로만든다)
# 키값을 템플릿에 가져가서 value를 사용함.
def hello(request, name):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,}
    return render(request, 'pages/hello.html', context)

def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'pages/introduce.html', context)

def times(request, num1, num2):
    mul = num1 * num2
    context = {'mul': mul, 'num1': num1, 'num2': num2,}
    return render(request, 'pages/times.html', context)

def area(request, radius):
    area = 3.14 * radius * radius
    context = {'radius': radius, 'area': area,}
    return render(request, 'pages/area.html', context)

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'pages/template_language.html', context)

def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result}
    return render(request, 'pages/isitgwangbok.html', context)


# GET 방식(주로 검색어...)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    # pprint(request)
    # scheme : http나 https의 속성을 알려줌
    # pprint(request.scheme)
    # pprint(request.path)
    # method 방식을 알려줌
    # pprint(request.method)
    # <QueryDict: {'message': ['ㅇㄹㅇㄹ']}> : 데이터가 딕셔너리 형태로 넘어옴.
    # pprint(request.GET)
    # 서버에 대한 정보 알려줌
    pprint(request.META)
    # request.GET.get(key) : request안에서 GET방식으로 딕셔너리 키값에 접근 .get('key값') 키값 중 하나 뽑아서 message라는 변수에 저장 후 context로 넘김
    message = request.GET.get('message')
    context = {'message': message,}
    return render(request, 'pages/catch.html', context)

#  요청보내는 함수 -> result로 보냄
def art(request):
    return render(request, 'pages/art.html')

# 요청받는 함수
def result(request):
    # 1. art에서 form 으로 보낸 데이너틑 받는다.
    word = request.GET.get('word') 
    
    # 2. ARTII API의 폰트 리스트로 요청을 보내 응답을 text로 받는다.
    # pip install requests 하고 import requests해주어야 함
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    # 3. 문자열을 리스트로 바꾸기 -> 나중에 랜덤으로 돌려서 주소에 넣기 위함.
    fonts = fonts.split('\n')

    # 4. fonts list 안에 들어있는 요소 중 하나를 선택해서 변수에 저장
    font = random.choice(fonts)

    # 5. 위에서 만든 word와 font 를 가지고 다시 요청을 만들어서 보내 응답결과를 받는다.
    # .text 로 받아야 객체가 아닌 값이 나온다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'response': response,}
    return render(request, 'pages/result.html', context)

# POST 방식으로 보내기 -> DATA의 수정, 삭제 가능 (ID, PASSWORD등은 숨겨서 보내야함)
# page만 render 해줌
def user_new(request):
    return render(request, 'pages/user_new.html')

# id, pwd 가 넘어옴
def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd,}
    return render(request, 'pages/user_create.html', context)


# 정적파일(static file)
def static_example(request):
    return render(request, 'pages/static_example.html')
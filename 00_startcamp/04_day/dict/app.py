# 로또

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    # 회차번호 받아옴
    num = request.args.get('num')
    #동행복권에 요청보내 응답 받음
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}') #회차정보 받아서 요청보냄
    # json 형태로 바꿔준다(우리가 크롬에서 보고있는 결과와 동일한 모습으로 바뀜)
    lotto = res.json()

    # 당첨번호 6개 가져오기
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}']) #당첨번호라 winner 리스트에 저장됨!

    # 내 번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num)) #list => int로 형변환!
    # 등수 가리기(몇 개 맞았는지 교집합이 필요!)
    matched = 0
    # 내 번호 요소를 뽑아서 당첨번호 리스트에 있는지 확인.
    for num in numbers:
        if num in winner:
            matched += 1
    if matched == 6:
        result = '1등 입니다!'
    elif matched == 5:
        if lotto['bnusNo'] in numbers:
            result = '2등 입니다!'
        else:
            result = '3등 입니다!'
    elif matched == 4:
        result = "4등 입니다!"
    elif matched == 3:
        result = "5등 입니다!"
    else:
        result = "꽝입니다."

    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)



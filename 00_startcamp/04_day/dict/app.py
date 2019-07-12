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
        numbers.append(int(num)) #문자열 => int로 형변환!
    # 등수 가리기(몇 개 맞았는지 교집합이 필요!)
    matched = 0
    # 내 번호 리스트를 돌면서 뽑은 번호 하나하나가 winner 당첨번호 리스트에 있는지 확인.
    for num in numbers:
        if num in winner:
            matched += 1


    # set을 이용한 코드!_위의 코드와 같음.
    matched = len(set(winner) & set(numbers))

    if len(numbers) == 6:
        if matched == 6:
            result = '1등 입니다!'
        elif matched == 5:
            # 보너스 번호가 내 로또번호 리스트에 존재하면, 
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
    else:
        result = '번호의 수가 6개가 아닙니다.'

    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)



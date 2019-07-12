from flask import Flask, render_template, request
import requests
from decouple import config

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')


@app.route('/')
def hello():
    return 'Hi there!'


@app.route(f'/{token}', methods=['POST'])
def telegram():
    # step 1. 데이터 구조 print 해보기
    from_telegram = request.get_json()

    if from_telegram.get('message') is not None:
        # step 2. 그대로 돌려보내기
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        # 한글 키워드 받기
        
        # /번역 으로 입력이 시작된다면, 파파고로 번역이 동작한다.
        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data={'source': 'ko', 'target': 'en', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') #여기에 한영 번역 텍스트가 있다.


        # /번역 으로 입력이 시작된다면, 파파고로 번역이 동작한다.
        if text[0:5] == '/번역2 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data={'source': 'ko', 'target': 'es', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') #여기에 한스 번역 텍스트가 있다.


        #로또
        if text[0:4] == '/로또 ':
            # 회차번호 받아옴
            num = text[4:]
            #동행복권에 요청보내 응답 받음
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}') #회차정보 받아서 요청보냄
            # json 형태로 바꿔준다(우리가 크롬에서 보고있는 결과와 동일한 모습으로 바뀜)
            lotto = res.json()

            # 당첨번호 6개 가져오기
            winner = []
            for i in range(1,7):
                winner.append(lotto[f'drwtNo{i}']) #당첨번호라 winner 리스트에 저장됨!
            bonus_num = lotto['bnusNo']
            text = f'로또 {num} 회차의 당첨 번호는 {winner} 입니다. 보너스 번호는 {bonus_num}' 

        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


    return '', 200
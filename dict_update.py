# .update() 사용법
a = {}

# 1
a.update(key='value')

# 2
a.update({row['영화대표코드': row['영화명(국문)']})

# .env 에 환경변수 세팅!(python- decouple)
NAVER_CLIENT_ID='T6QeWmD9Pir7AX9wpU7q'
NAVER_CLIENT_SECRET='DyN6O8CIsi'

# 네이버 요청하는법
# 1-1 기본설정
import requests
from decouple import config

CLIENT_ID = config(NAVER_CLIENT_ID)
NAVER_CLIENT_SECRET = config(NAVER_CLIENT_SECRET)
HEADERS = {'X-NAVER-Client-Id' : CLIENT_ID, 'X-NAVER-Client-Secret' : CLIENT_SECRET}

# 1-2 요청 보내기

url = 'https://openapi.naver.com/v1/search/blog.json'
address = f'{url}?query={movieNm}'
response = requests.get(address, headers=HEADERS).json()


# ------------------------------------------------------------

# 3 이미지 파일 저장하기
# 3-1 movie_naver.csv 여기서 영화코드랑 썸네일 url
# 3-2 요청보내서 응답을 작성하기

url = ''
# images 폴더 만들어 영화코드로 저장!
with open(f'images/{img}.jpg', 'wb') as f:
    response = requests.get(url).content
    f.write(image)
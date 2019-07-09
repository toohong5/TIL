#순위 리스트 출력하기

import requests
from bs4 import BeautifulSoup


url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser') #정제(타입변경 : )


#하나의 순위의 경로 가져와서 li(list) 뒤에 지우기(바뀌는거 찾기!), select 는 여러개 선택한다
s=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

#리스트로 출력!
for i in s:
    print(i.text) #키워드만 출력

# 두번째 커밋을 위한 주석!!!
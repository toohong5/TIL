import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/marketindex/').text #정보가져옴

soup = BeautifulSoup(html, 'html.parser') #정제(타입변경 : )
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text #필요한 정보만 출력
exchange_jpy = soup.select_one('#exchangeList > li > a.head.jpy > div > span.value').text
print(exchange)
print(exchange_jpy)
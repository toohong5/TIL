'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')

# 아래에 코드를 작성해 주세요.
list_prices=prices.split(';')

for i in list_prices:
    i=int[i]

list_prices.sort(reverse=True)

for i in list_prices:
    print(int(i))

"""
문자열 <=> 리스트 형변환이 포인트!!

makes = prices.split(';') # split(): 공백기준으로 나눔

숫자형 형변환 필요!

boxes = [] #빈 리스트 만들기
for make in makes:
   boxes.append(int(make)) #list.append() : list에 요소를 추가함.

boxes.sort(reverse=True) #내림차순 정렬

for boc in boxes:
    print(box)

"""

'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.

if number % 2 == 0:  # True(1,2,...), False(0)
    print("짝수입니다.")
else:
    print("홀수입니다.")

"""
if number % 2: #값이 있으면 true로 홀수 값이 없으면 false로 짝수 # True(1,2,...), False(0)
    print("홀수입니다.")
else:
    print("짝수입니다.")
"""
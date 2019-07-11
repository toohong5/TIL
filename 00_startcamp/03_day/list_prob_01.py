'''
# 문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

str = input('문자를 입력하세요: ')

# 아래에 코드를 작성해 주세요.
str = list(str)
first=str[0]
last=str[len(str)-1]

print(f'첫번째 문자: {first}\n두번째 문자: {last}')


"""
선생님 풀이

print(f'첫글자는 {str[0]}, 마지막글자 {str[-1]})

"""

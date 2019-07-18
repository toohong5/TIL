```python
# 04_homework.md
#1
Local scope -> Enclosed scope -> Global scope -> Built-in scope

#2
1번
# 2개를 리턴하는 것 처럼 보이지만 실제로는 튜플 1개가 리턴되는 것이다. 이는 하나의 튜플 객체입니다.

#3
반복문을 사용했을 때 보다 느리다는 단점이 있지만 알고리즘 자체가 재귀적인 표현이 자연스러운 경우가 많다.
# 장점: 직관적이고 이해하기 쉬운 경우가 많음(알고리즘의 경우)
# 단점: 작성하기 어려움. 메모리 스택이 넘치거나 프로그램이 느려지는 문제.


# 04_workshop.md
def func_sqrt(x):
    a = x
    b = x-1
    while a - b > 0.001: 
        if ((b+a)/2)**2 > x:
            a=((b+a)/2)
        else:
            b=((b+a)/2)
    return b


print(func_sqrt(2))

# 선생님 풀이 -----------------------------------------------------------------------------
# 양의 정수 n을 입력받아 제곱근의 근사값(제곱했을 때 n이 되는 수)을 반환하는 함수를 작성.
import math


def my_sqrt(n):
    x, y = 1, n # 범위 점차 좁혀나감.
    result = 1
    # 제곱근의 제곱(result**2) 과 입력 값(n) 의 차이가 적어도 이 정도 차이보다 작아지면!
    while abs(result**2 - n) > 1e-10: # 0.0000000001
   # math.isclose()사용
	# while not math.isclose(result**2, n):
        result = (x+y)/2 # 양쪽 끝 값을 더해서 2로 나눈다.(절반을 구한다.)
        # 위 근사치에 따라 x 또는 y의 값을 바꾼다.
        if result**2 <n:
            x = result
        else:
            y = result
    return result
print(my_sqrt(2))

    
    #!!!!!!!!!!
    

```


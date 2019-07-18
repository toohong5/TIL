```python
# 01_homework.md

# 1. Python에서 사용할 수 없는 식별자 예약어 를 찾아 작성하세요
import keyword
print(keyword.kwlist)
=>
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

# 2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (floating point rounding error) 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.
a = 0.1 * 3 b = 0.3
=>
import math
math.isclose(a,b)

# 3. 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \ 을 작성하세요.

	1) '\n'
	2) \t
	3) \\
# 4. 
print(f"
안녕, {name}야
")

# 5. 
5번

      
# 01_workshop.md

# 1. 
print((("*" * n) + '\n') * m)

# 2.
print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')

# 3. 근의 공식 작성하기
a = 1
b = 4
c = -21
print((-b + (b**2-4*a*c)**(1/2))/ 2*a)
print((-b - (b**2-4*a*c)**(1/2))/ 2*a)

```

```py

```
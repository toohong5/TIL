# DOCstring ("""....""") : 설명 쓸 수 있음

"""
다음과 같은 내용의 파일 quest.txt 가 있다.
0
1
2
3

이 파일의 내용을 다음과 같이 역순으로 reverse_quest.txt 라는 파일로 저장하시오.
3
2
1
0

"""

# 1. 읽기
with open('quest.txt', 'r') as f:
    all_text = f.read()

# 2. 뒤집고

# all_text.reverse()

# 3. 작성하고
with open('reverse_quest.txt', 'w') as f:
    # for i in all_text:
    #     reversed_txt = ""
    #     reversed_txt = reversed(i)
    # for i in reversed_txt:
    #     print(i)
 
     f.writelines(f'{all_text[::-1].strip()}\n')
    #f.write(all_text)
        
"""
선생님 풀이
# 1. 읽기
with open('quest.txt', 'r') as f:
    all_text = f.read()

# 2. 뒤집기
how to reverse list in python 으로 검색!
stack overflow들어가서 확인

변수.reverse() 채택

all_text.reverse()

# 3. 작성하기
i) 
with open('reverse_quest.txt', 'w') as f:
    for a in all_text:
        f.write(a)

ii)
with open('reverse_quest.txt', 'w') as f:
    f.writelines(all_text)

"""
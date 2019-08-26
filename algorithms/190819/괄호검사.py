import sys
sys.stdin = open('sample_input2.txt', 'r')

n = int(input())
for i in range(1, n + 1):
    words = input()
    S = []

    result = 0
    for ch in words:
        if ch == '(' or ch == '{':
            S.append(ch) 
        # }, )일 경우만 체크함.       
        elif ch == '}' or ch == ')':
            # 잘못된 경우들
            if len(S) == 0:
                result = 0
                break
            if ch==')' and  S.pop() != '(':
                result = 0
                break
            if ch=='}' and S.pop() != '{':
                result = 0
                break
    else:
        if len(S)==0:
            result = 1
        else:
            result = 0
    
    print('#{} {}'.format(i, result))
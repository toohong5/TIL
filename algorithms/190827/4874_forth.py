import sys
sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    forth = input().split()
    operator = '+-*/'
    S = []
    
    num1 = 0
    num2 = 0
    cal = 0
    flag = 0
    for i in forth:
        if i.isdecimal():
            S.append(int(i))
        elif i in operator:
            try:
                # pop은 뒤에서 부터 뽑아와서 연산한다...처음 뽑은 값이 연산할때 뒤로 가야함!!
                num2 = S.pop()
                num1 = S.pop()
                if i == '+':
                    cal = num1 + num2
                    S.append(cal)
                    cal = 0
                elif i == '-':
                    cal = num1 - num2
                    S.append(cal)
                    cal = 0
                elif i == '*':
                    cal = num1 * num2
                    S.append(cal)
                    cal = 0
                elif i == '/':
                    cal = num1 // num2
                    S.append(cal)
                    cal = 0
            except:
                flag = 1
        if i == '.':
            # len(S) 에 1개 이상의 값이 있으면 에러임!!
            if len(S) > 1 or flag == 1:
                print('#{} error'.format(tc))
            else:
                print('#{} {}'.format(tc, S[-1]))

        
            

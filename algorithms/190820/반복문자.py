import sys
sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    words = input()
    S = []

    for i in words:
        if i not in S:
            S.append(i)
        else:
            if len(S) == 0:
                break
            if i == S[-1]:
                S.pop()
            else:
                S.append(i)
    print('#{} {}'.format(tc, len(S)))

import sys
sys.stdin = open('sample_input3.txt', 'r')

n = int(input())
for tc in range(1, n + 1):
    words = input()
    S = []

    for ch in words:
        if ch not in S:
            S.append(ch)
        elif ch in S: 
            if len(S) == 0:
                break
            if ch == S[-1]:
                S.pop()
            else:
                S.append(ch)

    print('#{} {}'.format(tc, len(S)))

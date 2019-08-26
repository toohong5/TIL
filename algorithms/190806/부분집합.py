import sys
sys.stdin = open('input2_2.txt', 'r')

T = int(input())

A = [i for i in range(1, 13)]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    result = []
    for i in range(1 << len(A)):
        a = []
        for j in range(len(A)):
            if i & (1 << j):
                a.append(A[j])
        if len(a) == N:
            result.append(a)

    r = 0
    for k in result:
        if sum(k) == K:
            r += 1
        
    print('#{} {}'.format(tc, r))

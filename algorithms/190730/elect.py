import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    count = 0
    k = K
    i = 0
    charge = 1
    while i < N + 1:
        i += 1
        k -= 1
        if i == N:
            break
        if k == 0:
            if i in stops:
                k = K
                count += 1
                charge = i
            else:
                for j in range(i, charge, -1):
                    if j in stops:
                        k = K
                        count += 1
                        charge = j
                        i = j
                        break
                else:
                    count = 0
                    break
    print('#{} {}'.format(tc, count))
                    


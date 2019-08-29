import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_stops = list(map(int, input().split()))

    k = K
    count = 0
    charge = 1
    i = 0
    while i < N + 1:
        i += 1
    # for i in range(1, N + 1):
        k -= 1
        if i == N:
            break
        if k == 0:
            if i in charge_stops: # 충전소 있다면 충전함
                k = K
                count += 1
                charge = i
            else:
                for j in range(i, charge, -1):
                    if j in charge_stops:
                        k = K
                        count += 1
                        charge =j
                        i = j
                        break
                else:
                    count = 0
                    break
        
    print('#{} {}'.format(tc, count))
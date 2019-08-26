import sys
sys.stdin = open('input2.txt', 'r')

n = int(input())
for tc in range(1, n+1):
    K, N, M = map(int, input().split())
    m = list(map(int, input().split()))
    num_charge = 0
    charge = [0 for i in range(N+1)]

    num_charge = 0
    for i in range(len(charge)):
        if i in m:
            charge[i] = 1
    print(charge)
    # 충전소 수 부족시 0 출력
    for k in range(len(m)-1):
        if m[k+1] - m[k] > K:
            print('#{} 0'.format(tc))
        continue

    j = 1
    while j < len(charge):
        K -= 1
        if K==0 and charge[j]==1:
            K = K
            num_charge += 1
        elif K==0 and charge[j]==0 and charge[j-1]==1:
            K = K
            num_charge += 1
        j += 1
    print(num_charge)
        

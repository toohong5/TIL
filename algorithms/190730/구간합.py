import sys
sys.stdin = open('input4.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))

    sum_list = []
    for i in range(N - M + 1):
        sum = 0
        for j in range(i, i + M):
            sum += arr[j]
        sum_list.append(sum)
    
    print('#{} {}'.format(tc, max(sum_list) - min(sum_list)))
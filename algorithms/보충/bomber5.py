import sys
sys.stdin = open('bomber5_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum = 0
    for _ in range(M):
        x, y = map(int, input().split())
        for i in range(N):
            sum += arr[x][i]
            arr[x][i] = 0
            sum += arr[i][y]
            arr[i][y] = 0
    print('#{} {}'.format(tc, sum))
        

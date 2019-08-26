import sys
sys.stdin = open('bomber4_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
    for _ in range(M):
        x, y, m = map(int, input().split())
        for i in range(x, x + m):
            for j in range(y, y + m):
                if i > N - 1 or j > N - 1:
                    pass
                else:
                    sum += arr[i][j]
                    arr[i][j]=0
    print('#{} {}'.format(tc, sum))
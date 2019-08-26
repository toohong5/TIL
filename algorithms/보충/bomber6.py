import sys
sys.stdin = open('bomber6_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    sum = 0
    for _ in range(M):
        x, y, r = map(int, input().split())
        for i in range(x - r, x + r + 1): # 행범위(-1, 3)
            if i < 0 or i > N - 1:
                pass
            else:
                sum += arr[i][y]
                arr[i][y] = 0

        for j in range(y - r, y + r + 1): # 열범위(-1, 3)
            if j < 0 or j > N - 1:
                pass
            else:
                sum += arr[x][j]
                arr[x][j] = 0
        
    print('#{} {}'.format(tc, sum))
import sys
sys.stdin = open('bomber6_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    S = 0
    for _ in range(M):
        x, y, w = map(int, input().split())
        for r in range(x - w, x + w + 1): # 행범위
            if 0<= r < N:
                S += arr[r][y]
                arr[r][y] = 0
        for c in range(y - w, y + w + 1): # 열범위
            if 0 <= c < N:
                S += arr[x][c]
                arr[x][c] = 0

    print(S)
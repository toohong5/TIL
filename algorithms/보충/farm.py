import sys
sys.stdin = open('farm_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    sum = 0
    for r in range(0, N//2 + 1):
        for c in range(N//2 - r, N//2 + r + 1):
            sum += arr[r][c]
    
    for x in range(N - 1, N//2, -1):
        for y in range(N//2 - (N - x - 1), N//2 + (N - x - 1) + 1):
            sum += arr[x][y]

    print('#{} {}'.format(tc, sum))
import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
            # x = 행, y = 열
    dx = [-1, -1, 1, 1] # 좌상단, 우상단, 좌하단, 우하단
    dy = [-1, 1, -1, 1]
    ans = x = y = 0
    for r in range(N):
        for c in range(N):
            # 네 방향에 대해서 자료를 읽는다.
            S = 0
            for i in range(4):
                x, y = r + dx[i], c + dy[i]
                while x >= 0 and x < N and y >= 0 and y < N:
                    S += arr[x][y]
                    x, y = x + dx[i], y + dy[i]
            S += arr[r][c]

            # 따로 나눠서 하는법....
            S = 0
            # 좌상단
            x, y = r - 1, c - 1
            while x >= 0 and x < N and y >= 0 and y < N:
                S += arr[x][y]
                x, y = x - 1, y - 1
            # 우상단
            x, y = r - 1, c + 1
            while x >= 0 and x < N and y >= 0 and y < N:
                S += arr[x][y]
                x, y = x - 1, y + 1
            # 좌하단
            x, y = r + 1, c - 1
            while x >= 0 and x < N and y >= 0 and y < N:
                S += arr[x][y]
                x, y = x + 1, y - 1
            # 우하단
            x, y = r + 1, c + 1
            while x >= 0 and x < N and y >= 0 and y < N:
                S += arr[x][y]
                x, y = x + 1, y + 1




    # diag_sum = 0
    # diag_sum2 = 0
    # diag_list = []

    # for i in range(n):
    #     diag_sum += arr[i][i] 
    #     diag_sum2 += arr[i][n - i - 1]
    
    # print(diag_sum, diag_sum2)
    # while x:
    #     for i in range(n):
    #         for j in range(n):
    #             diag_sum = arr[i - 1][j + 1]
            
    

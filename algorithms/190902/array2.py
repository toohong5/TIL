import sys
from collections import deque

def BFS(x, y):
    visit = [[0] * N for _ in range(N)]
    visit[x][y] = 1
    q = deque()
    q.append((x, y))
    # size_row = 0
    # size_column = 0
    dx = [0, 1] # 우, 하
    dy = [1, 0]

    while q:
        (x1, y1) = q.popleft()
        for i in range(2):
            x2 = x1 + dx[i]
            if 0 <= x2 < N:
                if not visit[x2][y]:
                    if arr[x2][y] != 0:
                        q.append((x2, y))

        for i in range(2):
            y2 = y1 + dy[i]
            if 0 <= y2 < N:
                if not visit[x][y1]:
                    if arr[x][y1] != 0:
                        q.append((x, y2))
    print(x1, y1)


    #     for i in range(1, N):
    #         if not visit[x1][i]:
    #             x1 += 1
    #             if arr[x1][i] != 0:
    #                 q.append((x1, i))
    #                 size_row += 1
    #             if arr[x1][i] == 0:
    #                 size_row = i

    #         for j in range(N):
    #             if not visit[x1][y1]:
    #                 if arr[i][j] != 0:
    #                     q.append((x1, y1))
    #                 if arr[i][j] == 0:
    #                     return (x1, y1)
    # return (size_row, size_column)

sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    size_row = 0
    size_column = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                x = i
                y = j
                break
        break

    print(BFS(x, y))

# def sol_maze(maze, x1, y1, x2, y2):
#         visit[x1][y1] = True
#         global result
#         if x1 == x2 and y1 == y2:
#             result = 1
#             return result
#         else:
#             for i in range(4):
#                 # 갔던 길은 돌아가지 않게하기....
#                 if x1 + dx[i] >= 0 and x1 + dx[i] < N and y1 + dy[i] >= 0 and y1 + dy[i] < N:
#                     if maze[x1 + dx[i]][y1 + dy[i]] == 0 and visit[x1 + dx[i]][y1 + dy[i]] == False:
#                         x1 = x1 + dx[i]
#                         y1 = y1 + dy[i]
#                         x.append(x1)
#                         y.append(y1)
#                         visit[x1][y1] = True
#                         sol_maze(maze, x1, y1, x2, y2)
#                     elif maze[x1 + dx[i]][y1 + dy[i]] == 3:
#                         x1 = x1 + dx[i]
#                         y1 = y1 + dy[i]
#                         sol_maze(maze, x1, y1, x2, y2)
#             else:
#                 sol_maze(maze, x[0], y[0], x2, y2)

def DFS(x1, y1):
    visit[x1][y1] = True
    global result
    if maze[x1][y1] == 3:
        result = 1
    else:
        for i in range(4):
            x = x1 + dx[i]
            y = y1 + dy[i]
            if 0 <= x < N and 0 <= y < N:
                if not visit[x][y] and maze[x][y] == 0 or maze[x][y] == 3:
                    DFS(x, y)

# ---------------------------------------------------------------------------------                
import sys
sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
  
    dx = [-1, 1, 0, 0] # 상 하 좌 우
    dy = [0, 0, -1, 1]
    x1 = y1 = 0 # 2의 좌표

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                x1 = r
                y1 = c
    
    visit = [[False] * N for _ in range(N)]

    result = 0
    DFS(x1, y1)
    print('#{} {}'.format(tc, result))
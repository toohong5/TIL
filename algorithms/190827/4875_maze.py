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


    #---------------------------
    # 1. 출발지 찾기
    # 2. 상하좌우 갈 수 있는 길 찾기
    # 3. 지나간 길을 1로 변경
    # 4. 잘 못 들어온 미로로 들어가면 0을 반환
    # 5. 남은 스택에서 하나씩 꺼내면서 처음 출발점으로 돌아가서 남은 길 탐색
    # 6. 재탐색
    # 7. 도착점 확인 시 1 반환

    def find():
        dRow = [0, 1, 0, -1]
        dCol = [1, 0, -1, 0]
        s = []
        s.append([s.Row, sCol])     # 입구로 이동
        maze[sRow][sCol] = 1        # 방문 표시
        while(len(s) != 0):         # 스택이 0이 아니면 움질일 수 있는 곳이 있다는 의미. 0이면 더이상 갈 곳이 없음.
            n = s.pop()             # 다음 이동위치 pop으로 꺼냄
            for i in range(4):      # 갈 수 있는 좌표들
                nRow = n[0] + dRow[i]   # 주변좌표 계산(n[0]: 행, n[1]: 열)
                nCol = n[1] + dCol[i]
                if nRow>=0 and nRow<N and nCol>=0 and nCol<N: # 범위체크
                    if maze[nRow][nCol] == 3: # 출구인 경우
                        return 1
                    elif maze[nRow][nCol] == 0: # 갈 수 있는 경우
                        s.append([nRow, nCol])
                        maze[n[0]][n[1]] = 1
        return 0                                # 출구에 가지 못하고 막힘

    for tc in range(1, T + 1):
        N = int(input())

        maze = [[int(x) for x in input()] for i in range(N)]
        for i in range(N):
            if 2 in maze[i]:

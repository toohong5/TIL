import sys
sys.stdin = open('sample_input2.txt', 'r')

def DFS(x, y, count, S):
    dx = [-1, 1, 0, 0] # 상 하 좌 우
    dy = [0, 0, -1, 1]
    visit[x][y] = 1
    global result
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < N and 0 <= y1 < N:
            if arr[x1][y1] == 0:
                if not visit[x1][y1]:
                    S.append(arr[x1][y1])
                    # print(S)
                    return DFS(x1, y1, count+1, S)
            elif arr[x1][y1] == 3:
                # print('#{} {}'.format(tc, count))
                return count

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    S = []
    result = 0
    x = y = 0 # 2의 좌표
    for r in range(N):
        if 2 in arr[r]:
            x = r
            y = arr[r].index(2)
    
    visit = [[0] * N for _ in range(N)]
    count = 0
    d = DFS(x, y, count, S)
    # print(count)
    if d == None:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, d))
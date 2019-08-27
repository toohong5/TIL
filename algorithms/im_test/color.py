import sys
sys.stdin = open('1.txt', 'r')

# 칠해야 하는 영역을 먼저 탐색해서...

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    count = [0] * 11
    for _ in range(K):
        result = 0
        row1, col1, row2, col2, color = map(int, input().split())
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                if arr[r][c] <= color:
                    result = 1
        # if result == 0: continue 
        # continue: 컨티뉴 뒤의 내용을 건너뛰고 다시 올라간다.
                else:
                    result = 0
                    break
            if result == 0:
                break

        if result == 1:
            for x in range(row1, row2 + 1):
                for y in range(col1, col2 + 1):
                    arr[x][y] = color
    # count 세기
    for i in range(11):
        for a in range(N):
            for b in range(M):
                if arr[a][b] == i:
                    count[i] += 1

    print('#{} {}'.format(tc, max(count)))

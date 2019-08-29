import sys; sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    map = []
    for _ in range(N):
        map.append(list(input()))
    for s in map:
        print(s)
    type = {'A':2, 'B':3, 'C':4}
    for i in range(N):
        for j in range(N):      # i: 행값, j:열값
            if map[i][j] != 'H' and map[i][j] != 'X':
                for k in range(1, type[map[i][j]]):
                    if j + k < N and map[i][j + k] == 'H': # 우
                        map[i][j + k] = 'X'
                    if j - k >= 0 and map[i][j - k] == 'H': # 좌
                        map[i][j - k] = 'X'
                    if i + k < N and map[i + k][j] == 'H':  # 하
                        map[i + k][j] = 'X'
                    if i - k >= 0 and map[i - k][j] == 'H': # 상
                        map[i - k][j] = 'X'
    ans = 0
    for i in range(N):
        for j in range(N):  # i: 행값, j:열값
            if map[i][j] == 'H':
                ans += 1
    print('#{} {}'.format(tc, ans))
    for s in map:
        print(s)

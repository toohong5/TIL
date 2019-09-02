import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    S_x = []
    S_y = []
    size_x = []
    size_y = []

    # row
    for i in range(N):
        r = 0
        for j in range(N):
            if arr[i][j] != 0:
                S_x.append(arr[i][j])
            else:
                if len(S_x) != 0:
                    size_x.append(len(S_x))
                    S_x.clear()
                    r = i
                    c = j - 1
                    while r > N:
                        if arr[r][c] != 0:
                            S_y.append(arr[r][c])
                            r += 1
                        else:
                            if len(S_y) != 0:
                                size_y.append(len(S_y))
                                S_y.clear()
                                break

    # column
    # for j in range(N):
    #     for i in range(N):
    #         if not visit_y[i][j]:
    #             if arr[i][j] != 0:
    #                 visit_y[i][j] = 1
    #                 S.append(arr[i][j])
    #             else:
    #                 if len(S) != 0:
    #                     size_y.append(len(S))
    #                     S.clear()

print(size_x, size_y)
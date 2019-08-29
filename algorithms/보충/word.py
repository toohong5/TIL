import sys
sys.stdin = open('word_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 1: white, 0: black
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1일때 세기 시작해서 0나오면 stop
    count1 = 0
    result1 = 0
    for r in range(N):
        c = -1
        while c < N - 1:
        # for c in range(N):
            c += 1
            if arr[r][c] == 1: # 행
                k = c
                while arr[r][k] != 0:
                    k += 1
                # for k in range(c, N):
                    if arr[r][k] == 0:
                        c = k
                        break
                    elif arr[r][k] == 1:
                        count1 += 1
                # print(count1)
                if count1 != K:
                    count1 = 0
                    break
                else:
                    result1 += 1
    # print(result1)
    # print(count1)
    count2 = 0
    result2 = 0        
    for r in range(N):
        c = -1
        while c < N - 1:
            c += 1
        # for c in range(N):
            if arr[c][r] == 1: # 열
                for k in range(c, N):
                    if arr[k][r] == 0:
                        c = k
                        break
                    else:
                        count2 += 1
                # print(count)
                if count2 != K:
                    count2 = 0
                    break
                else:
                    result2 += 1
                    # break
    print('#{} {}'.format(tc, result1 + result2))
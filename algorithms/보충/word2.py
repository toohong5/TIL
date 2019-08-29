import sys
sys.stdin = open('word_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 1: white, 0: black
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for r in range(N):
        count = 0
        c = 0
        while c < N:
            if arr[r][c] == 1:
                count += 1
                c += 1
            else:
                if count == K:
                    result += 1
                    count= 0
                    c += 1
                else:
                    count = 0
                    c += 1
        if count == K:
            result += 1

    result2 = 0
    for c in range(N):
        count = 0
        r = 0
        while r < N:
            if arr[r][c] == 1:
                count += 1
                r += 1
            else:
                if count == K:
                    result2 += 1
                    count= 0
                    r += 1
                else:
                    count = 0
                    r += 1
        if count == K:
            result2 += 1
    print('#{} {}'.format(tc, result + result2))
    # result2 = 0
    # for c in range(N):
    #     count = 0
    #     r = 0
    #     while r < N:
    #         if arr[c][r] == 1:
    #             count += 1
    #             r += 1
    #         else:
    #             if count == K:
    #                 result2 += 1
    #                 r += 1
    #             else:
    #                 count = 0
    #                 r += 1

    # print('#{} {}'.format(tc, result2 + result))
                



    # result = 0
    # for r in range(N):
    #     c = 0
    #     count = 0
    #     while c <= N - 1:
    #         if arr[r][c] == 0:
    #             if count == K:
    #                 result += 1
    #                 c += 1
    #             else:
    #                 count = 0
    #                 c += 1
    #         else:
    #             count += 1
    #             c += 1
    #     if count == K:
    #         result += 1

    # print(result)
    # result2 = 0
    # c = 0
    # for c in range(N):
    #     count = 0
    #     while r <= N - 1:
    #         if arr[r][c] == 0:
    #             if count == K:
    #                 result2 += 1
    #                 r += 1
    #             else:
    #                 count = 0
    #                 r += 1
    #         else:
    #             count += 1
    #             if count == K:
    #                 result2 += 1
    #                 r += 1
    #             else:
    #                 r += 1
    
    # print(result + result2)


        # while c < N:
        #     if arr[r][c] == 1:
        #         k = c
        #         count = 0
        #         while k < N:
        #             if arr[r][k] == 0:
        #                 c = k
        #                 break
        #             elif k == N - 1 and arr[r][k] == 1:
        #                 count += 1
        #                 break
        #             else:
        #                 count += 1
        #             k += 1
        #         if count == K:
        #             result += 1
                
    # print(result)

            # c += 1
import sys
sys.stdin = open('sample_input5.txt', 'r')

for tc in range(10):
    n = int(input())
    arr = [input() for i in range(100)]
    N = len(arr)
    M = 1
    count = 0
    length_m = []
    #-------------------------
    # 세로행렬
    col_list = []
    for c in range(N):
        w = ''
        for r in range(N):
            w += arr[r][c]
        col_list.append(w)
    # print(col_list)
    for row in arr:
        while M <= N:
            for start in range(N-M+1):
                end = start + M
                if row[start:end] == row[start:end][::-1]:
                    if M not in length_m:
                        length_m.append(M)
            M += 1
        M = 1
        
    for col in col_list:
        while M <= N:
            for start in range(N-M+1):
                end = start + M
                if col[start:end] == col[start:end][::-1]:
                    if M not in length_m:
                        length_m.append(M)
            M += 1
        M = 1
        
    print('#{} {}'.format(tc+1, max(length_m)))


    # 뒤에서 부터 시작위치를 한칸씩 옮겨가며 찾아보기
    ans = 1
    for idx in range(100): # 모든 행
        for s in range(100): # start의 위치(0~99 까지)
            for e in range(99, s, -1): # 99부터 start까지
                L = e - s + 1 
                if ans >= L: break
                for i in range(L//2):
                    if arr[idx][s + i] != arr[idx][e - i]: break
                else:
                    ans = L
                if ans >= L: break
                for i in range(L//2):
                    if arr[s + i][idx] != arr[e - i][idx]: break
                else:
                    ans = L
    print(ans)

    # 중간에서 늘려가면서 찾는 방법
    # 길이가 짝수인 회문
    for idx in range(100):
        for x in range(100):
            # 길이가 짝수인 경우에는 x -> l(왼쪽)
            l, r, cnt = x, x+1, 0
            while l>=0 and r<100:
            if arr[idx][l] != arr[idx][r]: break
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)

            l, r, cnt = x, x+1, 0
            while l>=0 and r<100:
            if arr[l][idx] != arr[r][idx]: break
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)

            # 길이가 홀수인 경우
            l, r, cnt = x, x+1, 1
            while l>=0 and r<100:
            if arr[idx][l] != arr[idx][r]: break
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)

            l, r, cnt = x, x+1, 1
            while l>=0 and r<100:
            if arr[l][idx] != arr[r][idx]: break
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)
    
    
    # for row in range(N):
    #     for start in range(N - M + 1):
    #         end = start + M - 1
    #         for i in range(M // 2):
    #             if arr[row][start + i] != arr[row][end - i]:
    #                 break
    #         else:
    #             if M not in length_m:
    #                 length_m.append(M)
    #             M += 1
    
    # print(length_m)
    
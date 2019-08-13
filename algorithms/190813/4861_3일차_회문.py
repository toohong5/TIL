import sys
sys.stdin = open('sample_input2.txt', 'r')

n = int(input())
for tc in range(1, n+1):
    N, M = map(int, input().split())    
    words_list = [input() for i in range(N)]
    
    # 세로 행렬
    words_col_list = []
    
    for c in range(N):
        w=''
        for r in range(N):
            w += words_list[r][c]
        words_col_list.append(w)
        
    p=''
    for row in words_list:        
        for start in range(N - M + 1):  # 시작위치
            end = start + M
            if row[start:end] == row[start:end][::-1]:
                p = row[start:end]
                break
    
    for col in words_col_list:
        for start in range(N - M + 1):  # 시작위치
            end = start + M
            if col[start:end] == col[start:end][::-1]:
                p = col[start:end]
                break

    print('#{} {}'.format(tc, p))

#------------ 인덱스 이용------------------
for tc in range(1, n + 1):
    N, M = map(int, input().split())
    words_list = [input() for i in range(arr[0])]

    p = ''

    # 가로
    for row in range(N):
        for start in range(N - M + 1):
            end = start + M - 1


    # 세로
#---------------------------------
# n = int(input())
# for k in range(1, n+1):
#     N, M = map(int, input().split())    
#     words_list = [input() for i in range(arr[0])]
#     p = ''
    
#     # 세로 행렬
#     words_col_list = []
#     w = ''
#     for c in range(N):
#         for r in range(N):
#             w += words_list[r][c]
#         words_col_list.append(w)
#         w=''
    
#     p=''
#     if N == M:
#         for i in words_list:
#             if i == i[::-1]:
#                         p = i
#         else:
#             for j in words_col_list:
#                 if j == j[::-1]:
#                     p = j
    
#     elif M != N:
#         for a in range(N):
#             for start in range(N - M + 1):
#                 end = start - M + 1
#                 for b in range(M // 2):
#                     if words_list[a][start + b] != words_list[a][end - b]:
#                         # print(words_list[start][0][b])
#                         break
#                     # elif words_col_list[start + j] != words_col_list[end - j]:
#                     #     break
#                 else:
#                     p += words_list[a][start+b]

#     print('#{} {}'.format(k, p))
# #-----------------------------
# """
# start = 0~N
# end = start + m -1
# 회문인지 비교횟수  = m/2

# arr = []
# N=M=0 # N: 행의길이, M: 찾을 회문길이
# # 시작위치 0~ N-M
# for row in range(N):
#     for start in range(N-M+1):
#         end = start + M - 1
#         for i in range(M/2):
#             if arr[start + i] != arr[end - i]:
#                 break
#         else:
#             # 회문 찾음




# arr = []
# N = M = 0#N은 행의 길이 M은 찾을 회문의 길이
# for row in range(N):
#     for start in range(N - M + 1):#한 행의 모든 시작 위치: 0~N-M
#         end = start + M - 1
#         for i in range(M//2):#회문인지 조사하기 위한 비교 횟수가 M//2
#             if arr[row][start+i] != arr[row][end-i]:#열이면 arr[start+i][row]식으로~
#                 break
#         else:
#             #회문 찾음
# """              
import sys
sys.stdin = open('sample_input1.txt', 'r')

for _ in range(10):
    n = int(input())
    ladder = [list(map(int,input().split())) for i in range(100)]

    # 출발점 구하기
    start_x = start_y = 0
    for p in range(100):
        for q in range(100):
            if ladder[p][q] == 2:
                start_x = p
                start_y = q
    
    x = 99
    while x:
        if start_y - 1 >= 0 and ladder[x][start_y - 1] == 1:
            ladder[x][start_y] = 0
            start_y -= 1
        elif start_y + 1 <= 99 and ladder[x][start_y + 1] == 1:
            ladder[x][start_y] = 0
            start_y += 1
        else:
            x -= 1
    print('#{} {}'.format(_ + 1, start_y))
    #     if ladder[x-1][start_y - 1] != 1 and ladder[x-1][start_y + 1] != 1 and ladder[x-2][start_y] == 1:
    #         x -= 1
    #     elif ladder[x][start_y - 1] == 1:
    #         start_y -= 1
    #     elif ladder[x][start_y + 1] == 1:
    #         start_y += 1

    #     if x == 0:
    #         break
        
    # print(start_y)


        # for row in range(98, -1, -1):
        #     if ladder[row][start_y] == 1:

# --------------------------------------------------
# 쌤풀이 1
# for tc in range(1, 11):
#     N = input()
#     arr = [list(map(int,input().split()) for _ in range(100)]
#     # 진행 중 방향정보 필요
#     # 교차점 만나면 좌, 우, 위로 이동하는 방향 결정
#     # 올라가다가 왼쪽 혹은 오른쪽 길이 있으면 방향 변경
    
#     # 출발점
#     x, y = 99, 0
#     for i in range(100):
#         if arr[99][i] == 2:
#             y = i
#             break # 현재위치 찾고 break

#     dir = 0 # (방향정보) 0: 위, 1: 왼쪽, 2: 오른쪽
#     while x: # x==0이면 종료
#         # 왼쪽
#         if dir != 2 and y - 1 >= 0 and arr[x][y - 1]:
#             y, dir = y - 1, 1
#         # 오른쪽
#         elif dir != 1 and y + 1 < 100 and arr[x][y + 1]:
#             y, dir = y + 1, 2
#         else:
#             x, dir = x - 1, 0
#     print(y)

# # 2
# # 양쪽을 살피며 올라가다가 길이 나오면 쭉 가서 한칸 올림.
# for tc in range(1, 11):
#     N = input()
#     arr = [list(map(int,input().split()) for _ in range(100)]
#     # 진행 중 방향정보 필요
#     # 교차점 만나면 좌, 우, 위로 이동하는 방향 결정
#     # 올라가다가 왼쪽 혹은 오른쪽 길이 있으면 방향 변경
    
#     # 출발점
#     x, y = 99, 0
#     for i in range(100):
#         if arr[99][i] == 2:
#             y = i
#             break # 현재위치 찾고 break

#     while x: # x==0이면 종료
#         # 왼쪽
#         if y - 1 >= 0 and arr[x][y-1]:
#             while  y - 1 >= 0 and arr[x][y-1]:# 왼쪽에 길이 있으면 계속가고 끝까지 가면 한칸 올림
#                 y -= 1
#             x -= 1
#         # 오른쪽
#         elif y + 1 < 100 and arr[x][y + 1]:
#             while y + 1 < 100 and arr[x][y + 1]:
#                 y += 1
#             x -= 1
#         else:
#             x -= 1

#     print(y)

# # 3 재귀호출(DFS)(그래프 탐색 유사)
# def DFS(x, y):
#     if x == 0: return y

#     arr[x][y] = 0 # 방문한 길 지우기
#     if y - 1 >= 0 and arr[x][y - 1]:
#         return DFS(x, y - 1)
#     elif y + 1 < 100 and arr[x][y + 1]:
#         return DFS(x, y + 1)
#     else:
#         return DFS(x - 1, y)

# # 전역변수
# ans = -1
# def DFS(x, y):
#     global ans
#     if x == 0:
#         ans = y
#         return
#     arr[x][y] = 0 # 방문한 길 지우기
#     if y - 1 >= 0 and arr[x][y - 1]:
#         DFS(x, y - 1)
#     elif y + 1 < 100 and arr[x][y + 1]:
#         DFS(x, y + 1)
#     else:
#         DFS(x - 1, y)
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = []

# 100*100 배열 불러오기
for i in range(100):
    num = input().split()
    arr.append(num)


n, m = len(arr), len(arr[0])

# 행의 합
row_sum = []
sum1 = 0

for i in range(n):
    for j in range(m):
        sum1 += int(arr[i][j])
    row_sum.append(sum1)
    sum1 = 0
print(row_sum)

# 열의 합
column_sum = []
sum2 = 0

for i in range(n):
    for j in range(m):
        sum2 += int(arr[j][i])
    column_sum.append(sum2)
    sum2 = 0
print(column_sum)

cross_sum1 = []
sum3 = 0

for i in range(n):
    for j in range(m):
        if i == j:
            sum3 += int(arr[i][j])
    cross_sum1.append(sum3)
print(cross_sum1)

cross_sum2 = []
sum4 = 0

for i in range(n):
    for j in range(m):
        if i + j == 99:
            sum4 += int(arr[i][j])
    cross_sum2.append(sum4)
print(cross_sum2)

max1 = max(row_sum)
max2 = max(column_sum)
max3 = max(cross_sum1)
max4 = max(cross_sum2)

result = max(max1, max2, max3, max4)
print(result)


# 선생님 풀이
for tc in range(1, 11):
    N = input()
    arr = [list(map(int, input().split())) for i in range(100)]

    # 한꺼번에 하기!
    ans = 0
    dsum1 = dsum2 = 0
    for i in range(100):
        rsum = csum = 0
        dsum1 += arr[i][i]
        dsum2 += arr[i][99 - i]
        for j in range(100):
            rsum += arr[i][j]
            csum += arr[j][i]
        ans = max(ans, rsum, dsum1, dsum2)
    print(ans)

    # # 열들의 합
    # ans = 0
    # for i in range(100):
    #     S = 0
    #     for j in range(100):
    #         S += arr[j][j]
    #     ans = max(ans, S)
    # # 우상단 -> 좌하단
    # S = 0
    # for i in range(100):
    #     S += arr[i][99-i]
    # ans = max(ans, S)
    #
    # # 좌상단 -> 우하단
    # S = 0
    # for i in range(100):
    #     S += arr[i][i]
    # ans = max(ans, S)






# # 우대각의 합
# cross_sum1 = []
# sum3 = 0
# max3 = 0
# for diag in range(0, n + m - 1):    # diag: 사선의 수
#                                     # x, y: 시작 좌표
#     x = 0 if diag < m else (diag - m + 1)
#     y = diag if diag < m else m - 1
#
#     while x < n and y >= 0:
#         sum3 += int(arr[x][y])
#         x += 1
#         y -= 1
#     cross_sum1.append(sum3)
#     sum3 = 0
# print(cross_sum1)
#
# # 좌대각의 합
# cross_sum2 = []
# sum4 = 0
# max4 = 0
# for diag in range(0, n + m - 1):    # diag: 사선의 수
#                                     # x, y: 시작 좌표
#     x = 0 if diag < m else (diag - m + 1)
#     y = diag if diag < m else m-1
#
#     while x < n and y >= 0:
#         sum4 += int(arr[y][x])
#         x -= 1
#         y += 1
#     cross_sum2.append(sum4)
#     sum4 = 0
# print(cross_sum2)

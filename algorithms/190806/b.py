import sys
sys.stdin = open('input2_6.txt', 'r')

bingo = [list(map(int, input().split())) for _ in range(5)]
ans = [list(map(int, input().split())) for _ in range(5)]
answer = []
for p in range(5):
    for q in range(5):
        answer.append(ans[p][q])
result = 0
count = 0
sum_list = []

diag_sum1 = 0
diag_sum2 = 0
for r in range(len(bingo)):
    row_sum = 0
    col_sum = 0
    for c in range(len(bingo[0])):
        for i in range(len(answer)):
            if answer[i] == bingo[r][c]:
                bingo[r][c] = 0
                result += 1
                break
        row_sum += bingo[r][c]
        col_sum += bingo[c][r]
        
    diag_sum1 += bingo[r][r]
    diag_sum2 += bingo[r][5 - r - 1]

    if row_sum == 0:
        sum_list.append(row_sum)
        if len(sum_list) == 3:
            break
    if col_sum == 0:
        sum_list.append(col_sum)
        if len(sum_list) == 3:
            break
if diag_sum1 == 0:
    sum_list.append(diag_sum1)
    if len(sum_list) == 3:
        print(result)
if diag_sum2 == 0:
    sum_list.append(diag_sum2)
    if len(sum_list) == 3:
        print(result)
if len(sum_list) == 3:               
    print(result)
import sys
sys.stdin = open('bingo.txt', 'r')

bingo = [list(map(int, input().split())) for _ in range(5)]
ans = [list(map(int, input().split())) for _ in range(5)]
answer = []
for x in range(5):
    for y in range(5):
        answer.append(ans[x][y])
result = 0
for i in answer:
    count = 0
    for r in range(5):
        for c in range(5):
            if i == bingo[r][c]:
                bingo[r][c] = 0
                result += 1

    row_sum = 0
    diag_sum1 = 0
    diag_sum2 = 0
    for x in range(5):
        col_sum = 0
        row_sum = sum(bingo[x])
        if row_sum == 0:
            count += 1
        diag_sum1 += bingo[x][x]
        diag_sum2 += bingo[x][5 - x - 1]
        for y in range(5):
            col_sum += bingo[y][x]
        if col_sum == 0:
            count += 1
    if diag_sum1 == 0:
        count += 1
    if diag_sum2 == 0:
        count += 1
    if count >= 3:
        break

print(result)
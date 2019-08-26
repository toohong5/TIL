import sys
sys.stdin = open('sum_input.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    max_sum = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        # diag_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr [j][i]
        
        max_sum = max(max_sum, row_sum, col_sum)
    # print(max_sum)

    diag_sum1 = 0
    diag_sum2 = 0

    for k in range(100):
        diag_sum1 += arr[k][k]
        diag_sum2 += arr[k][100-k-1]
    
    print('#{} {}'.format(tc, max(diag_sum1, diag_sum2, max_sum)))
            # if i == j:
            #     diag_sum += arr[i][j]
            # elif j == 100 - 1 - i:
            #     diag_sum += arr[i][j]

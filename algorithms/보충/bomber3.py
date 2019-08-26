import sys
sys.stdin = open('bomber.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    max_sum = 0
    a = b = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sum = 0
            for r in range(i, i + m):
                for c in range(j, j + m):
                    sum += arr[r][c]
            if max_sum < sum:
                max_sum = sum
                a = i
                b = j
            
    print('#{} {} {} {}'.format(tc, a, b, max_sum))
    # print(max_sum)

            
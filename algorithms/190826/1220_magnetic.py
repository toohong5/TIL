import sys
sys.stdin = open('input1.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    result = 0
    for col in range(N):
        for i in range(N):
            if arr[i][col] == 1:
                for j in range(i + 1, N):
                    if arr[j][col] == 2:
                        result += 1
                        break
                    elif arr[j][col] == 1:
                        break
    print('#{} {}'.format(tc, result))
    
import sys
sys.stdin = open('sample_input4.txt', 'r')

for tc in range(10):
    M = int(input())
    arr = [input() for i in range(8)]
    
    N = len(arr)
    count = 0
    for row in range(N):
        for start in range(N - M + 1):
            end = start + M - 1
            for i in range(M // 2):
                if arr[row][start + i] != arr[row][end - i]:
                    break
            else:
                count += 1
    
    for col in range(N):
        for start in range(N - M + 1):
            end = start + M - 1
            for i in range(M // 2):
                if arr[start + i][col] != arr[end - i][col]:
                    break
            else:
                count += 1
    print('#{} {}'.format(tc+1, count))
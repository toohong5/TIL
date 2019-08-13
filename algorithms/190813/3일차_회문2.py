import sys
sys.stdin = open('sample_input5.txt', 'r')

for tc in range(10):
    n = int(input())
    arr = [input() for i in range(100)]
    
    N = len(arr)
    M = 3
    count = 0
    length_m = []
    for row in range(N):
        for start in range(N - M + 1):
            end = start + M - 1
            for i in range(M // 2):
                if arr[row][start + i] != arr[row][end - i]:
                    break
            else:
                if M not in length_m:
                    length_m.append(M)
                M += 1
    
    print(length_m)
    
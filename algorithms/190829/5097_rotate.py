import sys
sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for i in range(M):
        arr.append(arr.pop(0))
        # first = arr.pop(0)
        # arr.append(first)
    print('#{} {}'.format(tc, arr[0]))
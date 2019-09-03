import sys
sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    i = 0
    for _ in range(K):
        i += M
        if (i - 1) >= 0 and i < len(arr):
            arr.insert(i, arr[i-1] + arr[i])
        elif i > len(arr):
            i = i - len(arr)
            if (i - 1) >= 0 and i < len(arr):
                arr.insert(i, arr[i-1] + arr[i])
        elif i == len(arr):
            arr.append(arr[i-1] + arr[0])

    print('#{}'.format(tc), end = ' ')
    if len(arr) < 10:
        for i in range(len(arr)-1, 0, -1):
            print(arr[i], end = ' ')
        print(arr[0])
    else:
        for i in range(-1, -10, -1):
            print(arr[i], end = ' ')
        print(arr[-10])
import sys
sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        info = list(input().split())
        if info[0] == 'I':
            arr.insert(int(info[1]), int(info[2]))
        elif info[0] == 'D':
            arr.pop(int(info[1]))
        elif info[0] == 'C':
            arr[int(info[1])] = int(info[2])

    result = 0
    try:
        result = arr[L]
    except IndexError:
        result = -1

    print('#{} {}'.format(tc, result))
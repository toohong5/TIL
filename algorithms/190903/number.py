import sys
sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        index, num = map(int, input().split())
        arr.insert(index, num)
    print('#{} {}'.format(tc, arr[L]))
import sys
sys.stdin = open('minmax_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    print('#{} {}'.format(tc, max(arr) - min(arr)))
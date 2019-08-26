import sys
sys.stdin = open('input5.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    n = 0
    while n < N:
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
        n += 1
    print('#{} {}'.format(tc, max(arr)-min(arr)))


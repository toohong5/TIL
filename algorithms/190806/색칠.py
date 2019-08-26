import sys
sys.stdin = open('input2_1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    count = 0
    for _ in range(N):
        box = list(map(int, input().split()))
        for i in range(box[0], box[2]+1):
            for j in range(box[1], box[3]+1):
                if arr[i][j] == 0:
                    arr[i][j] = box[-1]
                elif arr[i][j] != 0 and arr[i][j] != box[-1]:
                    arr[i][j] = box[-1]
                    count += 1
    print('{} {}'.format(tc, count))
        
import sys
sys.stdin = open('input2_8.txt', 'r')

T = int(input())
arr = [[0] * 101 for _ in range(101)]
for k in range(1, T + 1):
    box = list(map(int, input().split()))
    for i in range(box[0], box[0] + box[2]):
        for j in range(box[1], box[1] + box[3]):
            arr[i][j] = k


for a in range(1, T + 1):
    count = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j] == a:
                count += 1
    print(count)
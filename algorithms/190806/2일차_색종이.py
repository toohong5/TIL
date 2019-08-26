import sys
sys.stdin = open('input2_8.txt', 'r')

n = int(input())
arr = [[0] * 101 for _ in range(101)]
# count_list = []
for i in range(1, n + 1):
    box = list(map(int, input().split()))
    for p in range(box[0], box[0] + box[2]):
        for q in range(box[1], box[1] + box[3]):
            arr[p][q] = i
            
for j in range(1, n + 1):
    count = 0
    for x in range(101):
        for y in range(101):
            if arr[x][y] == j:
                count += 1
    print(count)

        
    # print(count_list)

    # print(arr[i-1].count(i))

    

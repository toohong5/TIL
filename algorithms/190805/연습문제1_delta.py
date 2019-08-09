arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
sum = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(len(dx)):
            tx, ty = dx[i] + x, dy[i] + y
            if tx < 0 or tx == len(arr) or ty < 0 or ty == len(arr[0]): continue
            sum += abs(arr[tx][ty] - arr[x][y])

            result.append(sum)
sum2 = 0
for i in result:
    sum2 += i

print(sum2)
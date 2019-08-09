arr = [3, 6, -2, 7, -3, 1, -8, -1, 5, 4]

# 0이 되는 경우의 부분집합의 원소들을 한줄에 하나씩 출력해보기!

# 합이 0이되는 부분집합 구하기!!
N = len(arr)

for subset in range(1 << N):
    print(subset, end='> ')
    for j in range(N):
        if subset & (1 << j):
            print(arr[j], end=' ')
    print()

# 합이 0이되는 부분집합 구하기!!
arr = [3, 6, -2, 7, -3, 1, -8, -1, 5, 4]
N = len(arr)

for i in range(1, 1 << N):
    Sum = 0
    for j in range(N):
        if i & (1 << j):
            Sum += arr[j]

    if Sum == 0:
        for j in range(N):
            if i & (1 << j):
                print(arr[j], end=' ')
        print()
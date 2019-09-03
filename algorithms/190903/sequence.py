import sys
sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    for _ in range(M - 1):
        arr2 = list(map(int, input().split()))
        max_num = 0
        index = 0
        for n in arr1:
            if n > arr2[0]:
                max_num = n
                index = arr1.index(max_num)
                for i in range(len(arr2) - 1, -1, -1):
                    arr1.insert(index, arr2[i])
                break
        else:
            arr1.extend(arr2)
    print('#{}'.format(tc), end=' ')
    for j in range(-1, -10, -1):
        print(arr1[j], end=' ')
    print(arr1[-10])
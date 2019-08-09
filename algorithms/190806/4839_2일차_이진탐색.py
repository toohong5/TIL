import sys
sys.stdin = open('input2_3.txt', 'r')

N = int(input())

for i in range(1, N + 1):
    pages = list(map(int, input().split()))
    start = 1
    total = pages[0]
    key_a = pages[1]
    key_b = pages[2]

    count_a = 0
    count_b = 0

    while start <= total:
        c = int((start + total) / 2)
        if c == key_a:
            break
        if c > key_a:
            count_a += 1
            total = c
        else:
            count_a += 1
            start = c

    start = 1
    total = pages[0]
    while start <= total:
        c = int((start + total) / 2)
        if c == key_b:
            break
        if c > key_b:
            count_b += 1
            total = c
        else:
            count_b += 1
            start = c
    result = ''
    if count_a > count_b:
        result = 'B'
    elif count_a < count_b:
        result = 'A'
    else:
        result = 0

    print('#{} {}'.format(i, result))

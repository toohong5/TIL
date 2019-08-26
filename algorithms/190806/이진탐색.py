import sys
sys.stdin = open('input2_3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())

    start = 1
    total = N
    count_a = count_b = 0

    while start <= total:
        c = (start + total)//2
        if c == A:
            break
        elif c > A:
            total = c
            count_a += 1
        else:
            start = c
            count_a += 1

    start = 1
    total = N
    while start <= total:
        c = (start + total)//2
        if c == B:
            break
        elif c > B:
            total = c
            count_b += 1
        else:
            start = c
            count_b += 1
    
    if count_a > count_b:
        print('#{} B'.format(tc))
    elif count_a < count_b:
        print('#{} A'.format(tc))
    else:
        print('#{} 0'.format(tc))
    
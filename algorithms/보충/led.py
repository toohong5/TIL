import sys
sys.stdin = open('im_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = list(map(int,input().split()))
    led = [0] * N
    count = 0

    for i in range(1, N + 1):
        if room[i - 1] != led[i - 1]:
            count += 1
            for j in range(i, N + 1, i):
                if led[j - 1] == 0:
                    led[j - 1] = 1
                else:
                    led[j - 1] = 0
    print(led)
    print('#{} {}'.format(tc, count))
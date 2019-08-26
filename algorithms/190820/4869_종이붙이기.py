import sys
sys.stdin = open('sample_input1.txt', 'r')

n = int(input())
for tc in range(1, n + 1):
    N = int(input())

    def box(length):
        if length == 10:
            return 1
        elif length == 20:
            return 3
        else:
            return box(length - 10) + box(length - 20) * 2

    print('#{} {}'.format(tc, box(N)))

    # N = int(input()) # 가로길이
    # M = 20 # 세로길이
    
    # box = [10, 20]
    # S = []
    
    # while True:
    #     for i in box:
    #         if N/i == 0:

    # for i in range(2):
    #     for j in range(2):
    #         if N - (N / i) * box[i] == 0:
    #             N = N - box[i]*(N / i)
    #             M = M - 20
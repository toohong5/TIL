import sys
sys.stdin = open('index.txt', 'r')

N = int(input())
for k in range(1, N+1):
    nums = list(map(int, input().split()))
    NUMS = list(map(int, input().split()))
    # print(NUMS)

    MIN = NUMS[0]
    MAX = NUMS[-1]
    for i in range(0, len(NUMS)):
        if NUMS[i] < MIN:
            MIN = NUMS[i]
        elif NUMS[i] > MAX:
            MAX = NUMS[i]
    SUB = MAX - MIN

    print('#{} {}'.format(k, SUB))
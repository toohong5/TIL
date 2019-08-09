import sys
sys.stdin = open('input2.txt', 'r')

N = int(input())
for k in range(1, N+1):
    nums = list(map(int, input().split()))
    stops = list(map(int, input().split()))

    K = nums[0] # 최대이동 거리
    n = nums[1] # 정류장 수
    m = nums[2] # 충전기 설치된 정류장 번호
    charges = 0 # 충전횟수

    for i in range(0, n+1):
        for j in range(0, m):
            if stops[j+1] - stops[j] > K:
                print('#{} {}'.format(k, 0))
            else:
                if stops[j] == K:
                    charges += 1
                elif stops[i] < K:

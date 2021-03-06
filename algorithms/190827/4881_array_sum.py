import sys
sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    


# --------------------------------------------------------------------
# 순열 이용
# 열번호를 겹치지 않게 나열한다.

# 1. 순열 라이브러리 이용
from itertools import permutations

def find():
    min = 100 # 원소들의 합을 저장할 예정(최소값)
    for p in permutations(range(N)): # 순열 생성
        s = 0
        for i in range(N):
            s += m[i][p[i]]         # 순열을 이용해 합구하기
        if min > s:
            min = s
    return min

for tc in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for x in range(N)] # 중첩리스트에 숫자 저장
    print('#{} {}'.format(tc, find()))

# 2. 순열 직접 구하기
def find(n, s):             # n은 순열의 인덱스, s는 생성된 부분까지의 합
    global minV
    if n == N:              # 순열이 완성된 경우
        if minV > s:        # 기존의 최소값 보다 작으면
            minV = s
        return
    elif minV <= s:         # 순열 완성되지 않았지만 최소값보다 작은경우
        return
    else:
        for i in range(N):
            if u[i] == 0:
                u[i] = 1
                find(n + 1, s+m[n][i])
                u[i] = 0
            return

for tc in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for x in range(N)] # 중첩리스트에 숫자 저장
    u = [0 for _ in range(N)]
    minV = 100
    find(0, 0)
    # print('#{} {}'.format(tc, find()))
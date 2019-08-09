import sys
sys.stdin = open('input2_1.txt', 'r')

N = int(input())
for i in range(1, N + 1): # 전체 테스트 케이스 횟수
    n = int(input())
    arr = [[0] * 10 for i in range(10)]
    count = 0
    for j in range(n): # 한 테스트 케이스에서 반복
        n_list = list(map(int, input().split()))
        # color = 1
        for p1 in range(n_list[0], n_list[2]+1):
            for q1 in range(n_list[1], n_list[3]+1):
                if arr[p1][q1] == 0:
                    arr[p1][q1] = n_list[4]
                elif arr[p1][q1] != 0 and arr[p1][q1] != n_list[4]:
                    count += 1
    print('#{} {}'.format(i, count))


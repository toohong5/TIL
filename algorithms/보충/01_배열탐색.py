import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 한 번에 읽기
    arr = [list(map(int, input().split())) for _ in range(N)]

    """
    # 한 줄씩 읽는 방법
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    """

    # 행우선 순회
    # 모든 자료의 합
    total = 0
    sum = []
    min_sum = 100000
    for i in range(N): # 0 ~ N-1
        row_sum = 0 # 새로운 행에 들어갈때 마다 초기화 (행의 합)
        col_sum = 0
        for j in range(N): # 0 ~ N-1
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        min_sum = min(min_sum, row_sum, col_sum)
    # print(min_sum)
        # if col_sum > row_sum and min_sum > row_sum:
        #     min_sum = row_sum
        # if col_sum < row_sum and min_sum > col_sum:
        #     min_sum = col_sum

    # 대각의 합 구하기
    s = 0
    for i in range(N): # 좌상단 -> 우하단
        s += arr[i][i]
    s2 = 0    
    for i in range(N): # 우상단 -> 좌하단
        s2 += arr[i][N - 1 - i]

    # 사각행렬 -> 색칠하기 문제!!! 풀어보기이
    # 전체 크기가 N*N, M*M을 찾을 때
    # 좌상단이 있을 수 있는 위치를 모두 찾는다.(0,0), (N-M,N-M), (0, N-M), (N-M, 0)

    # 모든 M*M의 좌상단 좌표를 생성하기
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 좌상단 (i,j), 가로/세로길이 = M 사각영역을 행우선 탐색
            # (좌상단 좌표에 대한 사각형 만들기)
            for r in range(i, i + M): # i ~ i+M-1까지 돌아야 함
                for c in range(j, j + M): # j ~ j+M-1까지 돌아야 함
                    arr[r][c]

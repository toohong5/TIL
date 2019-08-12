# 요리사 문제

# 이진탐색 이용해 모든 그룹을 두 그룹으로 나눈다.


# 부분집합 만들기(같은 개수의 두 그룹 만들기!)_최적화 문제
arr  = [10,20,30,40]
N = 4

for set in range(1 << 4):
    A, B = [], []
    for i in range(N):
        if set & (1 << i):
            A.append(arr[i])
        else:
            B.append(arr[i])
    if len(A) == len(B):
        print(A, B)
        # 두 그룹에 들어가는 개수가 같은거에 대해서만 계산하기
        # 중복 포함되어 있음


# 금속막대
# 순열을 생성해서 백트레킹스타일로...
# 화학물질 문제 
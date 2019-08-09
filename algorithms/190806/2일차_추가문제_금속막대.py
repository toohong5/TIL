import sys
sys.stdin = open('input2_5.txt', 'r')

N = int(input())

for i in range(1, N + 1):
    n = int(input())
    length_list = list(map(int, input().split()))
    l_list = []
    # 수나사 굵기, 암나사 굵기를 리스트로 묶음
    while len(l_list) != n:
        l_list.append([length_list[0], length_list[1]])
        length_list.remove(length_list[0])
        length_list.remove(length_list[0])
    # print(l_list)
    
    # 기준 : [1]
    N = len(l_list)
    M = len(l_list[0])
    count_x = 0
    count_y = 0
    l_start = 0
    
    for p in range(N):
        for q in range(M):
            if l_list[p][0] in l_list[p][1]:
                count_x += 1

        # if l_list.count(l_list[p][0]) == 1:
        #     l_start = l_list[p][0]

        # print(l_start)


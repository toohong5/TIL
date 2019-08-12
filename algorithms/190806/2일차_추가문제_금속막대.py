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
    # 기준 : [1]
    
    N = len(l_list)
    M = len(l_list[0])
    
    for p in range(N):
        a = True
        for q in range(N):
            if l_list[p][0] == l_list[q][1]:
                 a = False
                 break
        if a:
            l_list[p], l_list[0] = l_list[0], l_list[p]
            break

    for p in range(N-1):
        for q in range(p+1, N):
            if l_list[p][1] == l_list[q][0]:
                l_list[p+1], l_list[q] = l_list[q], l_list[p+1]
    
    list_str = ''
    for p in range(N):
        for q in range(M):
            list_str += str(l_list[p][q]) + ' '

    print('#{} {}'.format(i, list_str))
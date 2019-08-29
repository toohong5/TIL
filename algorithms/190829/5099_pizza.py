import sys
sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    index = [i for i in range(1, M + 1)] # 1 ~ M번 피자 번호
    q = []
    # front = rear = 0
    # 피자 n만큼 넣고 굽고 확인하고 남아있으면 다시 맨 뒤로 보내고 
    # 치즈 0 되면 빼고 새로운 피자 넣기
    for i in range(M):
        if len(q) == N:
            break
        else:
            q.append(index.pop(0))

    result = 0
    while True:
        # for i in range(N):              # N번 돌림
        p = q.pop(0)                # 첫번째 피자 꺼내기
        cheeze = pizza[p - 1] // 2  # 치즈//2 값 확인하기
        pizza[p - 1] = cheeze
        if cheeze != 0:             # 치즈 0 아니면 다시 넣기
            q.append(p)
        elif cheeze == 0:
            if len(index) != 0:           # 치즈 0이면 새로운 피자 추가
                q.append(index.pop(0))
        if len(q) == 1:
            result = q.pop(0)
            break

    print('#{} {}'.format(tc, result))


    
    

    
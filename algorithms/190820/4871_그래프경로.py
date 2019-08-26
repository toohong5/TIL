import sys
sys.stdin = open('sample_input2.txt', 'r')

n = int(input())
for tc in range(1, n + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)

    s, g = map(int, input().split())

    result = 0
    
    # # 재귀호출
    visit = [0] * (V + 1)
    def DFS(v):
        visit[v] = 1
        for w in G[v]:
            if not visit[w]:
                DFS(w)
    DFS(s)
    print(visit[g])

    # def DFS(v):
    #     S = []
    #     visit = [0] * (V + 1)
    #     visit[v] = 1
    #     # print(v, end=' ')
    #     S.append(v)
    #     list_w = []
    #     while S:
    #         for w in G[v]:
    #             if not visit[w]:
    #                 visit[w] = 1
    #                 # print(w, end=' ')
    #                 S.append(v)
    #                 v = w
    #                 list_w.append(v)
    #                 break
    #         else:
    #             v = S.pop()
    #     return list_w

    # if g in DFS(s):
    #     result = 1

    # print('#{} {}'.format(tc, result))
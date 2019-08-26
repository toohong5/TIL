import sys
sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
    s, g = map(int, input().split())

    visit = [0] * (V + 1)
    w_list = []
    def DFS(v):
        visit[v] = 1
        for w in G[v]:
            w_list.append(w)
            if not visit[w]:
                DFS(w)
        return w_list
            # print()
    print(DFS(s))

    # for i in visit:
    #     if visit == 1:
    #         print(visit.index(i))
    
        
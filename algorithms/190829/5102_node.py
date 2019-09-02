# 간선의 개수 저장하는 배열 혹은 변수
# 인접 리스트?
# 몇번 거쳐가는지...


# 그래프 문제
import sys
from collections import deque
def BFS(start):
    visit = [0] * (V + 1)               # 다녀가서 1이 된 후 방문할 때 마다 1씩 증가시키기...n-1이 되면 거쳐간 간선의 개수가 된다...
    visit[start] = 1
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit[w]:
                q.append(w)
                visit[w] = visit[v] + 1 # 이전에 갔던 곳 + 1
            if w == g:
                return visit[w] - 1


sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
  
    s, g = map(int, input().split())
    
    print(BFS(s))






    
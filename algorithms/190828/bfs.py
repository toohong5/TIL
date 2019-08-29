from queue import Queue
import sys
sys.stdin = open('input1.txt', 'r')

V, E = 7, 7
visit = [0] * (V + 1)
G = [[] for _ in range(V + 1)]
q = Queue()
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

def Q(v):
    q.put(v)
    while q:
        g = q.get()
        if not visit[g]:
            print(q, end=' ')
            visit[g] = 1
            for i in G[g]:
                if not visit[i]:
                    q.put(i)

Q(1)
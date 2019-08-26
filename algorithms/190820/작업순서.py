import sys
sys.stdin = open('sample_input4.txt', 'r')

for tc in range(10):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        for i in range(2):
            u, v = [map(int, input().split())]
            
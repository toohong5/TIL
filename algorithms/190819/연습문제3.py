import sys
sys.stdin = open('04 Stack1_DFS_input.txt', 'r')

# V, E = map(int, input().split()) # 정점수, 간선수

# G = [[] for _ in range(V + 1)] # 정점번호 : 1~V까지 사용

# for _ in range(E):
#     u, v = map(int, input().split())
#     G[u].append(v)
#     G[v].append(u)

# for i in range(1, V + 1):
#     print(i, '-->', G[i]) # 각 정점의 인접정점을 표현

# def DFS(v): # v는 시작점
#     S = []
#     visit = [False] * (V + 1)
#     visit[v] = True # 시작점을 방문한다.
#     print(v, end=' ')
#     S.append(v)     # 시작점을 스택에 push

#     while S:        # 빈 스택이 아닐 동안 반복
#         # v의 방문하지 않은 인접정점을 찾는다. ==> w
#         for w in G[v]:
#             if not visit[w]: # 방문하지 않은 인접정점 찾기
#                 visit[w] = True # w를 방문하고
#                 print(w, end=' ') # 방문순서 출력
#                 S.append(v) # v를 스택에 push
#                 v = w # w를 현재 방문하는 정점으로 설정(다시 반복하기 위함)
#                 break # 빠져나옴
#         else: # 이전에 방문한 정점으로 되돌아 간다.
#             v = S.pop()
# print(DFS(1))

#----------------------------------------------
# 재귀호출

V, E = map(int, input().split()) # 정점수, 간선수
G = [[] for _ in range(V + 1)] # 정점번호 : 1~V까지 사용
visit = [False] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

def DFS(v):
    visit[v] = True; print(v, end=' ') # 현재 방문하는 정점
    for w in G[v]:
        if not visit[w]:
            DFS(w)
print(DFS(1))




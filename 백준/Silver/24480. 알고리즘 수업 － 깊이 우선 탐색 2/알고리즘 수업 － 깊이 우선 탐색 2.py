import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(V):
    global cnt
    visited[V] = cnt # 방문하면 몇 번째 순서인지 저장
    
    for i in graph[V]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
            
N, M, R = map(int, input().split()) # 정점의 수, 간선의 수, 시작 정점
visited = [0] * (N+1) # 정점 방문 여부 저장
graph = [[] for _ in range(N+1)]
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N+1):
    graph[i].sort(reverse=True)

dfs(R)

for i in range(1, N+1):
    print(visited[i])
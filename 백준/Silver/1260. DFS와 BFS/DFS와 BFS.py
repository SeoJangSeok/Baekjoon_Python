from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작 정점
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for adj in graph:
    adj.sort()
    
    
dfs_result = []
bfs_result = []

def dfs(V):
    dfs_result.append(V)
    for adj in graph[V]:
        if adj not in dfs_result:
            dfs(adj)
            
def bfs(V):
    bfs_result.append(V)
    q = deque([V])
    while q:
        current_node = q.popleft()
        for adj in graph[current_node]:
            if adj not in bfs_result:
                bfs_result.append(adj)
                q.append(adj)
            
dfs(V)
bfs(V)

print(*dfs_result)
print(*bfs_result)
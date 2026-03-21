import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 수
edge = int(input()) # 간선의 수
visited = [] # 방문 노드 기록

graph = [[] for _ in range(n+1)]

for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    stack = [node]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for adj in graph[v]:
                stack.append(adj)
dfs(1)
print(len(visited) - 1)
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    order = 2

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if visited[next_node] == 0:
                visited[next_node] = order
                order += 1
                queue.append(next_node)


N, M, R = map(int, input().split())
visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

bfs(R)

for i in range(1, N + 1):
    print(visited[i])

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        node = queue.popleft()
        
        for adj in graph[node]:
            if visited[adj] == 0:
                queue.append(adj)
                visited[adj] = -visited[node]
            elif visited[adj] == visited[node]:
                return True
    return False

K = int(input()) # 테스트 케이스

for _ in range(K):
    V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
    
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [0] * (V+1) # 0: 방문 안함, 1, -1은 서로 다른 그룹
    
    for i in range(1, V+1):
        if visited[i] == 0:
            result = bfs(i)
            if result:
                print('NO')
                break
    else:
        print('YES')
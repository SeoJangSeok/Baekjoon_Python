from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N명, 키를 비교한 횟수
graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

queue = deque()

for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)

answer = []

while queue:
    current = queue.popleft()
    answer.append(current)
    for next_student in graph[current]:
        in_degree[next_student] -= 1
        if in_degree[next_student] == 0:
            queue.append(next_student)

print(*answer, sep=' ')
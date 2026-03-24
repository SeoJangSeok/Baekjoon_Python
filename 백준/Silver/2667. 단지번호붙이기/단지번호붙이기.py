from collections import deque
import sys

input = sys.stdin.readline

N = int(input()) # 지도의 크기 N x N

graph = [list(map(int, input().rstrip())) for _ in range(N)]
result = []
count = 0

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽)으로 한 칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global count
    
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()

print(len(result), *result, sep='\n')
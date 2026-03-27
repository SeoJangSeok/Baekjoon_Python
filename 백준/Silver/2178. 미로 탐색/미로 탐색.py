from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # N x M 크기의 배열, (N, M)까지 도착
maze = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs(si, sj):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((si, sj))
    
    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni = ci + dx[i]
            nj = cj + dy[i]
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj]==1:
                q.append((ni, nj))
                maze[ni][nj] = maze[ci][cj] + 1
    return maze[N-1][M-1]

print(bfs(0, 0))
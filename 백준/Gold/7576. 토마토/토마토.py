from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and box[nx][ny]==0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))

M, N = map(int, input().split()) # 상자의 크기 M x N
box = [list(map(int, input().split())) for _ in range(N)]

# 익은 토마토의 위치 queue에 저장
q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
            
bfs()

day = 0
for row in box:
    for i in row:
        if i == 0: # 익지 않은 토마토가 존재하는 경우(모두 익지 못하는 상황)
            print(-1)
            exit()
    else:
        day = max(day, max(row))
        
print(day - 1)
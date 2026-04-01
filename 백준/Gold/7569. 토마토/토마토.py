from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while queue:
        cz, cx, cy = queue.popleft() # 현재 위치
        for i in range(6):
            nz, nx, ny = cz + dz[i], cx + dx[i], cy + dy[i] # 다음 탐색할 위치
            # 상자 범위를 벗어나지 않고, 익지 않은 토마토가 있다면
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[cz][cx][cy] + 1 # 익은 상태로 변경
                queue.append((nz, nx, ny)) # 다음 탐색할 위치를 큐에 추가
            

M, N, H = map(int, input().split()) # 상자의 크기 M x N, 쌓을 상자의 수 H
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [0, 0, 1, -1, 0, 0] # 앞, 뒤
dy = [-1, 1, 0, 0, 0, 0,] # 좌, 우
dz = [0, 0, 0, 0, 1, -1] # 위, 아래

queue = deque()

# 초기 상태에서 익은 토마토의 위치를 큐에 넣는다.
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 1:
                queue.append((z, x, y))

# BFS 탐색 호출
bfs()

day = 0

for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 0: # 익지 않은 토마토가 있다면 -1 출력 후 종료
                print(-1)
                exit()
            day = max(day, box[z][x][y])
print(day - 1)
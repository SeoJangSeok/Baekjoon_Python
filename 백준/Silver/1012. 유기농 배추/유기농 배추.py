from collections import deque
import sys

input = sys.stdin.readline

def bfs(si, sj):
    q = deque()
    q.append((si, sj)) # 시작 위치 queue에 삽입
    visited[si][sj] = 1 # 방문 처리
    count = 1
    
    while q:
        ci, cj = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + dx, cj + dy
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]==0 and arr[ni][nj]==1:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return count
    
T = int(input()) # 테스트 케이스
for _ in range(T):
    # 2차원 배열 생성
    M, N, K = map(int, input().split()) # 가로 길이, 세로 길이, 배추 개수
    arr = [[0] * M for _ in range(N)] # 배추밭
    visited = [[0] * M for _ in range(N)] # 방문 표시 배열
    answer = []
    
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                answer.append(bfs(i, j))
    print(sum(answer))
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
            # 인접 ni, nj가 지도의 범위 내에 있고 방문하지 않았고 집이라면
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and map_arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                count += 1
    return count
        

N = int(input()) # 지도의 크기 N x N
map_arr = [list(map(int, input().rstrip())) for _ in range(N)] # 지도 생성
visited = [[0] * N for _ in range(N)] # 방문 표시 배열
answer = []

for i in range(N):
    for j in range(N):
        if map_arr[i][j] == 1 and visited[i][j] == 0: # i행 j열에 집이 있고, 방문하지 않은 상태이면
            answer.append(bfs(i, j)) # bfs 호출 후 단지 개수 return
            
answer.sort()
print(len(answer), *answer, sep='\n')
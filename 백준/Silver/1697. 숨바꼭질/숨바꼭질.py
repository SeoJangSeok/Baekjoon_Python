from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split()) # 수빈의 위치, 동생의 위치
MAX = 10 ** 5 # 0 <= N, K <= 100,000
visited = [0] * (MAX + 1)

def bfs(si):
    q = deque()
    q.append(si) # 시작 위치 삽입
    while q:
        ci = q.popleft() # 현재 위치
        if ci == K: # 목표한 위치이면
            return visited[K]
        for ni in (ci+1, ci-1, ci*2):
            if 0 <= ni <= MAX and visited[ni]==0: # 탐색할 다음 위치가 범위 내이고 방문하지 않은 위치일 경우
                visited[ni] = visited[ci] + 1
                q.append(ni)

print(bfs(N))
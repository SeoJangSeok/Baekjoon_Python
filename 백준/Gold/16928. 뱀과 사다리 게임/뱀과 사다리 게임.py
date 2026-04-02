from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while queue:
        current = queue.popleft()
        if current == 100:
            return board[current] - 1
        
        for i in range(1, 7):
            next_pos = current + i
            if next_pos <= 100 and board[next_pos] == 0:
                if next_pos in ladder:
                    next_pos = ladder[next_pos]
                if next_pos in snake:
                    next_pos = snake[next_pos]
                if board[next_pos] == 0:
                    board[next_pos] = board[current] + 1
                    queue.append(next_pos)
                
N, M = map(int, input().split()) # 사다리 수, 뱀의 수
board = [0] * 101 # 게임 보드 초기화
board[1] = 1 # 시작 위치

ladder = {}
snake = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

queue = deque([1])

print(bfs())
from collections import deque
import sys

input = sys.stdin.readline

def bfs(si, sj):
    dx = [1, -1, 2, -2, 1, -1, 2, -2] # row
    dy = [2, 2, 1, 1, -2, -2, -1, -1] # col
    
    q = deque()
    q.append((si, sj))
    while q:
        ci, cj = q.popleft()
        if ci==di and cj==dj: # 현재 위치가 목표 위치일 경우
            return chess_board[ci][cj]
        for i in range(8):
            ni = ci + dx[i]
            nj = cj + dy[i]
            if 0<=ni<l and 0<=nj<l and chess_board[ni][nj]==0:
                chess_board[ni][nj] = chess_board[ci][cj] + 1
                q.append((ni, nj))

T = int(input()) # Test_case


for _ in range(T):
    l = int(input()) # 체스판의 한 변의 길이
    chess_board = [[0]*l for _ in range(l)] # l x l 크기의 chess판
    si, sj = map(int, input().split()) # 현재 위치 
    di, dj = map(int, input().split()) # 목표 위치
    print(bfs(si, sj))
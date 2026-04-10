import sys
input = sys.stdin.readline

SIZE = 9

sudoku = [list(map(int, input().split())) for _ in range(SIZE)]

# 빈칸의 좌표 리스트
empty = [(i, j) for i in range(SIZE) for j in range(SIZE) if sudoku[i][j] == 0]

def check(y, x, check_num):
    BOX_SIZE = 3
    
    for i in range(SIZE): # 가로, 세로 체크
        if sudoku[y][i] == check_num or sudoku[i][x] == check_num:
            return False
    
    for i in range(BOX_SIZE): # 3x3영역 체크
        for j in range(BOX_SIZE):
            if sudoku[y // BOX_SIZE * BOX_SIZE + i][x // BOX_SIZE * BOX_SIZE + j] == check_num:
                return False
    return True

def dfs(n):
    if n == len(empty):
        for i in sudoku: 
            print(*i) 
        exit() 
    
    for check_num in range(1,10):
        y, x = empty[n]
        # y = empty[n][0]
        # x = empty[n][1]
        if check(y, x, check_num):
            sudoku[y][x] = check_num
            dfs(n+1)
            sudoku[y][x] = 0
            
dfs(0)
import sys
input = sys.stdin.readline


N = int(input())

visited = [-1] * N
count = 0

def dfs(row):
    global count
    
    if row == N:
        count += 1
    else:
        for col in range(N):
            visited[row] = col
            if check(row):
                dfs(row + 1)

def check(current_row):
    for row in range(current_row):
        if visited[current_row] == visited[row] or current_row - row == abs(visited[current_row] - visited[row]):
            return False
    return True

dfs(0)
print(count)
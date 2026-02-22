import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]

def cut(x, y, n):
    paper = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper != arr[i][j]:
                cut(x, y, n//3)
                cut(x, y+n//3, n//3)
                cut(x, y+2*n//3, n//3)
                cut(x+n//3, y, n//3)
                cut(x+n//3, y+n//3, n//3)
                cut(x+n//3, y+2*n//3, n//3)
                cut(x+2*n//3, y, n//3)
                cut(x+2*n//3, y+n//3, n//3)
                cut(x+2*n//3, y+2*n//3, n//3)
                return
    answer[paper] += 1

cut(0, 0, N)
print(answer[-1])
print(answer[0])
print(answer[1])
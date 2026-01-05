import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    D = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for j in range(1, m+1):
        D[1][j] = j
        D[0][j] = 1
        
    for i in range(2, n+1):
        for j in range(i, m+1):
            D[i][j] = D[i-1][j-1] + D[i][j-1]

    print(D[n][m])
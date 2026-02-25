N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)] # N x M

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)] # M x K

AB = [[0] * K for _ in range(N)] # N x K

for i in range(N):
    for j in range(K):
        for k in range(M):
            AB[i][j] += A[i][k] * B[k][j]

for i in AB:
    for j in i:
        print(j, end=' ')
    print()
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def mul(a, b):
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                arr[i][j] += (a[i][k] * b[k][j])
            arr[i][j] %= 1000
    return arr

def square(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] = A[i][j] % 1000
        return A
    tmp = square(A, B//2)
    if B % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), A)

result = square(A, B)

for r in result:
    print(*r)
n = int(input())

A = list(map(int, input().split()))

inc = [1] * n
dec = [1] * n

for i in range(n):
    for j in range(i):
        if A[j] < A[i]: # 1 < 4
            inc[i] = max(inc[i], inc[j] + 1)

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if A[j] < A[i]:
            dec[i] = max(dec[i], dec[j] + 1)

answer = 0
for i in range(n):
    answer = max(answer, inc[i] + dec[i] - 1)

print(answer)
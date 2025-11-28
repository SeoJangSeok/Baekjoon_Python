N = int(input())
answer = 0

for M in range(1, N):
    m = list(map(int, str(M)))
    if M + sum(m) == N:
        answer = M
        break
print(answer)
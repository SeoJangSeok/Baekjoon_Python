n = int(input())

wire = [list(map(int, input().split())) for _ in range(n)]
wire.sort()

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if wire[j][1] < wire[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
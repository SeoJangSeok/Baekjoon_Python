N = int(input()) # 집의 수
cost = [list(map(int, input().split())) for _ in range(N)] # 각 집을 칠하는 비용

# R G B
# 0 0 0
# . . .
dp = [[0] * 3 for _ in range(N)]
dp[0] = cost[0] # 첫 집의 비용 초기화

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N-1]))
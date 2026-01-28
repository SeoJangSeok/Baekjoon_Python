n = int(input()) # 계단의 개수

stair = [int(input()) for _ in range(n)]

dp = [0] * n

if len(stair) <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0] # 첫 번째 계단 최대 점수
    dp[1] = dp[0] + stair[1] # 두 번째 계단 최대 점수
    for i in range(2, n):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])
    print(dp[-1])
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for w, v in items:
    for k in range(K, w-1, -1):
        dp[k] = max(dp[k], dp[k-w]+v)
print(dp[K])
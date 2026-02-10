import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))
prefix_sum = [0]
range_sum = []
tmp = 0

# 누적합
for i in range(N):
    tmp += temp[i]
    prefix_sum.append(tmp)
    
# 구간합
for i in range(N-K+1):
    range_sum.append(prefix_sum[i+K] - prefix_sum[i])

print(max(range_sum))
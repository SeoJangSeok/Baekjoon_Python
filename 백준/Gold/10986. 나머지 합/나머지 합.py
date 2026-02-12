import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

prefix_sum = 0
cnt = [0] * M
cnt[0] = 1

answer = 0

for i in A:
    prefix_sum = (prefix_sum + i) % M
    answer += cnt[prefix_sum]
    cnt[prefix_sum] += 1
    
print(answer)
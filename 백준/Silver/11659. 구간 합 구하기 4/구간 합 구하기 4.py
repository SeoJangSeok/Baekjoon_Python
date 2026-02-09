import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 수의 개수, M: 합을 구하는 횟수
A = list(map(int, input().split()))

prefix_sum = [0]
tmp = 0

for i in A:
    tmp += i
    prefix_sum.append(tmp)
# print(prefix_sum)
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
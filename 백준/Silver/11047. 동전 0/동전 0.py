import sys
input = sys.stdin.readline

N, K = map(int, input().split())
count = 0

arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

for i in arr:
    if i <= K:
        count += (K // i)
        K %= i
print(count)
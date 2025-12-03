import sys

n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]
for num in sorted(nums):
    print(num)
n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))
nums.sort()
for n in nums:
    print(n)
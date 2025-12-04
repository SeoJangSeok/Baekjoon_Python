nums = list(map(int, input()))

for n in sorted(nums, reverse=True):
    print(n, end='')
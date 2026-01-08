import sys
input = sys.stdin.readline

n = int(input())

numbers = dict()
arr = []
total = 0

for _ in range(n):
    num = int(input())
    arr.append(num)
    total += num
    numbers[num] = numbers.get(num, 0) + 1

arr.sort()

print(round(total / n))
print(arr[n // 2])

most_freq = max(numbers.values())
most_nums = [k for k, v in numbers.items() if v == most_freq]
most_nums.sort()
print(most_nums[1] if len(most_nums) > 1 else most_nums[0])

print(max(numbers.keys()) - min(numbers.keys()))
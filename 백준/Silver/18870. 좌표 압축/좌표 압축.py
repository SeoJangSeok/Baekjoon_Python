import sys

input = sys.stdin.readline

n = int(input())

points = list(map(int, input().split()))
filtered_arr = sorted(set(points))
dic = {filtered_arr[i]: i for i in range(len(filtered_arr))}

for num in points:
    print(dic[num], end=' ')
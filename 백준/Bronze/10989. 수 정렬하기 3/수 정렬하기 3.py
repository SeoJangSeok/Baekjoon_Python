import sys

input = sys.stdin.readline

# N개의 수
N = int(input())

# count 배열
count = [0] * 10001

for _ in range(N):
    num = int(input())
    count[num] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
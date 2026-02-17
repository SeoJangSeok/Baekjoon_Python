import sys
input = sys.stdin.readline

N = int(input())
P = sorted(map(int, input().split()))

time = 0
total = 0

for i in P:
    time += i
    total += time
print(total)    
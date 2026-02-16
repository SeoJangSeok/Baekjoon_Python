import sys
input = sys.stdin.readline

N = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x: (x[1], x[0]))

e = count = 0

for start, end in time:
    if e <= start:
        e = end
        count += 1

print(count)
import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]
points.sort(key=lambda x: (x[0], x[1]))

for x, y in points:
    print(x, y)
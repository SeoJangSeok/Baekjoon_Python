import sys
input = sys.stdin.readline

city = int(input())
km = list(map(int, input().split()))
cost = list(map(int, input().split()))

cost.pop()
min_cost = min(cost)
total_cost = 0

for i, c in enumerate(cost):
    if c == min_cost:
        total_cost += sum(km[i:]) * c
        break
    else:
        total_cost += km[i] * c
print(total_cost)
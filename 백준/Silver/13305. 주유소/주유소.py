import sys
input = sys.stdin.readline

city = int(input())
km = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
total_cost = 0

for i in range(city - 1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    total_cost += min_cost * km[i]
    
print(total_cost)
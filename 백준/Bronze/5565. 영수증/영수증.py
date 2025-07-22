total_cost = int(input())
readable_cost = 0
for i in range(9):
    readable_cost += int(input())

print(total_cost - readable_cost)
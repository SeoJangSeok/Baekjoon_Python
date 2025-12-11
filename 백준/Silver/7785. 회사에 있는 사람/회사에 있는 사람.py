n = int(input())
employees = {}

for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        employees[name] = log
    else:
        del employees[name]
for name in sorted(employees.keys(), reverse=True):
    print(name)
    
import sys

T = int(input())

for i in range(T):
    l = list(sys.stdin.readline().split())
    sum = 0
    for j in range(len(l)):
        if j == 0:
            l[j] = float(l[j])
            sum += l[j]
        elif l[j] == '@':
            sum *= 3
        elif l[j] == '%':
            sum += 5
        elif l[j] == '#':
            sum -= 7
    print(f'{sum:.2f}')
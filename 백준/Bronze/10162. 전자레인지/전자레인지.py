t = int(input())
a, b, c = 300, 60, 10
result = []

if t % 10 != 0:
    print(-1)
else:
    result.append(t // a)
    result.append((t % a) // b)
    result.append((t % b) // c)
    print(*result, sep=' ')
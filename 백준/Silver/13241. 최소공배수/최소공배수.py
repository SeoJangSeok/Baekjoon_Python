a, b = map(int, input().split())
ab = a * b

while b != 0:
    a, b = b, a % b

print(ab // a)
serial = list(map(int, input().split()))

for i, n in enumerate(serial):
    serial[i] = n ** 2

print(sum(serial) % 10)
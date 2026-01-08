import sys
input = sys.stdin.readline

n = int(input())
dancer = {'ChongChong'}

for _ in range(n):
    a, b = input().split()
    if a in dancer and b not in dancer:
        dancer.add(b)
    elif b in dancer and a not in dancer:
        dancer.add(a)

print(len(dancer))
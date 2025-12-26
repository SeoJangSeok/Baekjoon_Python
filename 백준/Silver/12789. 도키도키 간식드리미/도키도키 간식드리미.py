n = int(input())
line = list(map(int, input().split()))

stack = []
need = 1

for x in line:
    while stack and stack[-1] == need:
        stack.pop()
        need += 1

    if x == need:
        need += 1
    else:
        stack.append(x)

while stack and stack[-1] == need:
    stack.pop()
    need += 1

print("Nice" if need == n + 1 else "Sad")

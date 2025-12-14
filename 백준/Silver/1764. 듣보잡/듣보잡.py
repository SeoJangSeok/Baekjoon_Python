n, m = map(int, input().split())

not_heard = set()
not_saw = set()

for _ in range(n):
    not_heard.add(input())

for _ in range(m):
    not_saw.add(input())

not_heard_saw = sorted(list(not_heard & not_saw))
print(len(not_heard_saw))

for i in not_heard_saw:
    print(i)
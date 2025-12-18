def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
trees = [int(input()) for _ in range(n)]

dis = []
for i in range(len(trees) - 1):
    dis.append(trees[i + 1] - trees[i])

g = dis[0]
for d in dis[1:]:
    g = gcd(g, d)

answer = 0
for d in dis:
    answer += d // g - 1

print(answer)
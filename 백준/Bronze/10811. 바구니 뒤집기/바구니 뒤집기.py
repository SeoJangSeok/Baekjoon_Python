N, M = map(int, input().split())
baskets = [x+1 for x in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    temp = baskets[i-1:j]
    temp.reverse()
    baskets[i-1:j] = temp
print(*baskets)
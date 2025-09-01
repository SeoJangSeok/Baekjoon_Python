N = int(input())
answer = list(map(int, input().split()))
score = 0
bonus = 0
for i in range(N):
    if answer[i] == 1:
        bonus += 1
        score += bonus
    else:
        bonus = 0
print(score)

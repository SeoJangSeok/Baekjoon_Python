n = int(input())
score = list(map(int, input().split()))
temp = []
max_score = max(score)
for i in score:
    temp.append(i / max_score*100)
print(sum(temp) / len(temp))
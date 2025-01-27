N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    checker = []
    group_word = True
    for i in word:
        if i not in checker:
            checker.append(i)
        elif i == checker[-1]:
            continue
        else:
            group_word = False
            break
    if group_word:
        cnt += 1
print(cnt)
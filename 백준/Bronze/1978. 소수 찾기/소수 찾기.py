n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for i in nums:
    if i == 1:  # 1은 소수가 아님
        continue

    for j in range(2, i):
        if i % j == 0:
            break
    else:
        cnt += 1
print(cnt)
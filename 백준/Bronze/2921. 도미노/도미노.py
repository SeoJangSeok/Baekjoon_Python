set_size = int(input())
sum = 0

for i in range(set_size + 1):
    for j in range(set_size + 1):
        if i > j:
            continue
        sum += i + j
print(sum)
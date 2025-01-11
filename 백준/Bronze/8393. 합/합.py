n = int(input())
num = []
for i in range(1, n+1):
    num.append(i)
print((num[0] + num[-1]) * len(num)//2)
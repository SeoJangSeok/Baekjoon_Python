N, B = input().split() # 수, 진법
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = N[::-1]
result = 0

for i in range(len(N)):
    result += (int(B)**i) * (num.index(N[i]))
print(result)
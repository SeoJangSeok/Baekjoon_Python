N, B = map(int, input().split()) # 수, 진법
s = ''
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while N:
    s += num[N%B]
    N //= B
print(s[::-1])
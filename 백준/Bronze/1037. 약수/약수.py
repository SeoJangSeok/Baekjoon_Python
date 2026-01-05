n = int(input())

divisor = list(map(int, input().split()))
divisor.sort()

if len(divisor) % 2 == 0:
    print(divisor[0] * divisor[-1])
else:
    mid = len(divisor) // 2
    print(divisor[mid] ** 2)
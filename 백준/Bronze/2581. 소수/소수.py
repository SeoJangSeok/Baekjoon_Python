M = int(input())
N = int(input())
prime_num = []

for num in range(M, N + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_num.append(num)

if not prime_num:
    print(-1)
else:
    print(sum(prime_num))
    print(min(prime_num))
import sys
input = sys.stdin.readline

MAX = 1000000

is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False
            
primes = [i for i in range(2, MAX + 1) if is_prime[i]]

T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 0
    
    half = n // 2
    for p in primes:
        if p > half:
            break
        if is_prime[n - p]:
            cnt += 1
    print(cnt)
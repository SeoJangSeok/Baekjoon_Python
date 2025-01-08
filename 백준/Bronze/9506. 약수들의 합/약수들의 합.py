while True:
    n = int(input())
    if n == -1:
        break
    divisors = []
    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and n // i != n:
                divisors.append(n // i)
        divisors.sort()
    if sum(divisors) == n:
        print(f'{n} =', end=' ')
        print(*divisors, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')
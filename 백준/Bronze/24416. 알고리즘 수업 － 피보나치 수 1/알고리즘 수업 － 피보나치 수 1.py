def fib(n):
    f[1] = 1
    f[2] = 1

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]

def fibonacci(n):
    return n - 2

n = int(input())

f = [0] * (n + 1)

print(fib(n))
print(fibonacci(n))
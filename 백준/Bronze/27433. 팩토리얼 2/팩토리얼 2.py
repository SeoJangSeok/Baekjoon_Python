n = int(input())

def factorial(n):
    while n >= 0:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
print(factorial(n))
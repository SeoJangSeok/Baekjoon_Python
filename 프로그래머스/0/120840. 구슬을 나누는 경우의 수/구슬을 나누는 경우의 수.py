def solution(balls, share):
    return factorial(balls) // (factorial(balls - share) * factorial(share))

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
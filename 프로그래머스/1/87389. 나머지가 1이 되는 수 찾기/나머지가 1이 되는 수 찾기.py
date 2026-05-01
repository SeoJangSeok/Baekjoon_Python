def solution(n):
    x = n - 1
    
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return i
    return x
def solution(n):
    i = 1
    m = 1
    while i <= n:
        m += 1
        i *= m
    return m - 1
    
    
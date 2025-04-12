def solution(n):
    if n < 8:
        return 1
    elif n % 7 == 0:
        return n // 7
    else:
        return n // 7 + 1
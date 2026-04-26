def solution(n):
    n = sorted(str(n), reverse=True)
    return int(''.join(n))
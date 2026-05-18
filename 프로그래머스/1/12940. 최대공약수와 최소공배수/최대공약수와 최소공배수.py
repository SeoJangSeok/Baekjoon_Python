def solution(n, m):
    answer = []
    a, b = max(n, m), min(n, m)
    
    while b > 0:
        a, b = b, a % b
    gcd = a
    lcm = (n * m) // gcd
    
    answer.append(gcd)
    answer.append(lcm)
    
    return answer
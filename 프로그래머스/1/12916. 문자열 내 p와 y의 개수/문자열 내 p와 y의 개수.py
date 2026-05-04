def solution(s):
    total_p, total_y = 0, 0
    total_p += s.count('p')
    total_p += s.count('P')
    total_y += s.count('y')
    total_y += s.count('Y')
    if total_p == total_y:
        return True
    return False
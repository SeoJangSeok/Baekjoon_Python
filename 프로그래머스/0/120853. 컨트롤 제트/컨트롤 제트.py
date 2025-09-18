def solution(s):
    s = list(s.split())
    # Z가 없는 경우
    if 'Z' not in s:
        return sum(map(int, s))
    # Z가 있는 경우
    for i, ch in enumerate(s):
        if ch == 'Z':
            s[i] = -int(s[i-1])
    return sum(map(int, s))
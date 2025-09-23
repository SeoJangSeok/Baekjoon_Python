def solution(s):
    answer = []
    for ch in set(s):
        if s.count(ch) == 1:
            answer.append(ch)
    answer.sort()
    return ''.join(answer)

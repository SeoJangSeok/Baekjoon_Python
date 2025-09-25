def solution(num, k):
    for i, n in enumerate(str(num)):
        if int(n) == k:
            return i + 1
    return -1
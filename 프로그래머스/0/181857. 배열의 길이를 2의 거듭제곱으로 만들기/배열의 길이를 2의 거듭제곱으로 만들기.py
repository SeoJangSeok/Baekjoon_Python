def solution(arr):
    i = 1
    while i < len(arr):
        i *= 2
    return arr + [0] * (i - len(arr))
        
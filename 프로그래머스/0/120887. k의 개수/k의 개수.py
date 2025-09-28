def solution(i, j, k):
    return ''.join(str(x) for x in range(i, j+1)).count(str(k))
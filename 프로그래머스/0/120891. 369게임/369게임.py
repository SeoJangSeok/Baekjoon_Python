def solution(order):
    cnt = 0
    cnt += str(order).count('3')
    cnt += str(order).count('6')
    cnt += str(order).count('9')
    return cnt
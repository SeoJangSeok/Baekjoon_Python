def solution(a, b):
    answer = 0
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    
    if ab > ba:
        answer = ab
    elif ab < ba:
        answer = ba
    else:
        answer = ab
    
    return answer
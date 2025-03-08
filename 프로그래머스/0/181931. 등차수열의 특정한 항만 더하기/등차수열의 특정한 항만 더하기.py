def solution(a, d, included):
    answer = 0
    for i, boolean in enumerate(included):
        if boolean == True:
            answer += a + (i * d)
        
    return answer
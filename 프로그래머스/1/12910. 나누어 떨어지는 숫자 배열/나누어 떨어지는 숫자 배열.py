def solution(arr, divisor):
    answer = []
    
    for n in arr:
        if n % divisor == 0:
            answer.append(n)
    
    if not answer:
        return [-1]
    
    answer.sort()
    
    return answer
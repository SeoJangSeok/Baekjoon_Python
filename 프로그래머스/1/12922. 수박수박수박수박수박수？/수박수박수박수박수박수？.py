def solution(n):
    answer = '수박'
    answer *= ((n+1) // 2)
    return answer[0:n]
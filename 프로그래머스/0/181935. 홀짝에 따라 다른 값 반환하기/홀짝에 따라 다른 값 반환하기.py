def solution(n):
    answer = 0
    # 홀수의 경우
    if n % 2 != 0:
        for i in range(1, n+1, 2):
            answer += i
    else: # 짝수의 경우
        for i in range(2, n+1, 2):
            answer += i**2
    return answer
# 1, 4, 9, 16 등 제곱수의 약수 개수는 홀수이며, 나머지 수는 짝수
def solution(left, right):
    answer = 0
    
    for n in range(left, right+1):
        if int(n**0.5)**2 == n:
            answer -= n
        else:
            answer += n
    return answer
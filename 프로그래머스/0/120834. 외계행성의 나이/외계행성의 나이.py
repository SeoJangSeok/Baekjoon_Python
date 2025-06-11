def solution(age):
    answer = ''
    for i in str(age):
        answer += chr(97 + int(i))
    return answer
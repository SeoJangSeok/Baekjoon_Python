def solution(my_string):
    answer = ''
    for ch in my_string:
        if ch not in answer:
            answer += ch
    return answer
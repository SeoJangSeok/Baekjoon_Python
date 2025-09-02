def solution(rsp):
    answer = ''
    for i, c in enumerate(rsp):
        if c == '2':
            answer += '0'
        elif c == '0':
            answer += '5'
        elif c == '5':
            answer += '2'
    return answer
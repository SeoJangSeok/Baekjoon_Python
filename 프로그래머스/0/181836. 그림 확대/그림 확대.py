def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        answer += [picture[i].replace('x', 'x' * k).replace('.', '.' * k)] * k
    return answer
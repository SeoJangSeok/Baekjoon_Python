def solution(strArr):
    len_list = [len(i) for i in strArr]
    answer = []
    for i in set(len_list):
        answer.append(len_list.count(i))
    return max(answer)
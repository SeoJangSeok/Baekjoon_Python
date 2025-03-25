def solution(my_string):
    answer = [0] * 52
    for alphabet in set(my_string):
        idx = ord(alphabet) - 65
        if idx <= 25:
            answer[idx] = my_string.count(alphabet)
        else:
            answer[idx - 6] = my_string.count(alphabet)
    return answer
def solution(my_strings, parts):
    return ''.join(string[s : e+1] for string, (s, e) in zip(my_strings, parts))
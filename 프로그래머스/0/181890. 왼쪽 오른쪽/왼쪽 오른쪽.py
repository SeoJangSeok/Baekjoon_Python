def solution(str_list):
    for i in str_list:
        if i == 'l':
            return str_list[:str_list.index('l')]
        elif i == 'r':
            return str_list[str_list.index('r')+1:]
    return []
def solution(my_string, is_suffix):
    suffix = []
    for i in range(len(my_string)):
        suffix.append(my_string[i:])
    if is_suffix in suffix:
        return 1
    else:
        return 0
def solution(my_string):
    return ''.join(ch for ch in my_string if ch not in 'aeiou')
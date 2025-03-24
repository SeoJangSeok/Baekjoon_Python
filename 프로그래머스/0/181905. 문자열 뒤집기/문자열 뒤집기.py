def solution(my_string, s, e):
    if s == 0:
        return my_string[s : e+1][::-1] + my_string[e + 1:]
    return my_string[:s] + my_string[s : e+1][::-1] + my_string[e + 1:] if s != e else my_string
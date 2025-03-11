def solution(n, control):
    w_count = control.count('w')
    s_count = control.count('s')
    d_count = control.count('d')
    a_count = control.count('a')
    n += 1*w_count -1*s_count + 10*d_count -10*a_count
    return n
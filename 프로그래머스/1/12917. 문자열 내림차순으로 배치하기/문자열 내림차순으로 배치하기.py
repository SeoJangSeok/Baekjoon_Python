def solution(s):
    small = ''
    big = ''
    for i in s:
        if ord(i) < 65:
            small += i
        else:
            big += i
    small = sorted(small, reverse=True)
    big = sorted(big, reverse=True)
    
    return ''.join(small + big)
def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] == '1':
                mode = int(not(mode))
            else:
                if i % 2 == 0:
                    ret += code[i]
        else:
            if code[i] == '1':
                mode = int(not(mode))
            else:
                if i % 2 != 0:
                    ret += code[i]
    if ret == '':
        return 'EMPTY'
    return ret
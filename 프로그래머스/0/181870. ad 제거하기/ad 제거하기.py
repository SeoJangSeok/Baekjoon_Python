def solution(strArr):
    for i in strArr[:]:
        if 'ad' in i:
            strArr.remove(i)
    return strArr
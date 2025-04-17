def solution(myString):
    splited_list = myString.split('x')
    return list(len(i) for i in splited_list)
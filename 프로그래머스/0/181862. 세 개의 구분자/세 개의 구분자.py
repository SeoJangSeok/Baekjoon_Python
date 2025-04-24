def solution(myStr):
    for i in range(3):
        myStr = myStr.replace(chr(97 + i), ' ')
    return myStr.split() if myStr.split() else ['EMPTY']
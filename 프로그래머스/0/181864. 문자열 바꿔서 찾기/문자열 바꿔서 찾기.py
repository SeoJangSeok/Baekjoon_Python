def solution(myString, pat):
    pat = pat.replace('A', 't').replace('B', 'A').replace('t', 'B')
    return 1 if pat in myString else 0
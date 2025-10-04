def solution(spell, dic):
    for char in dic:
        print(char)
        if sorted(spell) == sorted(char):
            return 1
    return 2
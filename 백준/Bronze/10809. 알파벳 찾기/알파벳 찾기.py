S = input()
alp = 'abcdefghijklmnopqrstuvwxyz'

for i in alp:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')
t = int(input()) # test_case

for i in range(t):
    r, e, c = map(int, input().split())
    if r == e - c:
        print('does not matter')
    elif r < e - c:
        print('advertise')
    else:
        print('do not advertise')
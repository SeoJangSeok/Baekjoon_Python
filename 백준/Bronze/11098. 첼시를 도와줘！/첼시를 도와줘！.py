n = int(input())
for i in range(n):
    p = int(input())
    max_c = 0
    max_name = ''
    for i in range(p):
        c, name = input().split()
        if (int(c) > max_c):
            max_c = int(c)
            max_name = name
    print(max_name)
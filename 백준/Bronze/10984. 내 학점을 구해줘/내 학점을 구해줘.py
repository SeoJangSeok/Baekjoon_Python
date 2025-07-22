for term in range(int(input())):
    C, G = 0, 0
    for subject_count in range(int(input())):
        c_tmp, g_tmp = map(float, input().split())
        C += c_tmp
        G += g_tmp * c_tmp
    print(int(C), format(G / C, '.1f'))
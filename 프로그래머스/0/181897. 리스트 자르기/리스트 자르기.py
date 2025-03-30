def solution(n, slicer, num_list):
    a, b, c = slicer
    if n == 1:
        return list(num_list[:b+1])
    elif n == 2:
        return list(num_list[a : ])
    elif n == 3:
        return list(num_list[a : b+1])
    else:
        return list(num_list[a : b+1 : c])

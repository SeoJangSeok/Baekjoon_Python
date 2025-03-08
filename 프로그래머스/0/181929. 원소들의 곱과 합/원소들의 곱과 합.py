def solution(num_list):
    a = 1
    for i in range(len(num_list)):
        if num_list[i] == 0:
            a = 0
        else:
            a *= num_list[i]
    b = sum(num_list) ** 2
    
    if a < b:
        return 1
    else:
        return 0
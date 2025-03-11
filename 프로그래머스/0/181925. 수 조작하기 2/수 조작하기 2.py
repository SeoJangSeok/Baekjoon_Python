def solution(numLog):
    num_dict = {1:'w', -1:'s', 10:'d', -10:'a'}
    control = ''
    for i in range(len(numLog) - 1):
        n = numLog[i+1] - numLog[i]
        control += num_dict[n]
    return control
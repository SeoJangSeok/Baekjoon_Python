def solution(arr):
    i = 0
    stk = []
    for i in range(len(arr)):
        if stk == []:
            stk.append(arr[i])
        elif stk and stk[-1] == arr[i]:
            del stk[-1]
        elif stk and stk[-1] != arr[i]:
            stk.append(arr[i])
        i += 1
    return stk if stk else [-1]
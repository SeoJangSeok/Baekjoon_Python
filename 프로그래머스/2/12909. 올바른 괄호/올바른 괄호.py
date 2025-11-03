def solution(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []
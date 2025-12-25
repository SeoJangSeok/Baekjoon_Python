while True:
    string = input()
    stack = []
    
    if string == '.':
        break
    flag = True
    
    for c in string:
        
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
            
    if flag and not stack:
        print('yes')
    else:
        print('no')
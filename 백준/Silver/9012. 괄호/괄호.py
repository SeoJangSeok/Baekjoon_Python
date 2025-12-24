T = int(input())

for _ in range(T):
    vps_stack = []
    ps = input().strip()
    is_valid = True
    
    for i in ps:
        if i == '(':
            vps_stack.append(i)
        else:
            if vps_stack:
                vps_stack.pop()
            else:
                is_valid = False
                break
    if is_valid and not vps_stack:
        print('YES')
    else:
        print('NO')
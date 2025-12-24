T = int(input())

for _ in range(T):
    vps_stack = []
    ps = input().strip()
    
    for i in ps:
        if i == '(':
            vps_stack.append(i)
        else:
            if vps_stack:
                vps_stack.pop()
            else:
                print('NO')
                break
    else:
        if not vps_stack:
            print('YES')
        else:
            print('NO')
import sys

def stack_cmd():
    input = sys.stdin.readline
    n = int(input())
    stack = []
    
    for _ in range(n):
        cmd = input().split()
        
        if cmd[0] == '1':
            stack.append(int(cmd[1]))
        elif cmd[0] == '2':
            print(stack.pop() if stack else -1)
        elif cmd[0] == '3':
            print(len(stack))
        elif cmd[0] == '4':
            print(0 if stack else 1)
        else:  # '5'
            print(stack[-1] if stack else -1)

stack_cmd()
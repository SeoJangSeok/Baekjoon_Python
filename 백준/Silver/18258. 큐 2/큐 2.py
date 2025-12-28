import sys
input = sys.stdin.readline

n = int(input())
queue = []
head = 0

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if head == len(queue):
            print(-1)
        else:
            print(queue[head])
            head += 1
    elif cmd[0] == 'size':
        print(len(queue) - head)
    elif cmd[0] == 'empty':
        print(1 if head == len(queue) else 0)
    elif cmd[0] == 'front':
        print(-1 if head == len(queue) else queue[head])
    elif cmd[0] == 'back':
        print(-1 if head == len(queue) else queue[-1])

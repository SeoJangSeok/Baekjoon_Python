import sys
from collections import deque
input = sys.stdin.readline

def deque_cmd():
    n = int(input())
    deq = deque()
    
    for _ in range(n):
        cmd= list(map(int, input().split()))
        if cmd[0] == 1:
            deq.appendleft(cmd[1])
        elif cmd[0] == 2:
            deq.append(cmd[1])
        elif cmd[0] == 3:
            print(deq.popleft() if deq else -1)
        elif cmd[0] == 4:
            print(deq.pop() if deq else -1)
        elif cmd[0] == 5:
            print(len(deq))
        elif cmd[0] == 6:
            print(1 if not deq else 0)
        elif cmd[0] == 7:
            print(deq[0] if deq else -1)
        elif cmd[0] == 8:
            print(deq[-1] if deq else -1)

deque_cmd()
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deq = deque(enumerate(map(int, input().split())))
answer = []

while deq:
    idx, paper = deq.popleft()
    answer.append(idx + 1)
    if paper > 0:
        deq.rotate(-(paper - 1))
    elif paper < 0:
        deq.rotate(-paper)

print(' '.join(map(str, answer)))
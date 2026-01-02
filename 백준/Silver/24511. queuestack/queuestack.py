from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

q = deque(B[i] for i in range(N) if A[i] == 0)

for c in C:
    q.appendleft(c)
    print(q.pop(), end=' ')
import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for case in range(T):
    a, b = map(int, input().split())
    print(a + b)
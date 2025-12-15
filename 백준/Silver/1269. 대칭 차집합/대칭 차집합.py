n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_minus = A - B
B_minus = B - A
A_B = A_minus | B_minus
print(len(A_B))
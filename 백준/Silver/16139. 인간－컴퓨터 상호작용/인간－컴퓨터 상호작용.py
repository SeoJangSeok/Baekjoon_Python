import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

prefix_sum = [[0] * 26]

for i in range(len(S)):
    prefix_sum.append(prefix_sum[len(prefix_sum)-1][:])
    prefix_sum[i+1][ord(S[i]) - 97] += 1

for i in range(q):
    A, l, r = input().split()
    l, r = int(l), int(r)
    result = prefix_sum[r+1][ord(A)-97] - prefix_sum[l][ord(A)-97]
    print(result)
import sys
input = sys.stdin.readline

multitap = int(input())
total_plug = 0

for n in range(multitap):
    n_plug = int(input())
    total_plug += n_plug

print(total_plug - multitap + 1)
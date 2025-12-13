import sys
input = sys.stdin.readline

n = int(input())
cards_list = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))
cards_dict = {}

for n in cards_list:
    if n not in cards_dict:
        cards_dict[n] = 1
    else:
        cards_dict[n] += 1

for n in check_list:
    if n not in cards_dict:
        print(0, end=' ')
    else:
        print(cards_dict[n])

import sys
input = sys.stdin.readline

card_dict = {}

n = int(input())
card_list = list(map(int, input().split()))

for num in card_list:
    card_dict[num] = 1

m = int(input())
check_list = list(map(int, input().split()))

for num in check_list:
    if num in card_dict :
        print(1, end=' ')
    else:
        print(0, end=' ')
test_case = int(input())

for case in range(test_case):
    n_num = int(input())
    n_list = list(map(int, input().split()))
    print(sum(n_list))
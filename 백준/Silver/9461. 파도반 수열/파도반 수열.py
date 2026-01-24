p_list = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

test_case = int(input())

for i in range(10, 100):
    p_list.append(p_list[i-2] + p_list[i-3])

for _ in range(test_case):
    n = int(input())
    print(p_list[n-1])
test_case = int(input())
for case in range(test_case):
    s = int(input()) # 자동차 가격
    n = int(input()) # 옵션의 개수
    if n == 0:
        print(s)
        continue
    for i in range(n):
        q, p = map(int, input().split())
        s += q * p
    print(s)
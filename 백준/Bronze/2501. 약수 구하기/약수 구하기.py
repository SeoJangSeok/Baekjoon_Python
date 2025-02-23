n, k = map(int, input().split())
q = 1
n_list = []

# 약수 구하기
while n >= q:
    if n % q == 0:
        n_list.append(q)
    q += 1
n_list.sort()
try:
    print(n_list[k - 1])
except IndexError:
    print(0)
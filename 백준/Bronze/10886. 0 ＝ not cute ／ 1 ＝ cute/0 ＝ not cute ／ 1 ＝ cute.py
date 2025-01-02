N = int(input())
cute, n_cute = 0, 0

for i in range(N):
    vote = int(input())
    if vote == 1:
        cute += 1
    else:
        n_cute += 1

if cute > n_cute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
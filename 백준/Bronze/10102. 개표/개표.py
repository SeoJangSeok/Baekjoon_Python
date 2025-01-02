V = int(input())
vote = input()
v_A, v_B = 0, 0

for i in range(V):
    if vote[i] == 'A':
        v_A += 1
    else:
        v_B += 1

if v_A > v_B:
    print('A')
elif v_B > v_A:
    print('B')
else:
    print('Tie')    
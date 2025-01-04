n = int(input())
q_dict = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0, 'AXIS': 0}

for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        q_dict['Q1'] += 1
    elif x > 0 and y < 0:
        q_dict['Q4'] += 1
    elif x < 0 and y > 0:
        q_dict['Q2'] += 1
    elif x < 0 and y < 0:
        q_dict['Q3'] += 1
    else:
        q_dict['AXIS'] += 1
for key, value in q_dict.items():
    print(f'{key}: {value}')
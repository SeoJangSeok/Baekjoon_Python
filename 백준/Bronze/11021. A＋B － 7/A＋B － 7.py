test_case = int(input())
case = []

for i in range(test_case):
    a, b = map(int, input().split())
    case.append(a + b)
    
for i in range(test_case):
    print(f'Case #{i+1}: {case[i]}')
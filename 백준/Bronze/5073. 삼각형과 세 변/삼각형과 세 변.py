while True:
    triangle = list(map(int, input().split()))
    if sum(triangle) == 0:
        break
    
    if max(triangle) >= sum(triangle) - max(triangle):
        print('Invalid')
    elif len(set(triangle)) == 1:
        print('Equilateral')
    elif len(set(triangle)) == 2:
        print('Isosceles')
    else:
        print('Scalene')
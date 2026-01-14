def cantor_set(n):
    if n == 1:
        return '-'
    
    left = cantor_set(n // 3)
    center = ' ' * (n // 3)
    return left + center + left
    
while True:
    try:
        N = int(input())
        print(cantor_set(3 ** N))
    except EOFError:
        break
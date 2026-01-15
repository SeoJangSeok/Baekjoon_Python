def star_recursion(n):
    if n == 1:
        return ['*']
    
    Stars = star_recursion(n // 3) 
    star = []
    
    for S in Stars:
        star.append(S * 3)
    for S in Stars:
        star.append(S + ' ' * (n // 3) + S)
    for S in Stars:
        star.append(S * 3)
    
    return star

n = int(input())
print('\n'.join(star_recursion(n)))
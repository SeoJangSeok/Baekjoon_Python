def DAC(a, b, c):
    if b == 1:
        return a % c
    
    temp = DAC(a, b//2, c)
    
    if b % 2 == 0:
        return (temp * temp) % c
    else:
        return ((temp * temp) % c) * a % c
    
A, B, C = map(int, input().split())

print(DAC(A, B, C))
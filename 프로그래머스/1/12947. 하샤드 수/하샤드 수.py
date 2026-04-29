def solution(x):
    divisor = 0
    x_temp = x
    
    while x_temp > 0:
        divisor += (x_temp % 10)
        x_temp //= 10
        
    if x % divisor:
        return False
    else:
        return True
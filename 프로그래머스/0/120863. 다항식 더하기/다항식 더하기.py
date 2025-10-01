def solution(polynomial):
    poliynomial_splited = polynomial.replace(' ', '').split('+')
    
    x계수 = 0
    상수항 = 0
    for i in poliynomial_splited:
        if 'x' in i:
            if i == 'x':
                x계수 += 1
            else:
                x계수 += int(i[:-1])
        else:
            상수항 += int(i)
    if x계수 == 0:
        return str(상수항)
    if 상수항 == 0:
        if x계수 == 1:
            return 'x'
        else:
            return f'{x계수}x'
    if x계수 == 1:
        return f'x + {상수항}'
    return f'{x계수}x + {상수항}'
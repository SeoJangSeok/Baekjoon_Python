import math

def solution(signals):
    # 각 신호등의 주기
    cycles = []
    for signal in signals:
        cycles.append(sum(signal))
    
    # 각 신호등의 주기가 반복되는 최소공배수 구하기
    lcm = 1
    for cycle in cycles:
        lcm = lcm * cycle // math.gcd(lcm, cycle)
        
    for t in range(1, lcm+1):
        yellow = True
        
        for g, y, r in signals:
            cycle = g + y + r
            pos = (t - 1) % cycle + 1
            
            # 현재 시각이 노란불 구간이 아니라면 종료
            if not (g+1 <= pos <= g+y):
                yellow = False
                break
        if yellow:
            return t
    return -1
def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {}
    
    for num in dice:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    if len(counts) == 1:
        # 모든 주사위가 같은 경우
        p = list(counts.keys())[0]
        return 1111 * p
    elif len(counts) == 2:
        # p와 q로 나누어지는 경우
        key = list(counts.keys())
        if counts[key[0]] == 3 or counts[key[1]] == 3:
            # 세 주사위가 같은 경우
            p = key[0] if counts[key[0]] == 3 else key[1]
            q = key[1] if counts[key[0]] == 3 else key [0]
            return (10 * p + q) ** 2
        else:
            # 두 개씩 같은 주사위인 경우
            p, q = key[0], key[1]
            return (p + q) * abs(p - q)
    elif len(counts) == 3:
        q, r = 0, 0
        # p, q, r로 나누어지는 경우
        for num, count in counts.items():
            if count == 1:
                if q == 0:
                    q = num
                else:
                    r = num
        return q * r
    else:
        # 모든 주사위가 다른 경우
        return min(dice)
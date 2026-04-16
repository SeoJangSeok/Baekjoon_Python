def solution(park, routes):
    # 명령에 따른 이동 방향
    move = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    # 시작 위치
    S = [(row, col) for row in range(len(park)) for col in range(len(park[0])) if park[row][col]=='S'][0]
    
    # 각 명령 수행
    for route in routes:
        op, n = route.split()
        n = int(n)

        ch, cw = S # 현재 위치
        for _ in range(n):
            ch += move[op][0]
            cw += move[op][1]
            
            # 범위를 넘어선 경우
            if not (0 <= ch < len(park) and 0 <= cw < len(park[0])):
                break
            
            # 장애물이 있는 경우
            if park[ch][cw] == 'X':
                break
        else:
            # 모든 이동이 성공했을 때 현재 위치 업데이트
            S = (ch, cw)
    return list(S)
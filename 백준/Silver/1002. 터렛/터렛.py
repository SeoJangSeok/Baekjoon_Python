import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 원의 중심 사이의 거리
    dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if dis == 0: # 두 원이 동심원일 때
        if r1 == r2: # 두 원의 크기가 같을 때
            print(-1)
        else: # 한 원이 다른 원의 안에 포함될 때
            print(0)
    else: # 두 원의 중심이 다를 때
        if r1+r2 == dis or abs(r1-r2) == dis: # 외접 or 내접
            print(1)
        elif abs(r1-r2) < dis < r1+r2: # 두 점에서 만나는 경우
            print(2)
        else:
            print(0)
            
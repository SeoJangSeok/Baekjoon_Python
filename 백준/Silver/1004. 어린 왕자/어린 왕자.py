T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split()) # 출발점, 도착점
    n = int(input()) # 행성계의 개수
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split()) # 중점과 반지름
        dis1 = (x1 - cx) ** 2 + (y1 - cy) ** 2 # 출발점과 행성계 중점 사이의 거리
        dis2 = (x2 - cx) ** 2 + (y2 - cy) ** 2 # 도착점과 행성계 중점 사이의 거리
        pow_cr = r ** 2 
        
        if pow_cr > dis1 and pow_cr > dis2: # 출발점, 도착점이 행성계 안에 있는 경우
            continue
        elif pow_cr > dis1 or pow_cr > dis2: # 출발점, 도착점 중 하나가 행성계 안에 있는 경우
            count += 1
            
    print(count)
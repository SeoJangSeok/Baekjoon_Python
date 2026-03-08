N, M = map(int, input().split()) # N: 나무의 수, M: 필요한 길이
height = list(map(int, input().split())) # 나무의 높이

start, end = 0, max(height)

while start <= end:
    total = 0
    mid = (start + end) // 2 # 중간값
    
    for h in height:
        if h > mid:
            total += (h - mid)
    
    if total < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)
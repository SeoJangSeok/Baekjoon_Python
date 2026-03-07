K, N = map(int, input().split()) # K: 가지고 있는 랜선 개수, N: 필요한 랜선 개수
length = [int(input()) for _ in range(K)] # 가지고 있는 각 랜선의 길이

start, end = 1, max(length) # 가장 짧은 길이, 가장 긴 길이

while start <= end:
    mid = (start + end) // 2 # 중간 위치
    total = 0 # 만들 수 있는 랜선의 수
    for l in length:
        total += l // mid
    
    if total < N:
        end = mid - 1
    else:
        start = mid + 1
print(end)
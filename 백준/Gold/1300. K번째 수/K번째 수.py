N = int(input()) # 배열의 크기
k = int(input()) # 찾을 K 번째로 작은 수

start = 1
end = k
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    
    for i in range(1, N+1):
        count += min(mid // i, N)
    if count >= k: # 
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
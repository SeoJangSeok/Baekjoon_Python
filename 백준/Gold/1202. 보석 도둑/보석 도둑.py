import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split()) # 보석의 총 개수, 가방 개수

jewels_info = [list(map(int, input().split())) for _ in range(N)] # 보석의 정보(무게, 가격)
bags_storage = [int(input()) for _ in range(K)] # 가방에 담을 수 있는 최대 무게

jewels_info.sort()
bags_storage.sort()

answer = 0
price_heap = [] # 최대 힙

for storage in bags_storage:
    while jewels_info and storage >= jewels_info[0][0]:
        heapq.heappush(price_heap, -heapq.heappop(jewels_info)[1])
    if price_heap:
        answer += -heapq.heappop(price_heap)

print(answer)        
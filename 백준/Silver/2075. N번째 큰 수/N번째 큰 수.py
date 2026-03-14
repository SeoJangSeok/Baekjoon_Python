import sys
import heapq

input = sys.stdin.readline

min_heap = []
N = int(input())

for _ in range(N):
    numbers = map(int, input().split()) # N개의 수 입력
    for num in numbers:
        if len(min_heap) < N: # 찾을 수 있는 최대 N번째 수
            heapq.heappush(min_heap, num)
        else:
            if min_heap[0] < num:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
print(min_heap[0])
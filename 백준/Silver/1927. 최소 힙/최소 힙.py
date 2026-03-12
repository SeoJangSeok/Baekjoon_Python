import sys
import heapq

input = sys.stdin.readline

N = int(input()) # 연산의 개수
min_heap = []

for _ in range(N):
    x = int(input())
    
    if x > 0:
        heapq.heappush(min_heap, x)
    else:
        if not min_heap: # 배열이 비어있는 경우
            print(0)
        else:
            print(heapq.heappop(min_heap))
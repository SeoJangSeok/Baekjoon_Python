import sys
import heapq

input = sys.stdin.readline

N = int(input()) # 연산의 개수
abs_heap = []

for _ in range(N):
    x = int(input())
    
    if x:
        heapq.heappush(abs_heap, (abs(x), x)) # (1, -1)
    else:
        if not abs_heap: # 배열이 비어있는 경우
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])
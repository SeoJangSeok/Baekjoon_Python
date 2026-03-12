''' 
x > 0: 배열에 x 추가
x == 0: 배열에서 최대 값 출력 후 제거
'''
import sys
import heapq

input = sys.stdin.readline

N = int(input()) # 연산의 개수
max_heap = []

for _ in range(N):
    x = int(input())
    
    if x > 0:
        heapq.heappush(max_heap, -x)
    else:
        if not max_heap: # 배열이 비어있는 경우
            print(0)
        else:
            print(-heapq.heappop(max_heap))

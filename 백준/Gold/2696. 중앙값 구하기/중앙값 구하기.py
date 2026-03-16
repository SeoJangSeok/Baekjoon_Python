import sys
import heapq

input = sys.stdin.readline

def median_search(sequence):
    result = [sequence[0]]
    mid = sequence[0]
    left_heap, right_heap = [], [] # 최대 힙, 최소 힙
    
    for i in range(1, M):
        if sequence[i] > mid:
            heapq.heappush(right_heap, sequence[i])
        else:
            heapq.heappush(left_heap, -sequence[i])
        if i % 2 == 0:
            if len(left_heap) < len(right_heap):
                heapq.heappush(left_heap, -mid)
                mid = heapq.heappop(right_heap)
            elif len(left_heap) > len(right_heap):
                heapq.heappush(right_heap, mid)
                mid = -heapq.heappop(left_heap)
            result.append(mid)
    
    print(len(result)) # 중앙값의 개수
    for i in range(len(result)):
        if i > 0 and i % 10 == 0:
            print()
        print(result[i], end=' ')
    print()
            
    
T = int(input()) # 테스트 케이스

for _ in range(T):
    M = int(input()) # 수열의 크기
    sequence = [] # 입력받을 리스트
    # 주어지는 입력은 10개씩
    if M % 10 == 0:
        for _ in range(M // 10):
            sequence += list(map(int, input().split()))
    else:
        for _ in range(M // 10 + 1):
            sequence += list(map(int, input().split()))
    median_search(sequence)
N = int(input())
A = list(map(int, input().split()))

A.sort()

M = int(input())
target = list(map(int, input().split()))

def binary_search(start, end, target):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if A[mid] == target:
        return mid
    elif A[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(start, end, target)
    
for i in target:
    if binary_search(0, len(A)-1, i) is not None:
        print(1)
    else:
        print(0)
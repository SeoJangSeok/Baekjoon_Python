import sys
input = sys.stdin.readline


def binary_search(n):
    start = 0
    end = len(LIS) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if LIS[mid] == n:
            return mid
        elif LIS[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return start


N = int(input()) # 수열의 크기
A = list(map(int, input().split()))
LIS = [A[0]]

for i in A:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        idx = binary_search(i)
        LIS[idx] = i

print(len(LIS))
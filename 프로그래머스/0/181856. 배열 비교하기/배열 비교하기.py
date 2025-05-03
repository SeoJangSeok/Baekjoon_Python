def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        return 1 if len(arr1) > len(arr2) else -1
    else:
        return 1 if sum(arr1) > sum(arr2) else -1 if sum(arr1) < sum(arr2) else 0
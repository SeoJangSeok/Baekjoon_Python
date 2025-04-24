def solution(arr):
    X = []
    for i in arr:
        X.extend([i] * i)
    return X
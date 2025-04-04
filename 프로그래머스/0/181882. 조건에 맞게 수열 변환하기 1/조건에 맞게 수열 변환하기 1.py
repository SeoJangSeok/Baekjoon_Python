def solution(arr):
    for i, n in enumerate(arr):
        if n >= 50 and n % 2 == 0:
            arr[i] /= 2
        elif n < 50 and n % 2 == 1:
            arr[i] *= 2
    return arr
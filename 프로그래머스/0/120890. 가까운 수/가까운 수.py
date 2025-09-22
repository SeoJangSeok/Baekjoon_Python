def solution(array, n):
    array.append(n)
    array.sort()
    if n == array[-1]:
        return array[-2]
    elif n == array[0]:
        return array[1]
    else:
        if n - array[array.index(n) - 1] <= array[array.index(n) + 1] - n:
            return array[array.index(n) - 1]
        else:
            return array[array.index(n) + 1]
    
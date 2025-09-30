def solution(array):
    return sum(num.count('7') for num in map(str, array))
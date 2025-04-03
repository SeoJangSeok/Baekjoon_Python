def solution(numbers, n):
    sum = 0
    for i in numbers:
        sum += i
        if sum > n:
            return sum
def solution(numbers, k):
    if len(numbers) % 2 == 0:
        numbers = numbers[::2]
        return numbers[k % len(numbers) - 1]
    else:
        numbers = numbers[::2] + numbers[1::2]
        return numbers[k % len(numbers) - 1]
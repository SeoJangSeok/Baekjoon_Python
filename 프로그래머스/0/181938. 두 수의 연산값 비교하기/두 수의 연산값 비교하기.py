def solution(a, b):
    ab = int(f'{a}{b}')
    ab2 = 2 * a * b
    return max(ab, ab2)
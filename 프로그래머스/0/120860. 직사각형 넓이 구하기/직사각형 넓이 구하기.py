def solution(dots):
    sorted_dots = sorted(dots)
    width = sorted_dots[2][0] - sorted_dots[0][0]
    height = sorted_dots[1][1] - sorted_dots[0][1]
    return width * height    
def solution(array, height):
    taller = []
    for h in array:
        if h > height:
            taller.append(h)
    return len(taller)
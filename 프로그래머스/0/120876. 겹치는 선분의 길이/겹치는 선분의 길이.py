def solution(lines):
    sets = [set(range(line[0], line[1])) for line in lines]
    return len(sets[0] & sets[1] | sets[1] & sets[2] | sets[0] & sets[2])
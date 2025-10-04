def solution(sides):
    answer = 0
    for i in range(0, max(sides) + 1):
        if min(sides) + i > max(sides):
            print(i)
            answer += 1
    for i in range(max(sides) + 1, sum(sides)):
        if sum(sides) > i:
            print(i)
            answer += 1
    return answer
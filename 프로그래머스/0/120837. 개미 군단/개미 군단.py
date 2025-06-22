def solution(hp):
    ant = [5, 3, 1]
    answer = 0
    while hp > 0:
        for i in ant:
            answer += hp // i
            hp %= i
    return answer
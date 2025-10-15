def solution(score):
    sum_score = [sum(s) for s in score]
    rank = sorted(sum_score, reverse=True)
    return [rank.index(s) + 1 for s in sum_score]
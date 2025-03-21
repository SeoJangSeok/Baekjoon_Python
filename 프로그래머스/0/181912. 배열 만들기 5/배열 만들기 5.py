def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        if int(num[s : s+l]) > k:
            answer.append(int(num[s : s+l]))
    return answer
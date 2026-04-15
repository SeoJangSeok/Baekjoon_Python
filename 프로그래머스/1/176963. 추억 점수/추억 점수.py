def solution(name, yearning, photo):
    answer = []
    
    dic = {name[i]: yearning[i] for i in range(len(name))}
    
    for group in photo:
        total = 0
        for person in group:
            if person in dic:
                total += dic[person]
        answer.append(total)
    
    return answer
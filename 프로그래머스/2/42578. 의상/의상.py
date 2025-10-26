def solution(clothes):
    answer = 1
    clothes_dict = {}
    for item, category in clothes:
        if category not in clothes_dict.keys():
            clothes_dict[category] = [item]
        else:
            clothes_dict[category].append(item)
        print(clothes_dict)

    for key, value in clothes_dict.items():
        answer *= (len(value) + 1)
    
    return answer - 1
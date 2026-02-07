def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                time = j - i
                break
            else:
                time += 1
        answer.append(time)
    return answer
                
                
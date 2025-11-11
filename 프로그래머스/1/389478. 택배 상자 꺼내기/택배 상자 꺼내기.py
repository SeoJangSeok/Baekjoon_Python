def solution(n, w, num):
    storage = []
    height = n // w + 1
    x = 1 # 상자 번호
    answer = 0
    
    # 상자 적재
    for i in range(height):
        row = []
        for j in range(w):
            if x <= n: # 마지막 상자번호 보다 작은 상자들
                row.append(x)
                x += 1
            else:
                row.append(0) # 마지막 상자 이후의 공간은 0
        
        if i % 2 == 0: # 오른쪽으로
            storage.append(row)
        else: # 왼쪽으로
            row.reverse()
            storage.append(row)
    # 상자 탐색
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if storage[i][j] == num:
                d = i
                while d < height and storage[d][j]: # 꺼낼 상자가 있는 경우
                    answer += 1
                    d += 1 # 아래로
    return answer
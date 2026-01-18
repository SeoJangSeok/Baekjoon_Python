def backtracking():
    if len(seq) == M:
        print(*seq)
        return
    
    for i in range(1, N+1):
        seq.append(i)
        backtracking()
        seq.pop()
            
seq = [] # 수열 저장
N, M = map(int, input().split())

backtracking()
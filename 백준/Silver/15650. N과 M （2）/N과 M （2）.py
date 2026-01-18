def backtracking(start):
    if len(seq) == M:
        print(*seq)
        return
    
    for i in range(start, N+1):
        if i not in seq:
            seq.append(i)
            backtracking(i+1)
            seq.pop()
            
seq = [] # 수열 저장
N, M = map(int, input().split())

backtracking(1)
import sys
input = sys.stdin.readline

def dfs(n, team_a, team_b):
    global answer
    if n == N:
        if len(team_a) == len(team_b):
            total_a = total_b = 0
            for i in range(M):
                for j in range(M):
                    total_a += start_link[team_a[i]][team_a[j]]
                    total_b += start_link[team_b[i]][team_b[j]]
            answer = min(answer, abs(total_a - total_b))
        return
    
    dfs(n+1, team_a+[n], team_b) # A팀에 n번 선수를 추가한 경우
    dfs(n+1, team_a, team_b+[n]) # B팀에 n번 선수를 추가한 경우

N = int(input())
start_link = [list(map(int, input().split())) for _ in range(N)]

M = N // 2
answer = 1e9
dfs(0, [], [])
print(answer)
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

def check(start_color):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for row in range(N):
        for col in range(M):
            if ((row + col) % 2 == 0):
                v = (board[row][col] != start_color)
            else:
                v = (board[row][col] == start_color)

            dp[row + 1][col + 1] = dp[row][col + 1] + dp[row + 1][col] - dp[row][col] + v

    MIN = N * M
    for row in range(1, N - K + 2):
        for col in range(1, M - K + 2):
            MIN = min(MIN, dp[row + K - 1][col + K - 1] - dp[row + K - 1][col - 1] - dp[row - 1][col + K - 1] + dp[row - 1][col - 1])

    return MIN

answer = min(check('B'), check('W'))
print(answer)
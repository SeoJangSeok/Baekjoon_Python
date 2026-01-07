import sys
input = sys.stdin.readline

n = int(input())
chat_logs = dict()
answer = 0

for _ in range(n):
    chat = input().strip()

    if chat == "ENTER":
        chat_logs.clear()
    else:
        if chat not in chat_logs:
            chat_logs[chat] = 1
            answer += 1

print(answer)
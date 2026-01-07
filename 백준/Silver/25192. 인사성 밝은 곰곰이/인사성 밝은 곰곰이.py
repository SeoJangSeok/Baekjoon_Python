n = int(input())
chat_logs = dict()
cnt = 0

for _ in range(n):
    chat = input()
    
    if chat == "ENTER":
        chat_logs.clear()
    else:
        if chat not in chat_logs:
            chat_logs[chat] = 1
            cnt += 1
            
print(cnt)
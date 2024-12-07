h, m = map(int, input().split())
timer = int(input())

total_hour = h + (m + timer)//60
total_minute = (m + timer)%60

if total_hour > 23:
    total_hour %= 24
    
print(total_hour, total_minute)
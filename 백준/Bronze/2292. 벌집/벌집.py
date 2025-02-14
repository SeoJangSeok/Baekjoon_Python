N = int(input()) # 방 번호
room = 1 # 현재 위치
count = 1 # 이동 횟수

while N > room: # 현재 위치 + 6번 방까지 이동 횟수 1씩 증가
    room += 6 * count
    count += 1    
print(count)
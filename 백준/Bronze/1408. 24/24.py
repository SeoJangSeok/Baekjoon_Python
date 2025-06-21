current_time = input()
start_time = input()

ch, cm, cs = map(int, current_time.split(':'))
sh, sm, ss = map(int, start_time.split(':'))

current_sec = ch * 3600 + cm * 60 + cs
start_sec = sh * 3600 + sm * 60 + ss

diff_sec = start_sec - current_sec
if diff_sec < 0:
    diff_sec += 24 * 60 * 60

print(f'{diff_sec // 3600:02d}:{diff_sec % 3600 // 60:02d}:{diff_sec % 60:02d}')
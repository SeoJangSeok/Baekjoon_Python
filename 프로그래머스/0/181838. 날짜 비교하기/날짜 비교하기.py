def solution(date1, date2):
    date1 = ''.join([str(x).zfill(2) for x in date1])
    date2 = ''.join([str(x).zfill(2) for x in date2])
    
    if int(date1) < int(date2):
        return 1
    else:
        return 0
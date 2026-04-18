def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = sum(month_days[:a-1]) + (b-1)
    return days[total_day % 7]
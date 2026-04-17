def solution(s):
    count = 0
    i = 0

    while i < len(s):
        count_x = 0
        count_not_x = 0
        
        for j in range(i, len(s)):
            if s[j] == s[i]:
                count_x += 1
            else:
                count_not_x += 1 
                
            if count_x == count_not_x:
                break
                
        count += 1
        i = j + 1

    return count
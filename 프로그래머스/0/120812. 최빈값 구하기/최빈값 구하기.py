def solution(array):
    count_arr = [0] * (max(array) + 1)
    
    for i in array:
        count_arr[i] += 1
    if count_arr.count(max(count_arr)) > 1:
        return -1
    return count_arr.index(max(count_arr))
def solution(arr):
    row_count = len(arr)
    col_count = len(arr[0])
    if row_count > col_count:
        for i in range(row_count):
            for j in range(row_count - col_count):
                arr[i].append(0)
    elif row_count < col_count:
        for i in range(col_count - row_count):
            arr.append([0] * col_count)
    return arr
    
        
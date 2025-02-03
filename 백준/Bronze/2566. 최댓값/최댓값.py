table = []

for row in range(9):
    column = list(map(int, input().split()))
    table.append(column)
    
max_num = 0
max_row, max_col = 0, 0

for row in range(9):
    for col in range(9):
        if table[row][col] >= max_num:
            max_num = table[row][col]
            max_row, max_col = row+1, col+1
print(max_num)
print(max_row, max_col)
            
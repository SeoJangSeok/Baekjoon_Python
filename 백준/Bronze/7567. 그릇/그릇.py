dish = list(input())
height = 0

for i in range(len(dish)):
    if i == 0:
        height += 10
    elif dish[i] == dish[i-1]:
        height += 5
    else:
        height += 10
print(height)
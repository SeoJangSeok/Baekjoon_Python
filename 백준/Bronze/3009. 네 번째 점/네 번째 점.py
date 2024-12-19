x = []
y = []

for _ in range(3):
    x_, y_ = map(int, input().split())
    x.append(x_)
    y.append(y_)

for i in range(3):
    if x.count(x[i]) == 1:
        x4 = x[i]
    if y.count(y[i]) == 1:
        y4 = y[i]
print(x4, y4)
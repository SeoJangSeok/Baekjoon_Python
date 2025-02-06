string = [input() for _ in range(5)]

for col in range(15):
    for row in range(5):
        if col < len(string[row]):
            print(string[row][col], end='')
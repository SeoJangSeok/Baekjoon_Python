colored_paper = int(input()) # 색종이 개수
paper = [[0 for _ in range(100)] for _ in range(100)] # 도화지 범위 초기화 100X100

for i in range(colored_paper):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if i > 99 or j > 99: # 도화지의 범위(100 X 100)
                break
            paper[i][j] = 1
area = 0 # 넓이
for k in range(100):
    area += paper[k].count(1)
print(area)
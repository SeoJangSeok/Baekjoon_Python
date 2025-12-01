N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        white_index = 0 # 흰색으로 시작
        black_index = 0 # 검정으로 시작
        for i in range(a,a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        white_index += 1
                    if original[i][j] != 'B':
                        black_index += 1
                else:
                    if original[i][j] != 'B':
                        white_index += 1
                    if original[i][j] != 'W':
                        black_index += 1
        count.append(min(white_index, black_index))
print(min(count))
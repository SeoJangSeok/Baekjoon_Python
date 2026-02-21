N = int(input())
quad_tree = [list(map(int, input())) for _ in range(N)]

def compress(x, y, n):
    first = quad_tree[x][y] # 기준값
    for i in range(x, x+n):
        for j in range(y, y+n):
            if quad_tree[i][j] != first:
                half = n // 2
                return '(' + \
                    compress(x, y, half) + \
                    compress(x, y+half, half) + \
                    compress(x+half, y, half) + \
                    compress(x+half, y+half, half) + \
                    ')'
    return str(first)
            
print(compress(0, 0, N))   
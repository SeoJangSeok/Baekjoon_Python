tri = sorted(list(map(int, input().split())))

if tri[0] + tri[1] > tri[2]:
    print(sum(tri))
else:
    print(tri[0] + tri[1] + (tri[0] + tri[1] - 1))
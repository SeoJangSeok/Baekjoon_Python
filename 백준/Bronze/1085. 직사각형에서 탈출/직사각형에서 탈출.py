x, y, w, h = map(int, input().split())
dis_x = min(w - x, x - 0)
dis_y = min(h - y, y - 0)
print(min(dis_x, dis_y))
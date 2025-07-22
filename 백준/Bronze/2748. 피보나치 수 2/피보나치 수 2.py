n = int(input())
fi_prev, fi_current = 0, 1
if n < 2:
    print(n)
else:
    for _ in range(2, n + 1):
        fi_prev, fi_current = fi_current, fi_prev + fi_current
    print(fi_current)
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

a, b = map(int, input().split())
c, d = map(int, input().split())

lcm = b * d // gcd(b, d)

# 분자, 분모
numerator = a * (lcm // b) + c * (lcm // d)
denominator = lcm

g = gcd(numerator, denominator)
numerator //= g
denominator //= g

print(numerator, denominator)
from math import sqrt, ceil

r, x, y, x1, y1 = map(int, input().split())
print(ceil(sqrt((x - x1) ** 2 + (y - y1) ** 2) / 2 / r))

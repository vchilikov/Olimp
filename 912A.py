a, b = map(int, input().split())
x, y, z = map(int, input().split())
print(max(2 * x + y - a, 0) + max(y + 3 * z - b, 0))

n, s = map(int, input().split())
res = -1
for i in range(n):
    x, y = map(int, input().split())
    if 100 * x + y <= 100 * s:
        res = max(res, (100 - y) % 100)
print(res)

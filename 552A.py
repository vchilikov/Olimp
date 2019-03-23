n = int(input())
res = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    res += (x2 - x1 + 1) * (y2 - y1 + 1)
print(res)

n, m = map(int, input().split())
res = []
for _ in range(n):
    a, b = map(int, input().split())
    res.append(m * a / b)
print(min(res))
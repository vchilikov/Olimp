n, m = map(int, input().split())
a = [[0] * n for _ in range(m)]
for i in range(n):
    for j, el in enumerate(input()):
        a[j][i] = el

res = set()
for j in range(m):
    best = set()
    max_el = max(a[j])
    for i in range(n):
        if a[j][i] == max_el:
            best.add(i)
    res.update(best)

print(len(res))

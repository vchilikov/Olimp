n, q = map(int, input().split())
res = []
for _ in range(q):
    x, y = map(int, input().split())
    if (y - x % 2) % 2 == 0:
        res.append(str((x // 2) * ((n + 1) // 2) + ((x - 1) // 2) * (n // 2) + (y + x % 2) // 2))
    else:
        res.append(str((n * n + 1) // 2 + (x // 2) * (n // 2) + ((x - 1) // 2) * ((n + 1) // 2) + (y + (x + 1) % 2) // 2))

print('\n'.join(res))

n, q = map(int, input().split())
results = []
for _ in range(q):
    x, y = map(int, input().split())
    if (y - x % 2) % 2:
        res = (x // 2) * (n // 2) + ((x - 1) // 2) * ((n + 1) // 2) + (y + (x + 1) % 2) // 2 + (n * n + 1) // 2
    else:
        res = (x // 2) * ((n + 1) // 2) + ((x - 1) // 2) * (n // 2) + (y + x % 2) // 2
    results.append(str(res))

print('\n'.join(results))

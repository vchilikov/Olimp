n, k = map(int, input().split())
if k <= n - n // 2:
    print(k * 2 - 1)
else:
    print((k - (n - n // 2)) * 2)

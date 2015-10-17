n, d = map(int, input().split())
t = sum(map(int, input().split()))
if (n - 1) * 10 + t > d:
    print(-1)
else:
    print((n - 1) * 2 + ((d - t - (n - 1) * 10) // 5))

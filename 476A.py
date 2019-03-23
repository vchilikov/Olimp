n, m = map(int, input().split())
res = n // 2 + n % 2
if res % m != 0:
    res += (m - res % m)
print(res if res <= n else -1)

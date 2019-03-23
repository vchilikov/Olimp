n, m = map(int, input().split())
f = sorted(map(int, input().split()))
d = f[-1]
for i in range(m - n + 1):
    d = min(d, f[n + i - 1] - f[i])

print(d)
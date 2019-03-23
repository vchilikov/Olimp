n, k = map(int, input().split())
res = -10**9
for _ in range(n):
    f, t = map(int, input().split())
    res = max(res, min(f, f - (t - k)))
print(res)
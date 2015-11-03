import bisect

n = int(input())
t = sorted(tuple(map(int, input().split())) for i in range(n))
b = bisect.bisect_left(t, (0, 0))
l = min(b, n - b) + 1
print(sum((t[b + i][1] if b + i < n else 0) + (t[b - i - 1][1] if b - i - 1 >= 0 else 0) for i in range(l)))

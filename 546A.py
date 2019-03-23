k, n, w = map(int, input().split())
for i in range(1, w + 1):
    n -= i * k
print(0 if n > 0 else -n)
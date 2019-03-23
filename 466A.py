n, m, a, b = map(int, input().split())
if m * a < b:
    print(n * a)
elif n % m * a < b:
    print(n // m * b + n % m * a)
else:
    print((n // m + 1) * b)

def f(a):
    return a * (a - 1) // 2


n, m = map(int, input().split())
f_max = f(n - m + 1)
f_min = (n - m * (n // m)) * f(n // m + 1) + (m - n + m * (n // m)) * f(n // m)
print(f_min, f_max)
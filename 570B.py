n, m = map(int, input().split())
a = n / 2
if m <= a:
    a = m + 1
else:
    a = m - 1
if a < 1:
    a = 1
if a > n:
    a = n
print(a)

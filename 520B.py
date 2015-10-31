n, m = map(int, input().split())
res = 0
while m > n:
    if m % 2:
        m = (m + 1) // 2
        res += 2
    else:
        m //= 2
        res += 1

print(res + n - m)

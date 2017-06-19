n, t = map(int, input().split())
a = list(map(int, input().split()))
i, j, s = 0, 0, 0

for j in range(len(a)):
    s += a[j]
    if s > t:
        s -= a[i]
        i += 1

print(j - i + 1)

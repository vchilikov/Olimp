n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sorted(a)
res = []
for i in range(n):
    k -= s[i]
    if k < 0:
        break
    res += [str(a.index(s[i]) + 1)]
    a[a.index(s[i])] = 0
print(len(res))
print(" ".join(res))

n = int(input())
a = {}
res = []
for _ in range(n):
    s = input()
    if s in a:
        a[s] += 1
        res.append(s + str(a[s]))
    else:
        a[s] = 0
        res.append("OK")
print("\n".join(res))

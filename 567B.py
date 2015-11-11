n = int(input())
s = set()
res = 0
for i in range(n):
    r = int(input().replace(' ', ''))
    if r > 0:
        s.add(r)
    elif -r in s:
        s.remove(-r)
    else:
        res += 1
    res = max(res, len(s))
print(res)
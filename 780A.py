input()
res = 0
s = set()
for el in input().split():
    if el in s:
        s.remove(el)
    else:
        s.add(el)
        res = max(res, len(s))
print(res)

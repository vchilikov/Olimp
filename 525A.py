n = int(input())
s = input().lower()
res = 0
d = {}
for i in range(len(s)):
    if i % 2 == 0:
        d[s[i]] = d.get(s[i], 0) + 1
    else:
        if d.get(s[i], 0) > 0:
            d[s[i]] -= 1
        else:
            res += 1
print(res)

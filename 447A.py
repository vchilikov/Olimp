p, n = map(int, input().split())
s = set()
res = -1
for i in range(n):
    h = int(input()) % p
    if h in s:
        res = i + 1
        break
    s.add(h)
print(res)

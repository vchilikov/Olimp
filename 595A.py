n, m = map(int, input().split())
res = 0
for _ in range(n):
    s = input().split()
    res += sum(map(lambda x, y: int(x) or int(y), s[::2], s[1::2]))
print(res)

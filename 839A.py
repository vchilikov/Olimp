n, k = map(int, input().split())
s = 0
for i, v in enumerate(map(int, input().split())):
    k -= min(8, s + v)
    s += v - min(8, s + v)
    if k <= 0:
        print(i + 1)
        exit()
print(-1)

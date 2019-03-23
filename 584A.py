n, t = map(int, input().split())
res = -1
for i in range(10 ** (n - 1), 10 ** n):
    if i % t == 0:
        res = i
        break
print(res)

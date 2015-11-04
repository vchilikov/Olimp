n, c = map(int, input().split())
x = input().split()
res = c
for i in range(n - 1):
    res = max(res, int(x[i]) - int(x[i + 1]))
print(max(0, res - c))

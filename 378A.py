a, b = map(int, input().split())

res0, res1, res2 = 0, 0, 0
for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        res1 += 1
    elif abs(a - i) > abs(b - i):
        res2 += 1
    else:
        res0 += 1
print(res1, res0, res2)
n, x = map(int, input().split())
c = sorted(map(int, input().split()))
res = 0
for el in c:
    res += el * x
    if x > 1:
        x -= 1
print(res)

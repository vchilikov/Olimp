x1, y1, x2, y2 = map(int, input().split())
a = max(abs(x1 - x2), abs(y1 - y2))
b = min(abs(x1 - x2), abs(y1 - y2))

res = a + b
if b == 0:
    print(0)
    exit()

for i in range(1, a+1):
    if b * i % a == 0:
        res -= a // i
        break

print(res)

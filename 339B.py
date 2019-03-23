n, m = map(int, input().split())
current = 1
res = 0
for el in map(int, input().split()):
    if el >= current:
        res += el - current
    else:
        res += el + (n - current)
    current = el
print(res)
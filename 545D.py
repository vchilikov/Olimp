n = int(input())
t = sorted(map(int, input().split()))
s = 0
res = 0
for el in t:
    if s <= el:
        res += 1
        s += el
print(res)
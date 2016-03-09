n = int(input())
a = list(map(int, input().split()))
res = sum(a)
if res % 2:
    res -= min(el for el in a if el % 2)
print(res)

n = int(input())
a = sorted(map(int, input().split()))
res = -a[-1]
for i in range(n):
    res += a[i] * (i + 2)
print(res)

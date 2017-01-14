n, a = map(int, input().split())
t = list(map(int, input().split()))
res = t[a - 1]
for i in range(n):
    if a - i - 2 >= 0 and a + i < n and t[a - i - 2] and t[a + i]:
        res += 2
    elif a - i - 2 >= 0 and a + i >= n:
        res += t[a - i - 2]
    elif a - i - 2 < 0 and a + i < n:
        res += t[a + i]
print(res)

n, m = map(int, input().split())
res = 0
for _ in range(n):
    s = input().split()
    for j in range(m):
        res += s[j * 2] == '1' or s[j * 2 + 1] == '1'
print(res)

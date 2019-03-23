n, m = map(int, input().split())
a = [input() for i in range(n)]
cnt = 0
for i in range(n - 1):
    for j in range(m - 1):
        s = a[i][j] + a[i + 1][j] + a[i][j + 1] + a[i + 1][j + 1]
        cnt += "f" in s and "a" in s and "c" in s and "e" in s
print(cnt)

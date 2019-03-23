n, d = map(int, input().split())
cnt, res = 0, 0
for i in range(d):
    cnt = cnt + 1 if '0' in input() else 0
    res = max(res, cnt)
print(res)
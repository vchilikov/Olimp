n, t, c = map(int, input().split())
res, cnt = 0, 0
for el in map(int, input().split()):
    if el > t:
        res += max(0, cnt - c + 1)
        cnt = 0
    else:
        cnt += 1
print(res + max(0, cnt - c + 1))

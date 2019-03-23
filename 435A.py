n, m = map(int, input().split())
cnt = 1
group = 0
for el in map(int, input().split()):
    if group + el > m:
        cnt += 1
        group = el
    else:
        group += el
print(cnt)

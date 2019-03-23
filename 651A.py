a1, a2 = map(int, input().split())
cnt = 0
while a1 > 0 and a2 > 0 and (a1 > 1 or a2 > 1):
    cnt += 1
    if a1 > a2:
        a2 += 1
        a1 -= 2
    else:
        a1 += 1
        a2 -= 2
print(cnt)

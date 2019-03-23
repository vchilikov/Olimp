a = input().split()
res = 0
a[0] = int(a[0])
if a[2] == 'month':
    if a[0] <= 29:
        res = 12
    elif int(a[0]) == 30:
        res = 11
    else:
        res = 7
else:
    if a[0] in (5, 6):
        res = 53
    else:
        res = 52

print(res)
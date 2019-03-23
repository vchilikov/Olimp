n = int(input())
position = 20000
b = True
for _ in range(n):
    s = input().split()
    t, dir = int(s[0]), s[1]
    if (position == 20000 and dir != 'South') or (position == 0 and dir != 'North'):
        b = False
        break
    if dir == 'South':
        position -= t
    elif dir == 'North':
        position += t
    if position < 0 or position > 20000:
        b = False
        break
print('YES' if b and position == 20000 else 'NO')
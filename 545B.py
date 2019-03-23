res = []
cnt = 0
for s, t in zip(input(), input()):
    if s == t:
        res.append('0')
    else:
        res.append(str((int(s) + cnt) % 2))
        cnt += 1

print(''.join(res) if cnt % 2 == 0 else 'impossible')
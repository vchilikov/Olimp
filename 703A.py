cnt_m, cnt_c = 0, 0
for _ in range(int(input())):
    m, c = map(int, input().split())
    cnt_m += int(m > c)
    cnt_c += int(c > m)

if cnt_m > cnt_c:
    print('Mishka')
elif cnt_c > cnt_m:
    print('Chris')
else:
    print('Friendship is magic!^^')
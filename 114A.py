k = int(input())
l = int(input())
res = k
cnt = 0
while res < l:
    res *= k
    cnt += 1

if res == l:
    print('YES')
    print(cnt)
else:
    print('NO')

n = int(input())
a = list(map(int, input().split()))
cnt = 0
res = 0
while len(a):
    b = []
    for el in a:
        if el <= cnt:
            cnt += 1
        else:
            b.append(el)
    a = b[::-1]
    res += 1
print(res - 1)
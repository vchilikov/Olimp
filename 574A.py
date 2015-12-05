n = int(input())
a = list(map(int, input().split()))
a0 = a[0]
a = sorted(a[1:])
cnt = 0
while a0 <= a[-1]:
    cnt += 1
    a0 += 1
    a[-1] -= 1
    a.sort()
print(cnt)
n = int(input())
a = sorted(map(int, input().split()))
res = False
for i in range(len(a) - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        res = True
        break
print('YES' if res else 'NO')

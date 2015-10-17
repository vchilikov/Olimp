n = int(input())
a = [1] + list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

for i in range(1, n + 1):
    a[i] += a[i - 1]

i = 0
d = dict.fromkeys(q, 0)
for el in sorted(d):
    while el >= a[i]:
        i += 1
    d[el] = i

res = []
for el in q:
    res += [str(d[el])]
print("\n".join(res))
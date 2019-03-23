n, m = map(int, input().split())
a = input().split()
s = set()
for i in range(n - 1, -1, -1):
    s.add(a[i])
    a[i] = str(len(s))
print('\n'.join([a[int(input()) - 1] for _ in range(m)]))

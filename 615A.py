n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.update(input().split()[1:])
print('YES' if len(s) == m else 'NO')
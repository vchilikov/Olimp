from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
d = defaultdict(set)

for i in range(n - 1):
    x, y = map(lambda x: int(x) - 1, input().split())
    d[x].add(y)
    d[y].add(x)

cnt = 0
s = {0}
b[0] = a[0]
processed = set()
while s:
    processed.update(s)
    new_s = set()
    for el in s:
        children = d[el] - processed
        if children:
            for next_el in children:
                b[next_el] = b[el] + 1 if a[next_el] else 0
                if b[next_el] <= m:
                    new_s.add(next_el)
        elif b[el] <= m:
            cnt += 1

    s = new_s
print(cnt)

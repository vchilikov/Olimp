from datetime import datetime
from random import randint

start = datetime.now()

n = int(input())
c = list(map(int, input().split()))
a = list(map(lambda x: int(x) - 1, input().split()))
# n = 1000
# c = [1] * n
# a = [randint(0, n-1) for i in range(n)]

b = [None] * n
processed = [False for i in range(n)]
for i in range(n):
    if not b[a[i]]:
        b[a[i]] = {i}
    else:
        b[a[i]].add(i)

rings = []


def processed_ring(ring):
    copy_ring = ring.copy()
    while copy_ring:
        new_ring = set()
        for el in copy_ring:
            processed[el] = True
            if b[el]:
                new_ring |= b[el]
        copy_ring = new_ring - copy_ring


for i in range(n):
    if processed[i]:
        continue
    ring = set()
    position = set()
    next_pos = i
    while next_pos not in position:
        position.add(next_pos)
        next_pos = a[next_pos]
    while next_pos not in ring:
        ring.add(next_pos)
        next_pos = a[next_pos]
    processed_ring(ring)
    rings.append(ring)

res = sum(min(c[i] for i in ring) for ring in rings)
print(res)
print(datetime.now() - start)

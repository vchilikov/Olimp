from collections import  defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(list)

for i in range(n - 1):
    x, y = tuple(map(lambda x: int(x) - 1, input().split()))
    d[x].append(y)

result = []

s = {0}

while s:
    print(s)
    new_s = set()
    for el in s:
        new_s.update(d[el])
    s = new_s




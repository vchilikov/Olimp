import sys

sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
tree = {}
for i in range(n - 1):
    x, y = map(int, input().split())
    tree[x] = tree.get(x, []) + [y]
    tree[y] = tree.get(y, []) + [x]

nodes = set()
res = 0


def find(v, cnt):
    nodes.add(v)
    if cnt > m:
        return
    next_v = set(tree[v]) - nodes
    if next_v:
        for el in next_v:
            find(el, cnt + a[v] if a[v] else 0)
    else:

        if cnt + a[v] <= m:
            global res
            res += 1


find(1, 0)
print(res)

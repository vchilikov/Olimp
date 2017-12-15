import sys

sys.setrecursionlimit(100000)
n, m = 100000, 6
a = [0] + [0] * n
base_tree = {v: [] for v in range(1, n + 1)}
for i in range(n - 1):
    x, y = i + 1, i + 2
    base_tree[y].append(x)
    base_tree[x].append(y)



# n, m = map(int, input().split())
# a = [0] + list(map(int, input().split()))
# base_tree = {v: [] for v in range(1, n + 1)}
# restaurants = set(range(1, n + 1))
# for i in range(n - 1):
#     x, y = map(int, input().split())
#     base_tree[y].append(x)
#     base_tree[x].append(y)

res = 0
def find(v, prev_v, cnt):
    print(v)
    next_cnt = cnt + 1 if a[v] else 0
    if next_cnt > m:
        return
    if len(base_tree[v]) == 1 and v != 1:
        global res
        res += 1
        return
    for next_v in base_tree[v]:
        if next_v == prev_v:
            continue
        find(next_v, v, next_cnt)



find(1, None, 0)
print(res)



# def number_of_cats(restaurant):
#     r = restaurant
#     res = 0
#     cnt = a[r]
#     while r in tree:
#         r = tree[r]
#         if a[r]:
#             cnt += 1
#         else:
#             cnt = 0
#         res = max(res, cnt)
#     return res
#
#
# cnt = 0
# for r in restaurants:
#     if number_of_cats(r) <= m:
#         cnt += 1
#
# print(cnt)

# import sys
#
# sys.setrecursionlimit(1000000)
#
# n, m = map(int, input().split())
# a = [0] + list(map(int, input().split()))
# tree = {}
# for i in range(n - 1):
#     x, y = map(int, input().split())
#     tree[x] = tree.get(x, []) + [y]
#     tree[y] = tree.get(y, []) + [x]
#
# nodes = set()
# res = 0
#
#
# def find(v, cnt):
#     nodes.add(v)
#     if cnt > m:
#         return
#     next_v = set(tree[v]) - nodes
#     if next_v:
#         for el in next_v:
#             find(el, cnt + a[v] if a[v] else 0)
#     else:
#
#         if cnt + a[v] <= m:
#             global res
#             res += 1
#
#
# find(1, 0)
# print(res)

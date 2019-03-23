def swap(t, i, j):
    return t[:i] + t[j:j+2] + t[i+2:j] + t[i:i+2] + t[j+2:]


n = 6
root_el = tuple(range(1, n + 1))
tree = {root_el: None}

while True:
    count = 0
    for el in list(tree):
        for i in range(n - 3):
            for j in range(i + 2, n - 1):
                new_el = swap(el, i, j)
                if new_el not in tree.keys():
                    tree[new_el] = el
                    count += 1
    if count == 0:
        break

a = tuple(map(int, input().split()))
if a not in tree:
    print('Нет решения')
else:
    if not tree[a]:
        print(a)
    while tree[a]:
        print(tree[a])
        a = tree[a]
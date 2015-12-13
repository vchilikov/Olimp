n, k = map(int, input().split())
i = 1
j = n
res = []
for step in range(k):
    if step % 2:
        res += [j]
        j -= 1
    else:
        res += [i]
        i += 1
res = list(range(i, j + 1)) + res
print(' '.join(map(str, res)))

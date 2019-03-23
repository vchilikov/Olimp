from math import log2

t = int(input())
res = []
for _ in range(t):
    n = int(input())
    r = n * (n + 1) // 2 - 2 ** (int(log2(n)) + 2) + 2
    res += [str(r)]
print('\n'.join(res))

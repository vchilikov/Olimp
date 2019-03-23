n = int(input())
res = []
for i in range(n):
    s = set(map(int, input().split()))
    if not (1 in s or 3 in s):
        res += [str(i + 1)]
print(len(res))
print(" ".join(res))

n, m = map(int, input().split())
a = list(map(lambda x: (int(x) + m - 1) // m, input().split()))
last = 0
for i in range(n):
    if a[i] >= a[last]:
        last = i
print(last + 1)

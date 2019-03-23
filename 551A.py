n = int(input())
a = list(map(int, input().split()))
d = sorted(a, reverse=True)
print(" ".join(str(d.index(a[i]) + 1) for i in range(n)))

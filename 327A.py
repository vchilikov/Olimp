n = int(input())
a = list(map(int, input().split()))
max_a = -100
for i in range(n):
    for j in range(i, n):
        max_a = max(max_a, a[i: j + 1].count(0) - a[i: j + 1].count(1))
print(sum(a) + max_a)

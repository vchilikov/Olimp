n = int(input())
a = list(map(int, input().split()))
max_l = 0
l = 1
for i in range(1, n):
    if a[i - 1] > a[i]:
        max_l = max(max_l, l)
        l = 1
    else:
        l += 1

print(max(max_l, l))
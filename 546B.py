n = int(input())
a = sorted(map(int, input().split()))
cost = 0
for i in range(1, n):
    if a[i-1] >= a[i]:
        cost += a[i-1] - a[i] + 1
        a[i] = a[i-1] +1
print(cost)
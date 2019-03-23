n = int(input())
a = list(map(int, input().split()))
b, e = 0, 0
sorted_a = sorted(a)
if sorted_a == a:
    print("yes")
    print(b + 1, e + 1)
    exit()
for i in range(n - 1):
    if a[i] > a[i + 1]:
        b = i
        while i < n - 1 and a[i] > a[i + 1]:
            i += 1
        e = i
        break
if sorted_a == a[:b] + a[b:e + 1][::-1] + a[e + 1:]:
    print("yes")
    print(b + 1, e + 1)
else:
    print("no")

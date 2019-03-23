n = int(input())
a = list(map(int, input().split()))
for _ in range(n):
    for i in range(n - 1):
        if a[i] >= a[i + 1]:
            break
    else:
        print('Yes')
        exit()
    for i in range(n):
        a[i] = (a[i] + (-1 if i % 2 else 1)) % n
print('No')

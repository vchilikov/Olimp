n = int(input())
a = list(map(int, input().split()))
a_half = sum(a) * 2 // n
for i in range(n- 1):
    for j in range(i + 1, n):
        if a[i] + a[j] == a_half:
            print(i + 1, j + 1)
            a[i] = a[j] = 0
n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = sorted(map(int, input().split()))
i, j, cnt = 0, 0, 0
while i < n and j < m:
    if abs(a[i] - b[j]) <= 1:
        cnt += 1
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(cnt)

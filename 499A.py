n, x = map(int, input().split())
i = 1
cnt = 0
for _ in range(n):
    left, right = map(int, input().split())
    i += (left - i) // x * x
    cnt += right - i + 1
    i = right + 1
print(cnt)

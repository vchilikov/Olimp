n, m = map(int, input().split())
result = set(range(1, m + 1))
for i in range(n):
    left, right = map(int, input().split())
    result -= set(range(left, right + 1))
print(len(result))
print(' '.join(map(str, result)))

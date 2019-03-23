n, m, k = map(int, input().split())
print(min(10 * abs(m - i - 1) for i, v in enumerate(map(int, input().split())) if 0 < v <= k))

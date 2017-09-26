from collections import Counter
n, k = map(int, input().split())
print('YES' if k >= max(Counter(input()).values()) else 'NO')


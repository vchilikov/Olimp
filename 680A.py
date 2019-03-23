from collections import Counter

t = list(map(int, input().split()))
cnt = Counter(t)
print(sum(t) - max([2 * el if cnt[el] == 2 else 3 * el for el in cnt if cnt[el] > 1] + [0]))
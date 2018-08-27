from collections import Counter

n = int(input())
print(max(Counter(map(int, input().split())).values()))

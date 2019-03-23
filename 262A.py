n, k = map(int, input().split())
print(sum(el.count('4') + el.count('7') <= k for el in input().split()))

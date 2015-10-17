n, k = map(int, input().split())
f = sorted(map(int, input().split()))
print(2 * sum(el - 1 for el in f[n::-k]))
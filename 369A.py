n, m, k = map(int, input().split())
inp = input()
k -= inp.count("2")
m -= inp.count("1") + max(0, -k)
print(max(0, -m))
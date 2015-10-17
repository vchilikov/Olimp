n, m = map(int, input().split())
d = {}
for i in range(m):
    w1, w2 = input().split()
    d[w1] = w2 if len(w2) < len(w1) else w1
print(" ".join([d[s] for s in input().split()]))
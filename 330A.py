r, c = map(int, input().split())
r_set = set()
c_set = set()
for i in range(r):
    s = input()
    for j in range(c):
        if s[j] == "S":
            r_set.add(i)
            c_set.add(j)

print((r - len(r_set)) * c + (c - len(c_set)) * len(r_set))

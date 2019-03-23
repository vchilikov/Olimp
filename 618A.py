n = int(input())
a = []
for i in range(n):
    a.append(1)
    while len(a) > 1 and a[-2] == a[-1]:
        a.pop()
        a.append(a.pop() + 1)

print(" ".join(map(str, a)))

n = list(map(int, input()))
print(max(n))
for _ in range(max(n)):
    res = 0
    for i in range(len(n)):
        res *= 10
        if n[i] > 0:
            res += 1
            n[i] -= 1
    print(res)

n = int(input())
i = 2
res = []
while i ** 2 <= n:
    if n % i == 0:
        n //= i
        res.append(str(i))
    else:
        i += 1

if n > 1:
    res.append(str(n))

print(" ".join(res))